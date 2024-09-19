import unittest
from app import app, db
from models import User

class UserRoutesTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        self.create_test_users()

    def create_test_users(self):
        user = User(username="user", password="password", role="user")
        admin = User(username="admin", password="password", role="admin")
        db.session.add(user)
        db.session.add(admin)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_jwt_generation(self):
        response = self.app.post('/token', json={
            'username': 'user',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)

    def test_access_user_route_as_user(self):
        # Obter token JWT para usuário normal
        response = self.app.post('/token', json={
            'username': 'user',
            'password': 'password'
        })
        token = response.json['access_token']

        # Acessar rota protegida como usuário normal
        response = self.app.get('/users', headers={
            'Authorization': f'Bearer {token}'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Você é um usuário normal.', response.json['message'])

    def test_access_admin_route_as_admin(self):
        # Obter token JWT para admin
        response = self.app.post('/token', json={
            'username': 'admin',
            'password': 'password'
        })
        token = response.json['access_token']

        # Acessar rota protegida como admin
        response = self.app.get('/admin', headers={
            'Authorization': f'Bearer {token}'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Você tem acesso aos módulos administrativos.', response.json['message'])

    def test_access_admin_route_as_user(self):
        # Obter token JWT para usuário normal
        response = self.app.post('/token', json={
            'username': 'user',
            'password': 'password'
        })
        token = response.json['access_token']

        # Tentar acessar a rota de admin como usuário normal
        response = self.app.get('/admin', headers={
            'Authorization': f'Bearer {token}'
        })
        self.assertEqual(response.status_code, 403)  # Espera-se que seja negado

if __name__ == '__main__':
    unittest.main()
