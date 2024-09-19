# Teste Técnico - Desenvolvedor Backend Tivit
Projeto utilizando Flask (Python)

## Descrição
O objetivo deste teste é desenvolver uma API em Python, que interaja com a situação descrita nas instruções abaixo. A API deverá armazenar os dados em um banco de dados e disponibilizá-los por meio de endpoints protegidos.

## Instruções

1. **Configuração Inicial**
   - Utilize o framework Flask para construir a API.
   - Estruture o projeto utilizando as seguintes pastas:
     - `routes`: responsável pelas rotas da API.
     - `services`: lógica de negócio e serviços auxiliares.
     - `models`: definição das entidades e persistência com o banco de dados.

2. **Desenvolvimento da API**

   - **Autenticação**:  
     Crie um endpoint `/token` que gere um token JWT (JSON Web Token) quando o usuário fornecer as credenciais corretas. O token será utilizado para autenticar e autorizar o acesso às rotas protegidas.
   
   - **Rotas Protegidas**:
     - `/user`: Acessível apenas por usuários autenticados com o papel `user`.
     - `/admin`: Acessível apenas por usuários autenticados com o papel `admin`.
   
   - **Segurança com JWT**:  
     O token JWT será gerado na rota `/token` e deverá ser incluído no header `Authorization` com o formato `Bearer <token>` para acessar as demais rotas.

   - **Banco de Dados e Usuários Fictícios**:
   	 Utilize os dados de login e senha mencionados na seção de "usuários fictícios" para autenticação.
     Estrutura para armazenar usuários fictícios com as seguintes credenciais:
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
   - Integre a documentação da API utilizando Swagger para que todos os endpoints estejam devidamente descritos e acessíveis via interface gráfica.

4. **Testes Automatizados**
   - Implemente testes unitários cobrindo as principais funcionalidades da API. Os testes devem incluir:
     - Verificação da geração correta do token JWT.
     - Validação do acesso às rotas protegidas de acordo com o papel do usuário (user/admin).
     - Testes para falhas de autenticação (token inválido ou ausente).
   
5. **Segurança**
   - **Importante**: Não exponha credenciais sensíveis diretamente no código-fonte. Utilize variáveis de ambiente para armazenar dados sensíveis, como as credenciais de acesso ao banco de dados ou chaves secretas de JWT.

## Entrega
- O código-fonte do projeto deve ser disponibilizado em um repositório GitHub.
- Incluir no repositório um arquivo README com instruções claras de como executar o projeto localmente, incluindo:
  - Configuração de variáveis de ambiente.
  - Comandos para criar e popular o banco de dados.
  - Instruções para rodar os testes.

- Adicionar uma coleção Postman com exemplos de requisições para cada rota desenvolvida.

## Links de Exemplos
Para referência, veja exemplos de endpoints funcionando:
- [Health Check](https://api-onecloud.multicloud.tivit.com/fake/health) - public
- [Rota Admin](https://api-onecloud.multicloud.tivit.com/fake/admin) - private
- [Rota User](https://api-onecloud.multicloud.tivit.com/fake/user) - private
- [Autenticação](https://api-onecloud.multicloud.tivit.com/fake/token) - public
