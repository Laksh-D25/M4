from fer import FER
import base64
from PIL import Image
import cv2
import numpy as np

def detect_emotion(image_file):
    # Decode the image data from base64
    image_array = np.frombuffer(image_file.read(), np.uint8)
    processed_image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)  # Ensuring the image is read as a color image

    if processed_image is None:
        raise ValueError("Image could not be processed. Ensure it's in the correct format.")

    # Initialize the emotion detector
    detector = FER()
    emotions = detector.detect_emotions(processed_image)
    
    if emotions:
        dominant_emotion = emotions[0]["emotions"]
        return max(dominant_emotion, key=dominant_emotion.get)  # Return the dominant emotion
    return None
