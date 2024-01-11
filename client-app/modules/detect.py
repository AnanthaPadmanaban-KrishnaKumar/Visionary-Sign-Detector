"""
we will be hosting the traffic sign detector model
on the localhost:5001 using the flask service
"""


"""
Importing all necessary librarirs
"""
import numpy as np
import re
import requests
import cv2
import json
import google.generativeai as genai

from google.api_core.exceptions import InternalServerError
from PIL import Image
from modules import config

"""
configure the genAI API key
refere google gemini API docs on how to generate API key
"""
genai.configure(api_key=config.GOOGLE_API_KEY)

"""
Experiment with prompt engineering to get optimal results.
For demonstration we have constructed a sample prompt for the use case.
"""
prompt = config.prompt

"""
loading the geminiAI vision model
You need to configure the API key in order to access this model.
As of now the model allows 60 request per minute free of cost.
"""
vision_model = genai.GenerativeModel('gemini-pro-vision')
if vision_model != None:
    print("Vision Model Loaded ... ")
else:
    print("Vision Model failed to load!!!")


"""
The gemini-pro-vision return results that may consist of special characters
which is not relevant to our usecase.
Use this function to Remove non-ASCII characters, including emojis.
"""
def sanitize_text(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)


"""
We will send the input images in batches
to the YOLO model. Ultralytics YOLO supports
batch processing which can speed up the infrence speed. 
"""
def send_batch(url, batch):
    files = [('images', (image_path.name, open(image_path, 'rb'), 'image/jpeg')) for image_path in batch]
    response = requests.post(url, files=files)
    for _, file in files:
        file[1].close()
    return response

"""
cropping out each bounding box and sending
it through the gemini vision model and 
extracting the meaning, symbols, texts from it.
"""
def process_bounding_boxes(image_path, bounding_boxes):
    image = Image.open(image_path)
    np_image = np.array(image)
    np_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)
    final_image = np_image.copy()
    for box in bounding_boxes:
        x1, y1, x2, y2 = box
        bbox_image = np_image[y1:y2, x1:x2]
        if not bbox_image is None and bbox_image.any():
                try:
                    pil_bbox_image = Image.fromarray(bbox_image)
                    response = vision_model.generate_content([prompt,pil_bbox_image])
                    response.resolve()
                    json_str = response.text[response.text.find('{'):response.text.rfind('}')+1]

                    try:
                        response_data = json.loads(json_str)  
                        detected_text = sanitize_text(response_data.get("text", ""))
                        #detected_action = sanitize_text(response_data.get("action", ""))
                    except json.JSONDecodeError:
                        print("Failed to parse JSON from response.")
                    cv2.putText(final_image, detected_text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                except InternalServerError as e:
                    print("An internal server error occurred. Continuing with the next image.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
        cv2.rectangle(final_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return final_image