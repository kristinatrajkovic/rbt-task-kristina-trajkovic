from functools import wraps
from flask import request, jsonify

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token or not token.startswith("Bearer "):
            return jsonify({"error": "Authorization header required"}), 401

        auth_token = token.split(" ")[1]

        # dummy token
        if auth_token != "mysecrettoken":
            return jsonify({"error": "Invalid token"}), 403

        return f(*args, **kwargs)
    return decorated
