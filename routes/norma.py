from flask import Blueprint, render_template, request
from database.models.norma import Norma

norma_route = Blueprint('norma', __name__)

@norma_route.route('/')
def lista_normas():
    normas = Norma.select()
    return render_template('normas/index.html', normas=normas)

@norma_route.route('/', methods=["POST"])
def inserir_norma():

    data = request.json

    nova_norma = Norma.create(
        codigo = data['codigo'],
        descricao = data['descricao'],
        ano_norma = 0,
        situacao = 0,
    )

    return render_template('item_norma.html', norma=nova_norma)

@norma_route.route('/new')
def form_norma():
    return render_template('form_norma.html')

@norma_route.route('/<int:norma_id>')
def detalhe_norma(norma_id):

    norma = Norma.get_by_id(norma_id)

    return render_template('norma.html', norma=norma)

@norma_route.route('/<int:norma_id>/edit')
def editar_norma(norma_id):
    norma = Norma.get_by_id(norma_id)

    return render_template('form_norma.html', norma=norma)

@norma_route.route('/<int:norma_id>/update', methods=['PUT'])
def atualizar_norma(norma_id):
    data = request.json
    norma_editada = Norma.get_by_id(norma_id)

    norma_editada.codigo = data['codigo']
    norma_editada.descricao = data['descricao']
    norma_editada.save()
    
    return render_template('item_norma.html', norma=norma_editada)

@norma_route.route('/<int:norma_id>/delete', methods=['DELETE'])
def deletar_norma(norma_id):
    norma = Norma.get_by_id(norma_id)
    norma.delete_instance()
    return{'deleted': 'ok'}