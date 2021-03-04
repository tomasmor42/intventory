# from datetime import datetime
# from flask_wtf import FlaskForm
# from wtforms import StringField
# from wtforms.fields.html5 import DateField
# from wtforms.validators import DataRequired

# class ForecastForm(FlaskForm):
#     Inventories = StringField('city', validators=[DataRequired()])

from marshmallow import post_load, Schema, fields
from marshmallow_sqlalchemy.fields import Nested
from . import ma, db
from .models import Inventory, Product, ArticleInProduct
    

class InventorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inventory
    
    @post_load
    def make_article(self, data, **kwargs):
        return Inventory(**data)
    
class ArticleInProductSchema(ma.SQLAlchemyAutoSchema):
    fields = ('amount_of', 'art_id')
    class Meta:
        model = ArticleInProduct
        sqla_session = db.session
        load_instance = True
        include_relationships = True


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        sqla_session = db.session
        load_instance = True
        include_relationships = True

    contain_articles = ma.Nested(ArticleInProductSchema, many=True)


article_schema = InventorySchema()
articles_schema = InventorySchema(many=True)
product_schema = ProductSchema(many=True)
product_entity_schema = ProductSchema()