# !!START
"""Flask Application"""
import os
from flask import Flask
from app import routes
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(routes.bp)
