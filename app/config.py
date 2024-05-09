# !!START
"""Flask Config"""
import os

class Config:
    """Configures Flask application"""
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # define any other secret environment variables here

# !!END