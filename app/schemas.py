from flask_restful import fields

buyer_field = {
    "id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "document": fields.String,
    "email": fields.String,
    "phone": fields.String,
    "address": fields.String
}


address_city_field = {
    "id": fields.Integer,
    "name": fields.String,
}

address_state_field = {
    "id": fields.Integer,
    "name": fields.String,
    "uf": fields.String,
}