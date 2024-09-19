from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
import pytz

user_bp = Blueprint('user', __name__)
timezone = pytz.timezone('America/Sao_Paulo')

def get_current_time():
    return datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")

@user_bp.route('/user', methods=['GET'])
@jwt_required()
def get_users():
    """
    Obter informações do usuário
    ---
    tags:
      - Usuários
    security:
      - Bearer: []
    responses:
      200:
        description: Retorna uma mensagem para usuários com o papel de "user"
        schema:
          type: object
          properties:
            error:
              type: boolean
            message:
              type: string
            timestamp:
              type: string
      403:
        description: Acesso negado para papéis insuficientes
        schema:
          type: object
          properties:
            error:
              type: boolean
            message:
              type: string
            timestamp:
              type: string
    """
    claims = get_jwt_identity()
    
    if claims['role'] == 'user':
        return jsonify({
            "error": False,
            "message": "Você é um usuário normal.",
            "timestamp": get_current_time()
        }), 200
        
    return jsonify({
        "error": True,
        "message": "Acesso negado. Papel insuficiente.",
        "timestamp": get_current_time()
    }), 403

@user_bp.route('/admin', methods=['GET'])
@jwt_required()
def get_admin_data():
    """
    Obter informações administrativas
    ---
    tags:
      - Administração
    security:
      - Bearer: []
    responses:
      200:
        description: Retorna uma mensagem para usuários com o papel de "admin"
        schema:
          type: object
          properties:
            error:
              type: boolean
            message:
              type: string
            timestamp:
              type: string
      403:
        description: Acesso negado para papéis insuficientes
        schema:
          type: object
          properties:
            error:
              type: boolean
            message:
              type: string
            timestamp:
              type: string
    """
    claims = get_jwt_identity()
    
    if claims['role'] == 'admin':
        return jsonify({
            "error": False,
            "message": "Você tem acesso aos módulos administrativos.",
            "timestamp": get_current_time()
        }), 200
        
    return jsonify({
        "error": True,
        "message": "Acesso negado. Papel insuficiente.",
        "timestamp": get_current_time()
    }), 403
