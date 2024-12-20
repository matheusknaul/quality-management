from flask import Blueprint, render_template, request, send_file, jsonify, flash, redirect, url_for, current_app
from database.models.norma import Norma
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

norma_route = Blueprint('norma', __name__)

@norma_route.route('/', methods=["GET"])
def lista_normas():
    normas = Norma.select()
    return render_template('normas/lista_normas.html', normas=normas)

@norma_route.route('/export_excel')
def exportar_excel():

    from utils.normas_excel_extract import gerar_excel

    normas = Norma.select(
        Norma.codigo,
        Norma.descricao,
        Norma.ano_norma,
        Norma.situacao,
        Norma.data_ultima_verificacao
    )

    dados = [[
        norma.codigo,
        norma.descricao,
        norma.ano_norma,
        norma.situacao,
        norma.data_ultima_verificacao
    ] for norma in normas]

    gerar_excel(dados)

    return send_file('utils\\normas_verificacao.xlsx', as_attachment=True, download_name="verificacao_normas.xlsx")

@norma_route.route('/', methods=["POST"])
def inserir_norma():
    data = request.json
    nova_norma = Norma.create(
        codigo = data['codigo'],
        descricao = data['descricao'],
        ano_norma = data['ano_norma'],
        situacao = 'Analisar'
    )

    print(data['ano_norma'])
    return render_template('normas/item_norma.html', norma=nova_norma)

@norma_route.route('/new')
def form_norma():
    return render_template('normas/form_norma.html')

@norma_route.route('/<int:norma_id>')
def detalhe_norma(norma_id):
    norma = Norma.get_by_id(norma_id)
    return render_template('normas/norma.html', norma=norma)

@norma_route.route('/<int:norma_id>/edit')
def editar_norma(norma_id):
    norma = Norma.get_by_id(norma_id)
    return render_template('normas/form_norma.html', norma=norma)

@norma_route.route('/<int:norma_id>/update', methods=['PUT'])
def atualizar_norma(norma_id):
    data = request.json
    norma_editada = Norma.get_by_id(norma_id)
    norma_editada.codigo = data['codigo']
    norma_editada.descricao = data['descricao']
    norma_editada.save()
    return render_template('normas/item_norma.html', norma=norma_editada)

@norma_route.route('/<int:norma_id>/delete', methods=['DELETE'])
def deletar_norma(norma_id):
    norma = Norma.get_by_id(norma_id)
    norma.delete_instance()
    return{'deleted': 'ok'}

# API

@norma_route.route('/api/normas', methods=['GET'])
def get_normas():

    normas = Norma.select(
        Norma.id,
        Norma.codigo,
        Norma.descricao,
        Norma.ano_norma,
        Norma.situacao,
        Norma.data_ultima_verificacao,
        Norma.tag_main,
        Norma.part_main,
        Norma.number_main,
        Norma.link
    )

    list_normas = []

    for norma in normas:
        list_normas.append({"id":norma.id,"codigo":norma.codigo, "descricao":norma.descricao, "ano":norma.ano_norma, "situacao":norma.situacao, "data_verificacao":norma.data_ultima_verificacao, "link":norma.link, "tag_main": norma.tag_main, "part_main": norma.part_main, "number_main": norma.number_main})

    return jsonify(list_normas)

@norma_route.route('/api/normas/edit<int:norma_id>', methods=['POST'])
def create_norma():
    norma = request.json
    return norma

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@norma_route.route('/importscope', methods=['POST'])
def upload_scope():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = current_app.config.get('UPLOAD_FOLDER', './uploads')
        os.makedirs(upload_folder, exist_ok=True)  # Garante que o diretório existe
        file.save(os.path.join(upload_folder, filename))
        return jsonify({'message': 'Arquivo enviado com sucesso', 'filename': filename}), 200

    return jsonify({'error': 'Extensão de arquivo não permitida'}), 400