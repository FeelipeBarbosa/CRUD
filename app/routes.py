from flask import request, redirect, url_for, render_template, flash
from app import app, db
from app.models import item

@app.route('/')
def index():
    items = item.query.all()
    return render_template('index.html', items=items)