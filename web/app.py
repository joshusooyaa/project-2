"""
Josh Sawyers's Flask API.
"""

import os
import configparser

from flask import Flask, abort, send_from_directory

# Copied from project 0
def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config


app = Flask(__name__)

@app.route("/<path:request>")
def serve(request):
    if '~' in request or '..' in request: # Check for invalid characters in request
        abort(403)
    elif os.path.exists('pages/' + request): # See if path to file exists (from request) inside directory 'pages'
        return send_from_directory('pages/', request), 200
    else: # File doesn't exist
        abort(404)


@app.errorhandler(403) 
def forbidden(error):
    return send_from_directory('pages/', '403.html'), 403


@app.errorhandler(404)
def missing(error):
    return send_from_directory('pages/', '404.html'), 404


if __name__ == "__main__":
    config = parse_config(["credentials.ini", "default.ini"])
    cur_port = config["SERVER"]["PORT"]
    is_debug = config["SERVER"]["DEBUG"]
    app.run(debug=is_debug, host='0.0.0.0', port=cur_port)
