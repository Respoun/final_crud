import os
import sys
import requests
from flask import jsonify, request, make_response, send_from_directory, render_template

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))

import logger
from app import app

LOG = logger.get_root_logger(os.environ.get(
    'ROOT_LOGGER', 'root'), filename=os.path.join(ROOT_PATH, 'output.log'))

PORT = os.environ.get('PORT')


@app.errorhandler(404)
def not_found(error):
    """ error handler """
    LOG.error(error)
    return make_response(jsonify({'error': 'Not found'}), 404)

'''
GET ROUTES
'''
@app.route('/')
def index():
    return send_from_directory('dist', 'index.html')

'''
ADD ROUTES
'''
@app.route('/add_brewery')
def add_brewery():
    return send_from_directory('dist', 'add_brewery.html')

@app.route('/add_user')
def add_user():
    return send_from_directory('dist', 'add_user.html')

@app.route('/add_bill')
def add_bill():
    return send_from_directory('dist', 'add_bills.html')

@app.route('/add_product')
def add_product():
    return send_from_directory('dist', 'add_product.html')

@app.route('/add_style')
def add_style():
    return send_from_directory('dist', 'add_style.html')

@app.route('/add_country')
def add_country():
    return send_from_directory('dist', 'add_country.html')


@app.route('/<path:path>')
def static_proxy(path):
    file_name = path.split('/')[-1]
    dir_name = os.path.join('dist', '/'.join(path.split('/')[:-1]))
    return send_from_directory(dir_name, file_name)


if __name__ == '__main__':
    LOG.info('running environment: %s', os.environ.get('ENV'))
    app.config['DEBUG'] = os.environ.get('ENV') == 'development'
    app.run(host='0.0.0.0', port=int(PORT))
