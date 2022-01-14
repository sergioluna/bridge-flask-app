from flask import (
    Blueprint, request
)

from .models.email import ReservationEmail
from .models.reservation import Reservation


bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/')
def index():
    return {'message': 'API sanity check successful'}


@bp.route('/reservation', methods=['POST'])
def reservation():
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']

    reservation = Reservation(
        name,
        email,
        phone
    )
    
    email = ReservationEmail(reservation)
    email.send()

    success_msg = 'Reservation submitted!'
    error_msg = (
        'There was an issue with your reservation.'
        ' Please contact us by phone to set a reservation'
    )

    if email.response.status_code < 400:
        return {
            'status': email.response.status_code,
            'body': success_msg
        }
    else:
        return {
            'status': email.response.status_code,
            'body': error_msg
        }
