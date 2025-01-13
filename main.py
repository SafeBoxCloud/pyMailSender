from flask import Flask
from routes.teste import teste_route
from routes.email_endpoint import email_route

app = Flask(__name__)

app.register_blueprint(teste_route, url_prefix='/teste')
app.register_blueprint(email_route, url_prefix='/email')

app.run(debug=True)