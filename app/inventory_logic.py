from . import db
from sqlalchemy.orm.exc import NoResultFound
from .models import Inventory, Product
from .schemas import articles_schema,  article_schema, product_entity_schema, product_schema

import json

def get_sum_amount(products):
    articles = {}
    for product in products:
        for art in product.contain_articles:
            if art.art_id in articles:
                articles[art.art_id] += art.amount_of
            else:
                articles[art.art_id] = art.amount_of
    return articles

def get_new_values_for_articles(articles_needed, all_articles):
    new_values = all_articles
    for article, amount in articles_needed.items():

        if amount > all_articles.get(article, 0):
            return {}
        new_values[article] = all_articles.get(article, 0) - amount
    return new_values

def filter_required_articles(required_articles):
    all_inventory = articles_schema.dump(Inventory.query.filter(Inventory.art_id.in_(required_articles.keys())).all())
    inventory_dict = {art['art_id']: art['stock'] for art in all_inventory.data}
    return inventory_dict

def upload_products(products_data):
    products = product_schema.load(products_data).data
    required_articles = get_sum_amount(products)
    new_values = get_new_values_for_articles(required_articles, filter_required_articles(required_articles))
    if new_values:
        dict_for_update = [{'art_id': atr_id, 'stock': stock} for atr_id, stock in new_values.items()]
        db.session.bulk_update_mappings(Inventory, dict_for_update)
        db.session.add_all(products)
        db.session.commit()
    else: 
        raise ValueError("Not enough articles in stock")

def bulk_add_articles(articles):
    db.session.add_all(articles_schema.load(articles).data)
    db.session.commit()
    return articles_schema.dumps(articles)

def get_all_articles():
    inventory = Inventory.query.all()
    return articles_schema.dumps(inventory)

def get_all_products():
    products = Product.query.all()
    return product_schema.dumps(products)

def get_product(name):
    product = Product.query.filter_by(name=name).one()
    return product_entity_schema.dumps(product)

def remove_product(name):
    Product.query.filter_by(name=name).delete()
    db.session.commit()
    