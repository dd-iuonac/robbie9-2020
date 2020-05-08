from flask import Flask, render_template

from car.car import Car
from boundary.car_controller import CarController
from service.image_analysis import ImageAnalysisService

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    car = Car(17, 18, 22, 23, 5, 6, 12, 13, 1920, 1080, 270)
    imageAnalysisService = ImageAnalysisService()
    carController = CarController(car=car, image_analysis_service=imageAnalysisService, flask_app=app)
    app.run()
