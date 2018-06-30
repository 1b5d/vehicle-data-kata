from http import HTTPStatus

from flask import render_template, make_response, request
from flask_restful import Resource
from app.exceptions import VehicleDataError
from app.services.vehicle import HandlerService


class Home(Resource):
    """
    A resource for home URL.
    """
    def get(self):
        return make_response(render_template('home.html'))


class Vehicle(Resource):
    """
    A resource that represents vehicles.
    """
    def post(self, format):
        """
        handles post request to the vehicle resource.

        :param str format:
        :return:
        """
        data = request.get_data(as_text=True)
        try:
            handler = HandlerService.dispatch(format)
            result = list(handler.parse_iter(data))

        except VehicleDataError as e:
            return None, HTTPStatus.BAD_REQUEST, str(e)

        return result
