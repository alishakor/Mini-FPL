#!/usr/bin/env python3
"""
flask app module
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def precious():
    return "hello prexy"


if __name__ == "__main__":
    app.run(debug=True)
