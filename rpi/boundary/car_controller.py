from flask import Flask, jsonify

from car.car import Car
from service.car_service import CarService


class CarController:
    def __init__(self, car: Car, car_service: CarService, flask_app: Flask):
        self._car = car
        self._carService = car_service
        self._flaskApp = flask_app
        self._flaskApp.route("/status", methods=['GET'])(self.status)
        self._flaskApp.route("/run", methods=['PUT'])(self.run)
        self._flaskApp.route("/stop", methods=['POST'])(self.stop)

    def status(self):
        return jsonify(status=str(self._car.status.name))

    def run(self):
        self._carService.run()
        return self.status()

    def stop(self):
        self._carService.stop()
        return self.status()
