from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity
from models import db, User
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash
import pytz

user_tokens = {}
timezone = pytz.timezone('America/Sao_Paulo')

def generate_token(request):
    username = request.json.get('username')
    password = request.json.get('password')

    # Encontre o usuário pelo nome de usuário
    user = User.query.filter_by(username=username).first()

    # Verifique se o usuário existe e se a senha está correta
    if user and check_password_hash(user.password, password):  # Verifique a senha com hash
        current_time = datetime.now(timezone)
        current_token_info = user_tokens.get(user.id)

        if current_token_info and current_token_info['expires_at'] > current_time:
            remaining_time = int((current_token_info['expires_at'] - current_time).total_seconds())
            return jsonify({
                "error": False,
                "access_token": current_token_info['token'],
                "expires_in": remaining_time,
                "timestamp": datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
            }), 200

        expires = timedelta(minutes=1)
        access_token = create_access_token(
            identity={'id': user.id, 'username': user.username, 'role': user.role},
            expires_delta=expires
        )

        user_tokens[user.id] = {
            'token': access_token,
            'expires_at': current_time + expires
        }

        return jsonify({
            "error": False,
            "access_token": access_token,
            "expires_in": 60,  # 1 minuto em segundos
            "timestamp": datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
        }), 200

    return jsonify({
        "error": True,
        "message": "Bad username or password",
        "timestamp": datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
    }), 401

def check_token():
    claims = get_jwt_identity()
    current_token_info = user_tokens.get(claims['id'])

    if current_token_info:
        remaining_time = int((current_token_info['expires_at'] - datetime.now(timezone)).total_seconds())
        if remaining_time > 0:
            return jsonify({
                "error": False,
                "message": "Token válido.",
                "expires_in": remaining_time,
                "timestamp": datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
            }), 200

        return jsonify({
            "error": True,
            "message": "Token expirado",
            "timestamp": datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
        }), 401

    return jsonify({
        "error": True,
        "message": "Nenhum token encontrado.",
        "timestamp": datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
    }), 404
