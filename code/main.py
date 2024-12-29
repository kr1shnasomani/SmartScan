# Import the required libraries
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt

class QRCodeDetector:
    def detect_qr_codes(self, image):
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Use pyzbar to decode QR codes
        qr_codes = decode(gray_image)
        return qr_codes

    def extract_qr_data(self, qr_codes):
        # Extract and print data from the detected QR codes
        if qr_codes:
            for qr_code in qr_codes:
                qr_data = qr_code.data.decode('utf-8')
                print("QR Code:", qr_data)

    def draw_qr_code_rectangles(self, image, qr_codes):
        # Draw rectangles around detected QR codes in the image
        if qr_codes:
            for qr_code in qr_codes:
                points = qr_code.polygon

                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    cv2.polylines(image, [hull], True, (255, 0, 255), 3) 
                else:
                    cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (255, 0, 255), 3)
        return image

    def run(self, image_path):
        # Load the image from the given path
        image = cv2.imread(image_path)
        
        # Check if the image was successfully loaded
        if image is None:
            print("Could not load the image. Please check the image path.")
            return

        # Detect QR codes in the image
        qr_codes = self.detect_qr_codes(image)
        
        # Extract and display QR code data
        self.extract_qr_data(qr_codes)
        
        # Draw rectangles around QR codes and display the processed image
        processed_image = self.draw_qr_code_rectangles(image, qr_codes)

        # Convert BGR to RGB for displaying using matplotlib
        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
        
        # Display the image with matplotlib
        plt.imshow(processed_image)
        plt.title("Detected QR Code")
        plt.axis('off') 
        plt.show()


if __name__ == "__main__":
    # Specify the image path
    image_path = r"C:\Users\krish\OneDrive\Desktop\image.jpg"  
    
    # Create an instance of the QRCodeDetector and run it
    qr_detector = QRCodeDetector()
    qr_detector.run(image_path)
