# Teste Técnico - Desenvolvedor Backend Tivit
Projeto utilizando Flask (Python)

## Descrição
O objetivo deste teste é desenvolver uma API em Python, que interaja com a situação descrita nas instruções abaixo. A API deverá armazenar os dados em um banco de dados e disponibilizá-los por meio de endpoints protegidos.

## Instruções

1. **Configuração Inicial**
   - Utilize o framework Flask para construir a API. - OK
   - Estruture o projeto utilizando as seguintes pastas:
     - `routes`: responsável pelas rotas da API. - OK
     - `services`: lógica de negócio e serviços auxiliares. - OK
     - `models`: definição das entidades e persistência com o banco de dados. - OK

2. **Desenvolvimento da API**

   - **Autenticação**:  
     Crie um endpoint `/token` que gere um token JWT (JSON Web Token) quando o usuário fornecer as credenciais corretas. O token será utilizado para autenticar e autorizar o acesso às rotas protegidas. - OK
   
   - **Rotas Protegidas**:
     - `/user`: Acessível apenas por usuários autenticados com o papel `user`. - OK
     - `/admin`: Acessível apenas por usuários autenticados com o papel `admin`. - OK
   
   - **Segurança com JWT**:  
     O token JWT será gerado na rota `/token` e deverá ser incluído no header `Authorization` com o formato `Bearer <token>` para acessar as demais rotas. - OK

   - **Banco de Dados e Usuários Fictícios**:
   	 Utilize os dados de login e senha mencionados na seção de "usuários fictícios" para autenticação. - OK (Postgres, optei por não usar migrations)
     Estrutura para armazenar usuários fictícios com as seguintes credenciais: - OK
     ```json
     {
       "user": {
         "username": "user",
         "role": "user",
         "password": "L0XuwPOdS5U"
       },
       "admin": {
         "username": "admin",
         "role": "admin",
         "password": "JKSipm0YH"
       }
     }
     ```

3. **Documentação da API**
   - Integre a documentação da API utilizando Swagger para que todos os endpoints estejam devidamente descritos e acessíveis via interface gráfica. - OK (http://localhost:5000/apidocs/#/Usuários/get_users)

4. **Testes Automatizados**
   - Implemente testes unitários cobrindo as principais funcionalidades da API. Os testes devem incluir:
     - Verificação da geração correta do token JWT. - OK
     - Validação do acesso às rotas protegidas de acordo com o papel do usuário (user/admin). - OK
     - Testes para falhas de autenticação (token inválido ou ausente). - OK
     # python -m unittest discover -s tests - OK
   
5. **Segurança**
   - **Importante**: Não exponha credenciais sensíveis diretamente no código-fonte. Utilize variáveis de ambiente para armazenar dados sensíveis, como as credenciais de acesso ao banco de dados ou chaves secretas de JWT. (Optei por não criar o arquivo .env por se tratar de um teste)

## Entrega
- O código-fonte do projeto deve ser disponibilizado em um repositório GitHub. - OK
- Incluir no repositório um arquivo README com instruções claras de como executar o projeto localmente, incluindo:
  - Configuração de variáveis de ambiente. 
  - Comandos para criar e popular o banco de dados. - OK
  - Instruções para rodar os testes. - OK

- Adicionar uma coleção Postman com exemplos de requisições para cada rota desenvolvida. - OK

## Links de Exemplos
Para referência, veja exemplos de endpoints funcionando:
- [Health Check](https://api-onecloud.multicloud.tivit.com/fake/health) - public
- [Rota Admin](https://api-onecloud.multicloud.tivit.com/fake/admin) - private
- [Rota User](https://api-onecloud.multicloud.tivit.com/fake/user) - private
- [Autenticação](https://api-onecloud.multicloud.tivit.com/fake/token) - public

## Instruções de Instalação e Execução

Observações:

Passo 1: Instalar o Python
Certifique-se de que o Python está instalado em sua máquina.

Passo 2: Baixar Dependências
Navegue até o diretório do seu projeto e execute o seguinte comando para instalar as dependências:pip install -r requirements.txt

Passo 3: Configurar o Banco de Dados
Crie o esquema do banco de dados.
Importe o arquivo db_test_tivit.sql para o banco de dados.
Gere uma nova senha para cada usuário usando o script generate_hash.py e atualize as senhas no banco de dados.


Passo 4: Rodar Testes Unitários
Execute os testes unitários com o seguinte comando:python -m unittest discover -s tests

Passo 5: Rodar a Aplicação
Inicie a aplicação Flask com o comando:flask run

Passo 6: Acessar a Documentação da API Para visualizar os payloads e respostas, acesse a documentação Swagger em: http://localhost:5000/apidocs/#/Usuários/get_users

Você também pode usar ferramentas como Postman para testar suas rotas, importando a coleção disponível no arquivo: Test Tivit.postman_collection.json

Para qualquer dúvida, entre em contato comigo: marco.oliveira.s10@gmail.com


#INFO:

Informações adicionais:

Aproximadamente 2 horas de desenvolvimento.
Complexidade de implementação: 1 (de 0 a 10).
Complexidade de entender o desafio: 4 (de 0 a 10).