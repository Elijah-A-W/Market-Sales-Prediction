from flask import Blueprint,request,jsonify

api=Blueprint('api',__name__)


@api.route('/')
def index():
    return jsonify({"message":"Hello API"})