# !!START
"""Flask Application"""
from flask import (Flask, render_template, redirect, request)
from .config import Config

app = Flask(__name__)

app.config.from_object(Config)
