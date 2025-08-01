from flask import Blueprint, request, jsonify
from .models import Item
from . import db

crud_bp = Blueprint('crud', __name__)

@crud_bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': i.id, 'name': i.name, 'description': i.description} for i in items])

@crud_bp.route('/items', methods=['POST'])
def create_item():
    data = request.json
    item = Item(name=data['name'], description=data.get('description', ''))
    db.session.add(item)
    db.session.commit()
    return jsonify({'id': item.id}), 201

@crud_bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.json
    item.name = data['name']
    item.description = data.get('description', '')
    db.session.commit()
    return jsonify({'message': 'Updated'})

@crud_bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Deleted'})
