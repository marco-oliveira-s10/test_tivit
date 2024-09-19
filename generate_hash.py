from werkzeug.security import generate_password_hash

user_password = "L0XuwPOdS5U"
user_password_hash = generate_password_hash(user_password)
print("Hash para usuário:", user_password_hash)

admin_password = "JKSipm0YH"
admin_password_hash = generate_password_hash(admin_password)
print("Hash para admin:", admin_password_hash)
