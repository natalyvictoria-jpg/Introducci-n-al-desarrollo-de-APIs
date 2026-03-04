from app import create_app, db
from app.models import Estudiante  # ← IMPORTANTE
from app.models import Estudiante, Usuario

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Tablas creadas correctamente")

    print("Servidor iniciado en http://localhost:5000")
    app.run(debug=True)