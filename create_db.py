# create_db.py (create this file in your project root or inside app folder)

from app import create_app, db

app = create_app()
with app.app_context():
    db.create_all()
    print("Database tables created!")

