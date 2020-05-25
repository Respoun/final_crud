''' controller and routes for model '''
import os
from flask import request, jsonify
from app import app, mongo
import logger

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))

@app.route('/model', methods=['GET'])
def model():
    if request.method == 'GET':
        query = request.args
        try:
            data = mongo.db.Model.find_one(query)
            return jsonify(data), 200
        except:
            return jsonify({'ok': False, 'message': 'Database unreachable'}), 500
