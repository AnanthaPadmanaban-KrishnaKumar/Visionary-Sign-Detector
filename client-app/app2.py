"""
Importing necessary libraries
"""
import cv2
import os
from pathlib import Path
from modules import detect

"""
The main function to run on the client side
for inferring the models. HTTP requests are
sent to the model hosted on localhost:5001
using the container name model-server.
"""
def main():
    # sending the requests to the model server 
    url = 'http://model-server:5001/predict'
    images_directory = Path('/input')
    output_directory = '/output'
    images_paths = list(images_directory.glob('*.jpg'))

    if not images_paths:
        print("No images found in the directory.")
        return

    batch_size = 24
    for i in range(0, len(images_paths), batch_size):
        batch = images_paths[i:i + batch_size]
        response = detect.send_batch(url, batch)

        if response.ok:
            batch_results = response.json()
            for j, (image_path, bounding_boxes) in enumerate(zip(batch, batch_results)):
                final_image = detect.process_bounding_boxes(image_path, bounding_boxes)
                original_filename = os.path.basename(image_path)
                output_filename = f"{original_filename[:-4]}_batch_{i // batch_size}_{j}.jpg"
                output_filepath = os.path.join(output_directory, output_filename)
                cv2.imwrite(output_filepath, final_image)

        else:
            print('Error:', response.text)

if __name__ == "__main__":
    main()
