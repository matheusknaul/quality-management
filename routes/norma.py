from flask import Blueprint, render_template, request
from database.norma import NORMAS

norma_route = Blueprint('norma', __name__)

@norma_route.route('/')
def lista_normas():
    return render_template('lista_normas.html', normas=NORMAS)

@norma_route.route('/', methods=["POST"])
def inserir_norma():
    data = request.json

    nova_norma = {
        "id": len(NORMAS) + 1,
        "codigo": data['codigo'],
        "descricao":data['descricao']
    }

    NORMAS.append(nova_norma)

    return render_template('item_norma.html', norma=nova_norma)

@norma_route.route('/new')
def form_norma():
    return render_template('form_norma.html')

@norma_route.route('/<int:norma_id>')
def detalhe_norma(norma_id):
    norma = list(filter(lambda n: n['id'] == norma_id, NORMAS))[0]
    return render_template('norma.html', norma=norma)

@norma_route.route('/<int:norma_id>/edit')
def editar_norma(norma_id):
    norma = None
    for n in NORMAS:
        if n['id'] == norma_id:
            norma = n

    return render_template('form_norma.html', norma=norma)

@norma_route.route('/<int:norma_id>/update', methods=['PUT'])
def atualizar_norma(norma_id):
    norma_editada = None
    data = request.json

    for n in NORMAS:
        if n['id'] == norma_id:
            n['codigo'] = data['codigo']
            n['descricao'] = data['descricao']

            norma_editada = n
    return render_template('item_norma.html', norma=norma_editada)

@norma_route.route('/<int:norma_id>/delete', methods=['DELETE'])
def deletar_norma(norma_id):
    global NORMAS
    NORMAS= [ n for n in NORMAS if n['id'] != norma_id ]
    return{'deleted': 'ok'}