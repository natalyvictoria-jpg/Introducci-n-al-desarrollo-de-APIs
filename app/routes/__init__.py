from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensaje": "API funcionando correctamente",
        "version": "1.0"
    })