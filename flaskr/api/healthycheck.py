from flask import Blueprint
from flask_restful import Api, Resource

healthy_check_bp = Blueprint('healthycheck', __name__)
api = Api(healthy_check_bp)

class HealthyCheck(Resource):
  def get(self):
    return ({
      'status': 'success'
    }, 200)

api.add_resource(HealthyCheck, '/healthycheck')