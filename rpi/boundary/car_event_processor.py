from socket import SocketIO

from pydispatch import dispatcher

from car.car_status import CarStatus


class CarEventProcessor:
    def __init__(self, socket_io: SocketIO):
        self._socketIO: SocketIO = socket_io

        dispatcher.connect(self.running, signal=CarStatus.RUNNING, sender=dispatcher.Any)

        dispatcher.connect(self.stopped, signal=CarStatus.STOPPED, sender=dispatcher.Any)

        dispatcher.connect(self.take_picture, signal=CarStatus.TAKE_PICTURE, sender=dispatcher.Any)

        dispatcher.connect(self.uploading_image, signal=CarStatus.UPLOADING_IMAGE, sender=dispatcher.Any)

        dispatcher.connect(self.image_uploaded, signal=CarStatus.IMAGE_UPLOADED, sender=dispatcher.Any)

        dispatcher.connect(self.analyse_image, signal=CarStatus.ANALYSE_IMAGE, sender=dispatcher.Any)

        dispatcher.connect(self.traffic_light_detected, signal=CarStatus.TRAFFIC_LIGHT_DETECTED, sender=dispatcher.Any)

        dispatcher.connect(self.traffic_light_not_present, signal=CarStatus.TRAFFIC_LIGHT_NOT_PRESENT, sender=dispatcher.Any)

        dispatcher.connect(self.move_forward, signal=CarStatus.MOVE_FORWARD, sender=dispatcher.Any)

    def take_picture(self):
        self._socketIO.emit('take_picture', broadcast=True, namespace="/test")

    def uploading_image(self):
        self._socketIO.emit('uploading_image', broadcast=True, namespace='/test')

    def traffic_light_detected(self):
        self._socketIO.emit('traffic_detected', broadcast=True, namespace='/test')

    def traffic_light_not_present(self):
        self._socketIO.emit('traffic_not_detected', broadcast=True, namespace='/test')

    def move_forward(self):
        self._socketIO.emit('moving_forward', broadcast=True, namespace='/test')

    def running(self):
        self._socketIO.emit('running', broadcast=True, namespace='/test')

    def stopped(self):
        self._socketIO.emit('stopped', broadcast=True, namespace='/test')

    def image_uploaded(self):
        self._socketIO.emit('image_uploaded', broadcast=True, namespace='/test')

    def analyse_image(self):
        self._socketIO.emit('analyse_image', broadcast=True, namespace='/test')
