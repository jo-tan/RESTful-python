#!/bin/sh
set -e

# 1. Check if under venv
in_venv() {
    [ -n "$VIRTUAL_ENV" ]
}

# 2. Start venv if not activate
if ! in_venv; then
    if [ -f ".venv/bin/activate" ]; then
        echo "🤖 Activating python virtual environment ..."
        source .venv/bin/activate
    else
        echo "❌ Virtual environment not found... Have you create it? 🫥"
        echo "💡 Tip: Run 'python3 -m venv .venv' to create it."
        exit 1
    fi
else
    echo "📦 Already in the virtual environment..."
fi

# 3. Check and set environment variables if not set
if [ -f "instance/.env" ]; then
    echo "📄 Loading environment variables from instance/.env ..."
    export $(grep -v '^#' instance/.env | xargs)
else
    echo "⚠️  No .env file found in /instance. Using default or exported env vars."
fi


# 4. Check and Install dependencies
echo "📚 Checking Python dependencies..."
pip install --quiet --upgrade pip setuptools wheel

if [ -f "requirements.txt" ]; then
    echo "🔍 Installing/updating packages from requirements.txt..."
    pip install -r requirements.txt -qq
else
    echo "⚠️  requirements.txt not found. Skipping package installation."
fi

# 5. Ensure instance and logs directory exist
mkdir -p instance
mkdir -p logs

# 6. Auto-init migrations if missing
if [ ! -d "migrations" ] || [ ! -f "migrations/env.py" ]; then
    echo "🧱 No valid migrations folder found. Initializing Flask-Migrate..."
    flask db init
fi

# 7. Create database if not exists (for SQLite only)
if [ ! -f "instance/recipes.db" ]; then
    echo "🗃️  Creating empty SQLite database..."
    touch instance/recipes.db
fi

# 8. Apply migrations with timestamp & git info
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
git_commit=$(git rev-parse --short HEAD 2>/dev/null || echo "no-git")

echo "🔄 Generating and applying migration..."
flask db migrate -m "Auto migration at $timestamp (commit $git_commit)" || echo "⚠️  Nothing to migrate."
flask db upgrade

# 9. Start app
echo "✅ Starting Flask app with debug mode ... "
flask run --debug


