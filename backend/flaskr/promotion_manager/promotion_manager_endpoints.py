from flask import Blueprint, jsonify, request
from ..models import db, PromotionManager, get_column_names
promotion_manager = Blueprint('promotion_manager', __name__)

@promotion_manager.route('/test')
def my_first_blueprint():
    return jsonify({'succes':'blueprint success'})

@promotion_manager.route('/promotion_manager', methods = ['POST'])
def create_promotion_manager():
    id = request.get_json().get('id')
    first_name = request.get_json().get('first_name')
    last_name = request.get_json().get('last_name')
    phone_number = request.get_json().get('phone_number')
    new_promotion_manager = PromotionManager(id,first_name, last_name, phone_number)
    new_promotion_manager.insert()
    return jsonify(new_promotion_manager.format())

@promotion_manager.route('/promotion_managers',methods = ['GET'])
def get_promotion_managers():
    pmanagers= [pmanager.format() for pmanager in db.session.query(PromotionManager).all()]
    return jsonify(pmanagers)
    
