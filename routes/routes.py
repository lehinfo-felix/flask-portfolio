from flask import Blueprint, render_template

routes_bp = Blueprint("routes", __name__)


@routes_bp.route("/")
def index():
    return render_template("index.html")


@routes_bp.route("/sobre")
def sobre():
    return render_template("sobre.html")


@routes_bp.route("/experiencia")
def experiencia():
    return render_template("experiencia.html")


@routes_bp.route("/formacao")
def formacao():
    return render_template("formacao.html")


@routes_bp.route("/contato")
def contato():
    return render_template("contato.html")
