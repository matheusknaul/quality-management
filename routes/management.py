from flask import Blueprint, render_template, request
from flask import request, jsonify
import json

management_route = Blueprint('management', __name__)

@management_route.route('/', methods=["POST"])
def track_time():
    data = json.loads(request.data)
    page = data.get('page')
    time_spent = data.get('timeSpent')

    print(f'O usuário ficou {time_spent} segundos na página {page}')

    return jsonify({'status': 'success'}), 200