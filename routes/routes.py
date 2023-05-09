from flask import Blueprint, render_template

routes_bp = Blueprint("routes", __name__)


@routes_bp.route("/")
def index():
    return render_template("index.html", \
    titulo_pagina="Início")


@routes_bp.route("/sobre")
def sobre():
    return render_template("sobre.html", \
    titulo_pagina="Sobre")


@routes_bp.route("/experiencia")
def experiencia():
    return render_template("experiencia.html", \
    titulo_pagina="Sobre")


@routes_bp.route("/formacao")
def formacao():
    return render_template("formacao.html", \
    titulo_pagina="Sobre")


@routes_bp.route("/contato")
def contato():
    return render_template("contato.html", \
    titulo_pagina="Sobre")
