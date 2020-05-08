import time

from flask import Flask, jsonify

from car.car import Car
from service.image_analysis import ImageAnalysisService


class CarController:
    def __init__(self, car: Car, image_analysis_service: ImageAnalysisService, flask_app: Flask):
        self._car = car
        self._imageAnalysisService = image_analysis_service
        self._flaskApp = flask_app
        self._flaskApp.route("/status", methods=['GET'])(self.status)

    def status(self):
        return jsonify(status=str(self._car.status.name))

    def run(self):
        for i in range(5):
            self._car.move_forward()
            self._car.stop()
            self._car.take_picture('img_' + str(i) + '.png')
            time.sleep(1)
