from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app import db
from app.models import Usuario

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    nuevo = Usuario(
        username=data["username"],
        password=data["password"]
    )

    db.session.add(nuevo)
    db.session.commit()

    return jsonify({"mensaje": "Usuario registrado"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    usuario = Usuario.query.filter_by(username=data["username"]).first()

    if not usuario or usuario.password != data["password"]:
        return jsonify({"mensaje": "Credenciales incorrectas"}), 401

    access_token = create_access_token(identity=str(usuario.id))

    return jsonify({
        "access_token": access_token
    })