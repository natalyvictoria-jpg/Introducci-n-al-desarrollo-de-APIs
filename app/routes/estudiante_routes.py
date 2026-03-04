from flask import Blueprint, request, jsonify
from app import db
from app.models import Estudiante
from flask_jwt_extended import jwt_required

estudiante_bp = Blueprint("estudiante", __name__, url_prefix="/estudiantes")

# CREAR
@estudiante_bp.route("/", methods=["POST"])
@jwt_required()
def crear_estudiante():
    data = request.get_json()

    nuevo = Estudiante(
        nombre=data["nombre"],
        correo=data["correo"]
    )

    db.session.add(nuevo)
    db.session.commit()

    return jsonify({"mensaje": "Estudiante creado"}), 201


# LISTAR TODOS
@estudiante_bp.route("/", methods=["GET"])
@jwt_required()
def listar_estudiantes():
    estudiantes = Estudiante.query.all()

    resultado = []
    for e in estudiantes:
        resultado.append({
            "id": e.id,
            "nombre": e.nombre,
            "correo": e.correo
        })

    return jsonify(resultado)


# OBTENER POR ID
@estudiante_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def obtener_estudiante(id):
    estudiante = Estudiante.query.get_or_404(id)

    return jsonify({
        "id": estudiante.id,
        "nombre": estudiante.nombre,
        "correo": estudiante.correo
    })


# ACTUALIZAR
@estudiante_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def actualizar_estudiante(id):
    estudiante = Estudiante.query.get_or_404(id)
    data = request.get_json()

    estudiante.nombre = data.get("nombre", estudiante.nombre)
    estudiante.correo = data.get("correo", estudiante.correo)

    db.session.commit()

    return jsonify({"mensaje": "Estudiante actualizado"})


# ELIMINAR
@estudiante_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def eliminar_estudiante(id):
    estudiante = Estudiante.query.get_or_404(id)

    db.session.delete(estudiante)
    db.session.commit()

    return jsonify({"mensaje": "Estudiante eliminado"})