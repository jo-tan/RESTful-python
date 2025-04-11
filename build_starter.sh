#!/bin/sh
set -e
# 1. Check if under venv
in_venv() {
    [ -n "$VIRTUAL_ENV" ]
}

# 2. Start venv if not activate
if ! in_venv; then
    if [ -f ".venv/bin/activate" ]; then
        echo "🤖 Activatin python virtual environment ..."
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
if [ -z "$FLASK_APP" ]; then
    export FLASK_APP=app.py
    echo "🔨 set FLASK_APP=app.py"
fi

if [ -z "$FLASK_ENV" ]; then
    export FLASK_ENV=development
    echo "🔧 set FLASK_ENV=developemnt"
fi

# 4. start Flask
echo "✅ Staring Flask app with debug mode ... "
flask run --debug

