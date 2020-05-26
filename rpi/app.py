from flask_socketio import SocketIO
from flask import Flask, render_template

from boundary.car_controller import CarController
from boundary.car_event_processor import CarEventProcessor
from car.car import Car
from service.car_service import CarService
from service.image_analysis import ImageAnalysisService


app = Flask(__name__)
socketIO = SocketIO(app)


@app.route('/')
def index():
    return render_template("index.html")


@socketIO.on('connect', namespace='/test')
def test_connect():
    print('Client connected')


@socketIO.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    car = Car(17, 18, 22, 23, 5, 6, 12, 13, 1920, 1080, 270)
    imageAnalysisService = ImageAnalysisService()
    carService = CarService(car=car, image_analysis_service=imageAnalysisService, socket_io=socketIO)
    carController = CarController(car=car, car_service=carService, flask_app=app)
    car_event_processor = CarEventProcessor(socketIO)
    socketIO.run(app)
