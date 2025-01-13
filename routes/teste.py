from flask import Blueprint, render_template, url_for, request

teste_route = Blueprint('teste', __name__)

@teste_route.route('/')
def hello_world():
    return {"teste":"teste"}

