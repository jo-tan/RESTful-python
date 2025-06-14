import os
import subprocess
from app import create_app
from models.recipes import db

app = create_app()

MIGRATIONS_DIR = "migrations"
DB_PATH = os.getenv('DATABASE_URL', 'sqlite:///instance/recipes.db').replace('sqlite:///', '')

with app.app_context():
    # Step 1: Ensure database file exists (SQLite-specific)
    if not os.path.exists(DB_PATH):
        print(f"🗃 Creating database file at {DB_PATH}...")
        open(DB_PATH, 'a').close()  # Touch file
    else:
        print(f"✅ Database already exists at {DB_PATH}.")

    # Step 2: Initialize migrations if not already present
    if not os.path.exists(MIGRATIONS_DIR):
        print("📁 Initializing migrations directory...")
        subprocess.run(["flask", "db", "init"])
    else:
        print("📁 Migrations directory already exists.")

    # Step 3: Generate migration script from current models
    print("✏️ Generating migration script...")
    subprocess.run(["flask", "db", "migrate", "-m", "Initial schema"])

    # Step 4: Apply migrations (create tables)
    print("🚀 Applying migration to database...")
    subprocess.run(["flask", "db", "upgrade"])

    print("✅ Database and migrations fully initialized.")
