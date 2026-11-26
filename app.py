"""Serve the shop's web page."""

import os
import socket

import redis
from flask import Flask

from build import ITEMS, page

app = Flask(__name__)
VERSION = os.environ.get("VERSION", "dev")

store = redis.Redis(
    host=os.environ.get("REDIS_HOST", "localhost"),
    socket_connect_timeout=1
)


@app.route("/")
def home():
    try:
        visits = store.incr("visits")
    except redis.exceptions.RedisError:
        visits = "unknown"

    extra = f"<p>Visits: {visits}. Served by {socket.gethostname()}</p>"
    return page(ITEMS, VERSION) + extra


@app.route("/health")
def health():
    return {"status": "ok"}