import json 
import pytest
from app.schemas import articles_schema, ProductSchema
from app.exceptions import APIException

def fill_inventory(client, inventory_json, base_url):
    res = client.post(base_url+'/inventory', json=inventory_json)
    return res
def test_post_invnetory(client, inventory_json, base_url):
    rv = fill_inventory(client, inventory_json, base_url)
    assert rv.status_code == 200

def test_get_invnetory(client, inventory_json, base_url):
    rv = client.get('/inventory')
    assert rv.status_code == 200
    data = articles_schema.loads(rv.get_data())
    assert len(data.data) == 4

def test_add_products_not_valid_json(client, base_url):
    with pytest.raises(APIException):
        rv = client.put('/products', json={"key":"value"})

def test_fill_invnetory_not_valid_json(client, base_url):
    with pytest.raises(APIException):
        rv = client.post('/inventory', json={"key":"value"})

def test_add_products(client, base_url, products_json):
    res = client.put(base_url+'/products', json=products_json)
    assert res.status_code == 201
    articles = client.get('/inventory')
    data = articles_schema.loads(articles.get_data()).data
    stock = {article.art_id: article.stock for article in data}
    assert stock[4] == 0

def test_get_products(client, base_url):
    res = client.get(base_url+'/products')
    assert res.status_code == 200
    data = json.loads(res.get_data())
    assert len(data) == 2
def test_test_get_product_by_name(client, base_url):
    res = client.patch(base_url+'/products/Dining Chair')
    assert res.status_code == 201
    
def test_sell_product(client, base_url):
    res = client.patch(base_url+'/products/Dining Chair')
    assert res.status_code == 201
    data = client.get(base_url+'/products')
    data = json.loads(data.get_data())
    assert len(data) == 1

def test_get_product_by_name_empty(client, base_url):
    with pytest.raises(APIException):
        rv = client.get('/products/fake_product')