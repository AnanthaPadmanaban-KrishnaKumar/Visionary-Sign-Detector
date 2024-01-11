"""
We will be hosting the traffic sign detector model
on the localhost:5001 using the flask service.
"""


"""
Importing necessary libraries
"""
from flask import Flask, request, jsonify
from ultralytics import YOLO
from modules import config
from PIL import Image

"""
The application to host the model on localhost
"""
app = Flask(__name__)
#Loading the YOLO traffic sign detection model
model = YOLO(config.traffic_sign_detect_model_path)
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve list of images from the 'images' field
    images_files = request.files.getlist('images')
    # Check if at least one image was provided
    if not images_files:
        return jsonify({'error': 'No images provided'}), 400

    all_bounding_boxes = []
    
    # Process each image
    for image_file in images_files:
        try:
            # Convert the image file to a PIL Image
            image = Image.open(image_file.stream)

            # Run your model inference here
            # we have used Mac's inbuilt Metal Performance Shaders (MPS) backend for GPU inference acceleration
            results = model(image, device="mps", conf=0.5)[0]
            results = results.boxes.data.tolist()

            bounding_boxes = []
            for box in results:
                x1, y1, x2, y2, _, class_id = box
                bounding_boxes.append([int(x1), int(y1), int(x2), int(y2)])
            
            # Append the bounding boxes for each image to the all_bounding_boxes list
            all_bounding_boxes.append(bounding_boxes)

        except Exception as e:
            # Log exceptions or errors for this particular image and move on to the next
            print(f"Error processing one of the images: {str(e)}")
            all_bounding_boxes.append([])  # Append an empty list or some error indicator for this image

    return jsonify(all_bounding_boxes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5001)
