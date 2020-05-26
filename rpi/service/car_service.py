from pydispatch import dispatcher

from car.car import Car
from car.car_status import CarStatus
from service.image_analysis import ImageAnalysisService


class CarService:
    def __init__(self, socket_io, car: Car, image_analysis_service: ImageAnalysisService):
        self.socketIO = socket_io
        self.socketIO.on_event('start', self.run, namespace='/test')
        self.socketIO.on_event('stop', self.stop, namespace='/test')
        self._car = car
        self._imageAnalysisService = image_analysis_service
        self._running = True

    def run(self):
        self.socketIO.start_background_task(target=self._run)

    def _run(self):
        while self._running:
            image_taken = 'img.png'

            self._car.take_picture(image_taken)
            dispatcher.send(signal=CarStatus.TAKE_PICTURE, sender=dispatcher.Any)

            self._imageAnalysisService.upload_image(image_taken)
            dispatcher.send(signal=CarStatus.UPLOADING_IMAGE, sender=dispatcher.Any)

            if self._imageAnalysisService.detect_traffic_light(image_taken):
                dispatcher.send(signal=CarStatus.TRAFFIC_LIGHT_DETECTED, sender=dispatcher.Any)
            else:
                dispatcher.send(signal=CarStatus.TRAFFIC_LIGHT_NOT_PRESENT, sender=dispatcher.Any)

            self._car.move_forward()
            dispatcher.send(signal=CarStatus.MOVE_FORWARD, sender=dispatcher.Any)

            self.socketIO.sleep(1)

        self._car.stop()
        dispatcher.send(signal=CarStatus.STOPPED, sender=dispatcher.Any)

    def stop(self):
        self._running = False
