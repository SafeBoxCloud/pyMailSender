from flask import Flask
from routes.teste import teste_route


app = Flask(__name__)

app.register_blueprint(teste_route, url_prefix='/teste')

app.run(debug=True)