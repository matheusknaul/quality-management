from flask import Blueprint, render_template

norma_route = Blueprint('norma', __name__)

@norma_route.route('/')
def lista_normas():
    return render_template('lista_normas.html')

@norma_route.route('/', methods=["POST"])
def inserir_norma():
    pass

@norma_route.route('/new')
def form_norma():
    return render_template('form_norma.html')

@norma_route.route('/<int:norma_id>')
def detalhe_norma(norma_id):
    return render_template('norma.html')

@norma_route.route('/<int:norma_id>/edit')
def editar_norma(norma_id):
    return render_template('form_norma.html')

@norma_route.route('/<int:norma_id>/update', methods=['PUT'])
def atualizar_norma(norma_id):
    pass

@norma_route.route('/<int:norma_id>/delete', methods=['DELETE'])
def deletar_norma(norma_id):
    pass