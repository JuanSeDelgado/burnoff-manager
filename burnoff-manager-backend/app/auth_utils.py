
from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.models import Admin

def admin_required(superadmin_only=False):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                # Verifica que haya un JWT válido en la request
                verify_jwt_in_request()

                # Extrae la identidad (admin_id) desde el JWT
                admin_id = get_jwt_identity()

                # Verifica en la base de datos que ese admin exista
                admin = Admin.query.get(admin_id)
                if not admin:
                    return jsonify({"msg": "Admin no encontrado"}), 404

                # Verifica si es superadmin si se requiere
                if superadmin_only and not admin.superadmin:
                    return jsonify({"msg": "Permisos insuficientes: requiere superadmin"}), 403

                # Opcional: adjuntar el admin al objeto request
                request.admin = admin

                return fn(*args, **kwargs)

            except Exception as e:
                return jsonify({"msg": "Error de autenticación", "error": str(e)}), 401

        return wrapper
    return decorator
