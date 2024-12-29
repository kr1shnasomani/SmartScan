<h1 align="center">SmartScan</h1>
This code detects and decodes QR codes from an image, drawing rectangles around detected QR codes and extracting their data using OpenCV for image processing and pyzbar for QR code decoding. Results are displayed using Matplotlib.

## Execution Guide:
1. Run the following command line in the terminal:
   ```
   pip install opencv-python pyzbar matplotlib
   ```

2. From [Visual C++ Redistributable Packages for Visual Studio 2013](https://www.microsoft.com/en-US/download/details.aspx?id=40784) install the appropriate version:

   a. 64-bit Python: `vcredist_x64.exe`

   b. 32-bit Python: `vcredist_x86.exe`

3. Enter the path of the image which contains the QR code

4. Upon running the code it detects the QR code from the image and outputs the link present in the QR code

## Model Prediction:

  Input Image:
  
  ![image](https://github.com/user-attachments/assets/9316032a-e628-49d0-b373-5d6210203ca1)

  Detected Link:
  
  `QR Code: https://www.qrfy.com/Zgke4d3HDI`

## Overview:
This code defines a `QRCodeDetector` class that detects and processes QR codes from an image. It uses the `cv2` (OpenCV) library for image processing, `pyzbar` for decoding QR codes, and `matplotlib` for displaying the results. Here's an overview of the key components and their functions:

1. **Imports**
   - `cv2`: OpenCV library for image manipulation and computer vision tasks.
   - `numpy`: For numerical operations (used for handling points and arrays).
   - `pyzbar.pyzbar`: For QR code detection and decoding.
   - `matplotlib.pyplot`: For displaying images in a graphical format.

2. **QRCodeDetector Class**
   - **`detect_qr_codes(self, image)`**: This method takes an image, converts it to grayscale, and uses the `decode` function from `pyzbar` to detect QR codes. It returns a list of QR code objects.
   - **`extract_qr_data(self, qr_codes)`**: This method takes the list of detected QR codes and extracts the data (decoded text) from each QR code. It prints the QR code data in the console.
   - **`draw_qr_code_rectangles(self, image, qr_codes)`**: This method draws rectangles around the detected QR codes on the image. If the QR code is not a simple polygon, it computes the convex hull (to handle complex shapes) and draws the shape using OpenCV’s `polylines` function.
   - **`run(self, image_path)`**: This method takes the path of the image file, loads it, and then calls the previous methods to:
     - Detect QR codes.
     - Extract and print the QR code data.
     - Draw rectangles around the detected QR codes.
     - Display the processed image with QR codes highlighted using `matplotlib`.

3. **Main Block**
   - **Image Path**: The image file path is specified as `image_path`. This image is used as input to the `QRCodeDetector` class.
   - **Create an Instance**: An instance of `QRCodeDetector` is created, and the `run` method is called with the provided image path to start the QR code detection process.

### Execution Flow:
   1. The image is read from the specified path.
   2. QR codes are detected and decoded from the image.
   3. The extracted data from the QR codes is printed.
   4. Rectangles are drawn around the detected QR codes.
   5. The processed image (with rectangles) is displayed.
