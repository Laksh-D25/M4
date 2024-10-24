import cv2
from fer import FER

def main():
    # Initialize the emotion detector
    detector = FER()

    # Start video capture
    video_capture = cv2.VideoCapture(0)  # Use 0 for the default camera

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Detect emotions
        emotions = detector.detect_emotions(frame)

        if emotions:
            # Get the dominant emotion
            dominant_emotion = emotions[0]["emotions"]
            emotion_label = max(dominant_emotion, key=dominant_emotion.get)
            confidence = dominant_emotion[emotion_label]

            # Display the dominant emotion and its confidence
            cv2.putText(frame, f'Emotion: {emotion_label}, Confidence: {confidence:.2f}', 
                        (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
