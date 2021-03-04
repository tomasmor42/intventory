from sqlalchemy.orm import validates, backref, relationship
from app import db


class Inventory(db.Model):
    art_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    stock = db.Column(db.Integer)
    @validates('stock')
    def validate_stock(self, key, stock):
        assert stock >= 0 
        return stock



class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    
    contain_articles = db.relationship(
        "ArticleInProduct", back_populates="product"
    )


class ArticleInProduct(db.Model):
    #__tablename__ = "contain_articles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    art_id = db.Column(db.Integer, nullable=False)
    amount_of = db.Column(db.Integer)

    product_name = db.Column(db.String, db.ForeignKey("product.name"), nullable=False)
    product = db.relationship("Product", back_populates="contain_articles", foreign_keys=[product_name])
