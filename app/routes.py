from collections import defaultdict
from sqlalchemy.orm.exc import NoResultFound
from flask import Flask, redirect, request, abort, jsonify, Response
from flask import current_app as app
from .exceptions import APIException
from .models import Inventory
from .inventory_logic import get_sum_amount, get_new_values_for_articles, upload_products, \
                bulk_add_articles, get_all_articles, get_all_products, get_product, remove_product
from . import db

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return get_all_articles()

@app.route('/inventory', methods=['POST'])
def add_articles():
    inventory = request.json.get('inventory', '')
    if not inventory:
        raise APIException("There is no inventory", status_code=412)
    return bulk_add_articles(inventory)

@app.route('/inventory', methods=['DELETE'])
def clean_up():
    db.session.query(Inventory).delete()
    db.session.commit()
    return Response("{}", status=201, mimetype='application/json')

@app.route('/products', methods=['PUT'])
def add_products():
    products_data = request.json.get('products', '')
    if not products_data:
        raise APIException("There is no products", status_code=412)
    res = upload_products(products_data)
    return Response("", status=201, mimetype='application/json')

@app.route('/products', methods=['GET'])
def get_products():
    res = get_all_products()
    return res

@app.route('/products/<string:name>', methods=['GET'])
def get_product_by_name(name):
    try: 
        res = get_product(name)
        return res
    except NoResultFound:
        raise APIException("No product found", status_code=404)


@app.route('/products/<string:name>', methods=['PATCH'])
def remove_product_by_name(name):
    res = remove_product(name)
    return Response("{}", status=201, mimetype='application/json')
    