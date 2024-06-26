from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comment(db.Model):
    __tablename__= 'comment'
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(200), nullable=False)
    

class User(db.Model):
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    firstname= db.Column(db.String(80), unique=False, nullable=False)
    lastname= db.Column(db.String(80), unique=False, nullable=False)
    username= db.Column(db.String(80), unique=False, nullable=False)
    address= db.Column(db.String(80), unique=False, nullable=False)
    user_calification = db.Column(db.Integer, unique=False, nullable=False)
    comments= db.relationship('Comment', backref='user')
    wishes = db.relationship('Wishlist', backref='user')
    products= db.relationship('Product', backref='user')
    
    def __repr__(self):
        return f'<User {self.email}>'
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Wishlist(db.Model):
    __tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

class Publication(db.Model):
    __tablename__= 'publication'
    id = db.Column(db.Integer, primary_key=True)
    value= db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    product_description = db.Column(db.String(400), nullable=False)
    state = db.Column(db.Boolean, nullable=False)
    offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'))
    wishes = db.relationship('Wishlist', backref='publication') 




class Category(db.Model):
    __tablename__= 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    products= db.relationship('Product', backref='category')

class Product(db.Model):
    __tablename__= 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(200), nullable=False)
    product_info = db.Column(db.String(400), nullable=False)
    brand = db.Column(db.String(200), nullable=False)
    state = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id= db.Column(db.Integer, db.ForeignKey('category.id'))
    offers= db.relationship('Offer', backref='product')

    




class Offer(db.Model):
    __tablename__= 'offer'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    offer_product_value = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(200), nullable=False)
    product_description = db.Column(db.String(200), nullable=False)
    state = db.Column(db.Boolean, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    offers= db.relationship('Publication', backref='offer')

    
