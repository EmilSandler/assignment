from app import app
from db import db

db.init_app(app=app)

# Create all tables before first request if not exists.
@app.before_first_request
def create_tables():
    db.create_all()