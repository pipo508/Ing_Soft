from flask import jsonify, request, Blueprint
from app.mapping.user_schema import UserSchema
from app.services.user_service import UserService
user = Blueprint('user', __name__)
user_schema =  UserSchema()

def handle_exception(e, message):
    return jsonify({"error": f"{message}: {str(e)}"}), 500
def get_user_response(user, success_code=200, not_found_message="Usuario no encontrado"):
    if user:
        return jsonify({"user": user_schema.dump(user)}), success_code
    else:
        return jsonify({"error": not_found_message}), 404
def get_user_service():
    return UserService()
@user.route('/add', methods=['POST'])
def post_user():
    try:
        user_data = request.get_json()
        user = user_schema.load(user_data)
        return get_user_response(get_user_service().create(user))
    except Exception as e:
        return handle_exception(e, "Error al crear usuario")
