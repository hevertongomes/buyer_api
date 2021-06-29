from app import db
from datetime import datetime

class Buyer(db.Model):
    __tablename__ = "buyers"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    update_at = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    document = db.Column(db.String(100), nullable=False, unique=True, index=True)
    email = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(250), nullable=True)

    address_city_id = db.Column(db.Integer, db.ForeignKey('address_cities.id'),
        nullable=False)
    address_city = db.relationship('Address_City',
        backref=db.backref('buyers', lazy=True))
    
    def __init__(self, first_name, last_name, document, email, phone, address, address_city):
            self.first_name = first_name
            self.last_name = last_name
            self.document = document
            self.email = email
            self.phone = phone
            self.address = address
            self.address_city = address_city

    def __repr__(self):
        return f'<Buyer {self.first_name} : {self.document}'


class Address_City(db.Model):

    __tablename__ = "address_cities"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    address_state_id = db.Column(db.Integer, db.ForeignKey('address_states.id'),
        nullable=False)
    address_state = db.relationship('Address_State',
        backref=db.backref('address_cities', lazy=True))
    
    def __init__(self, name, address_state):
        self.name = name
        self.address_state = address_state
    
    def __repr__(self):
        return f'<Address_City {self.name}'


class Address_State(db.Model):

    __tablename__ = "address_states"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    uf = db.Column(db.String(100), nullable=True)

    def __init__(self, name, uf):
        self.name = name
        self.uf = uf

    def __repr__(self):
        return f'<Address_State {self.name}/{self.uf}'