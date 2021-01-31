from flask import Blueprint, jsonify
promotion_manager = Blueprint('promotion_manager', __name__)

@promotion_manager.route('/test')
def my_first_blueprint():
    return jsonify({'succes':'blueprint success'})