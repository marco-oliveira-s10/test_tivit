from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from services.auth_service import generate_token, check_token
import pytz
from datetime import datetime

auth_bp = Blueprint('auth', __name__)
timezone = pytz.timezone('America/Sao_Paulo')

@auth_bp.route('/token', methods=['POST'])
def token():
    """
    Geração de Token JWT
    ---
    tags:
      - Autenticação
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              description: Nome de usuário
            password:
              type: string
              description: Senha do usuário
    responses:
      200:
        description: Token gerado com sucesso
        schema:
          type: object
          properties:
            access_token:
              type: string
              description: Token JWT gerado
            expires_in:
              type: integer
              description: Expiração do token em segundos
            timestamp:
              type: string
              description: Hora da geração do token
      401:
        description: Falha de autenticação
    """
    return generate_token(request)
