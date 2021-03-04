import pytest
from unittest import mock
from app.schemas import product_schema
from app.models import Inventory
import app.inventory_logic as inventory_logic


def test_get_sum_amount(products_json):
    products = product_schema.load(products_json['products']).data
    res = inventory_logic.get_sum_amount(products)
    assert 1 in res
    assert res[1] == 8   
    assert 3 in res
    assert res[3] == 1
    assert 5 not in res
    
def test_get_new_values_for_articles_valid():
    all_articles = {1: 2, 2: 3, 3: 4}
    articles_needed = {1: 1, 2: 3}
    res = inventory_logic.get_new_values_for_articles(articles_needed, all_articles)
    assert 1 in res
    assert res[1] == 1
    assert 2 in res
    assert res[2] == 0
    assert 3 in res
    assert res[3] == 4

def test_get_new_values_for_articles_invalid():
    all_articles = {1: 2, 2: 3, 3: 4}
    articles_needed = {1: 1, 2: 4}
    res = inventory_logic.get_new_values_for_articles(articles_needed, all_articles)
    assert res == {}
