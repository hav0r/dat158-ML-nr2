from flask import Flask
from flask_bootstrap import Bootstrap
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_mapping(config)
cache=Cache(app)

from app import routes 