from flask_restful import Resource, marshal
from app.models import Buyer, Address_City, Address_State
from app import request, db
from app.schemas import buyer_field

class Buyers(Resource):

    def post(self):

        payload = request.only([
            'first_name', 'last_name', 'document', 'email', 'phone','address',
            'name_city', 'name_state', 'uf'
        ])

        try:

            # Address_state 
            name_state = payload['name_state']
            uf = payload['uf']
            state = Address_State(name_state, uf)

            # Address_city 
            name_city = payload['name_city']
            city = Address_City(name_city, state)

            # Buyer
            first_name = payload['first_name']
            last_name = payload['last_name']
            document = payload['document']
            email = payload['email']
            phone = payload['phone']
            address = payload['address']

            buyer = Buyer(first_name=first_name, last_name=last_name, 
                document=document, email=email, address=address, 
                phone=phone, address_city=city 
            )

            db.session.add(buyer)
            db.session.commit()

            return marshal(buyer, buyer_field, 'buyer'), 201
        
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500