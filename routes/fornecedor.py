from flask import Blueprint, render_template, request
from database.models.fornecedor import Fornecedor, Categoria

fornecedor_route = Blueprint('fornecedor', __name__)

@fornecedor_route.route('/')
def listar_fornecedores():
    fornecedores = Fornecedor.select()
    return render_template('fornecedores/lista_fornecedores.html', fornecedores=fornecedores)

@fornecedor_route.route('/', methods=["POST"])
def inserir_fornecedor():
    data = request.json

    novo_fornecedor = Fornecedor.create(
        nome = data['nome'],
        email = data['email'],
        estado = data['estado'],
        cidade = data['cidade'],
        cep = data['cep'],
        endereco = data['endereco'],
        cnpj = data['cnpj'],
        ie = data['ie'],
        categoria = data['categoria']
    )

    return render_template('fornecedores/item_fornecedor.html', fornecedor=novo_fornecedor)

@fornecedor_route.route('/new')
def form_fornecedor():
    return render_template('fornecedores/form_fornecedor.html')

@fornecedor_route.route('/<int:fornecedor_id>')
def visualizar_fornecedor(fornecedor_id):

    fornecedor = Fornecedor.get_by_id(fornecedor_id)

    return render_template('fornecedores/fornecedor.html', fornecedor=fornecedor)

@fornecedor_route.route('/<int:fornecedor_id>/edit')
def editar_fornecedor(fornecedor_id):
    fornecedor = Fornecedor.get_by_id(fornecedor_id)
    return render_template('fornecedores/form_fornecedor.html', fornecedor=fornecedor)

@fornecedor_route.route('/<int:fornecedor_id>/update', methods=['PUT'])
def atualizar_fornecedor(fornecedor_id):
    data = request.json
    fornecedor_editado = Fornecedor.get_by_id(fornecedor_id)

    fornecedor_editado.nome = data['nome'],
    fornecedor_editado.email = data['email'],
    fornecedor_editado.estado = data['estado'],
    fornecedor_editado.cidade = data['cidade'],
    fornecedor_editado.cep = data['cep'],
    fornecedor_editado.endereco = data['endereco'],
    fornecedor_editado.cnpj = data['cnpj'],
    fornecedor_editado.ie = data['ie'],
    fornecedor_editado.categoria = data['categoria']

    fornecedor_editado.save()

    return render_template('fornecedores/item_fornecedor.html', fornecedor=fornecedor_editado)

@fornecedor_route.route('/<int:fornecedor_id>/update', methods=['DELETE'])
def deletar_fornecedor(fornecedor_id):
    fornecedor = Fornecedor.get_by_id(fornecedor_id)
    fornecedor.delete_instance()
    return {'deleted': 'ok'}
