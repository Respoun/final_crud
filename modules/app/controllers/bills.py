''' controller and routes for bills '''
import os
from flask import request, jsonify
from app import app, mongo
import logger

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))


@app.route('/bills', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def bills():
    if request.method == 'GET':
        query = request.args
        try:
            data = mongo.db.Bills.find_one(query)
            return jsonify(data), 200
        except:
            return jsonify({'ok': False, 'message': 'Database unreachable'}), 500

    data = request.get_json()
    if request.method == 'POST':
        if data.get('id', None) is not None and data.get('client_id', None) is not None and data.get('sum', None) is not None:
            mongo.db.Bills.insert_one(data)
            return jsonify({'ok': True, 'message': 'Bills created successfully!'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'DELETE':
        if data.get('id', None) is not None:
            db_response = mongo.db.Bills.delete_one({'id': data['id']})
            if db_response.deleted_count == 1:
                response = {'ok': True, 'message': 'record deleted'}
            else:
                response = {'ok': True, 'message': 'no record found'}
            return jsonify(response), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'PATCH':
        if data.get('query', {}) != {}:
            mongo.db.Bills.update_one(
                data['query'], {'$set': data.get('payload', {})})
            return jsonify({'ok': True, 'message': 'record updated'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400
