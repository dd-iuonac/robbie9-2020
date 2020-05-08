from time import sleep


class ImageAnalysisService:

    def upload_image(self, image_filename: str):
        print(f"Uploading {image_filename} ...")
        sleep(0.25)

    def detect_traffic_light(self, image_filename: str) -> bool:
        print(f"Detecting traffic light in {image_filename} ...")
        sleep(0.25)
        return False
