'''
controller and routes for Products (Beers)
'''
import os
from flask import request, jsonify, render_template
from app import app, mongo
import logger
import json

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))


@app.route('/products', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def products():
    if request.method == 'GET':
        query = request.args
        try:
            data = mongo.db.Products.find()
            response = []
            for document in data:
                document['_id'] = str(document['_id'])
                img = mongo.db.Images.find_one({"id": document["id_pics"]})
                full_data = {**document, **img}
                response.append(full_data)
            return render_template("products.html", response=response), 200
        except:
            return jsonify({'ok': False, 'message': 'Database unreachable'}), 500


    if request.method == 'POST':
        data = request.get_json(force=True)
        if data.get('id', None) is not None and data.get('name', None) is not None and data.get('price', None) is not None:
            mongo.db.Products.insert_one(data)
            return jsonify({'ok': True, 'message': 'Product created successfully!'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'DELETE':
        if data.get('id', None) is not None:
            db_response = mongo.db.Products.delete_one({'id': data['id']})
            if db_response.deleted_count == 1:
                response = {'ok': True, 'message': 'record deleted'}
            else:
                response = {'ok': True, 'message': 'no record found'}
            return jsonify(response), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'PATCH':
        if data.get('query', {}) != {}:
            mongo.db.Products.update_one(data['query'], {'$set': data.get('payload', {})})
            return jsonify({'ok': True, 'message': 'record updated'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400
