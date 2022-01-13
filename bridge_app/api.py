from flask import (
    Blueprint, request
)


bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/')
def index():
    return {'message': 'API sanity check successful'}