# Visionary-Sign-Detector
![U-Net Architecture with VGG Backbone](https://github.com/AnanthaPadmanaban-KrishnaKumar/Visionary-Sign-Detector/blob/main/asset/processed_video.gif)
## Introduction
In this project, we leveraged the comprehensive Cityscapes Dataset to focus on a crucial aspect of autonomous driving systems - traffic sign recognition and interpretation. Our objective was to develop a system that not only accurately identifies traffic signs in urban scenes but also provides a clear understanding of their meaning, which is essential for any effective Autonomous Driving Assistant System (ADAS).

## Core Components
- **Ultralytics YOLOv8 Segmentation Model**: At the heart of our project, we utilized the Ultralytics YOLOv8 segmentation model. This state-of-the-art model is specifically fine-tuned for the precise identification and extraction of traffic signs from varied urban scenes within the Cityscapes Dataset.
- **Traffic Sign Segmentation and Extraction**: Our custom-developed module uses the YOLOv8 model to accurately detect traffic signs. Once detected, the module segments and extracts just the traffic sign from the frame, ensuring that the focus is solely on the sign for subsequent analysis.
- **Gemini AI Pro Vision Model Integration**: Post-segmentation, the extracted traffic sign images are fed into the Gemini AI Pro Vision Model. This advanced model excels in interpreting and understanding the traffic signs, providing detailed descriptions that are crucial for informed decision-making in ADAS.

## Data Source
The [Cityscapes Dataset](https://www.cityscapes-dataset.com) is an extensive collection designed for advancing semantic urban scene understanding, primarily in the context of autonomous driving. This dataset features a comprehensive set of stereo video sequences, meticulously recorded in urban street scenes across 50 different cities. A standout aspect of the Cityscapes Dataset is its high-quality pixel-level annotations for 5,000 frames, complemented by coarser annotations for an additional 20,000 frames. These annotations encompass a wide range of urban scenarios, captured under various seasonal, weather, and lighting conditions.

This dataset serves as a benchmark in the field of computer vision, offering an essential tool for tasks such as semantic segmentation, object detection, and instance-level segmentation. Its rich annotations cover numerous classes, including roads, sidewalks, vehicles, and pedestrians, among others. The Cityscapes Dataset's detailed and diverse data make it an invaluable asset for researchers and practitioners looking to train and evaluate computer vision models on complex, real-world urban scenes.

## Ultralytics Segmentation Model 
The Ultralytics segmentation model, particularly the YOLOv8 variant used in our project, is a cutting-edge tool in the field of computer vision and object detection. It's renowned for its speed, accuracy, and efficiency, making it ideal for real-time applications. YOLOv8's architecture is designed to perform complex segmentation tasks with remarkable precision, which is essential for differentiating and isolating specific objects in varied environments.

## Role of Ultralytics YOLOv8 in Our Project
In our traffic sign recognition project, the Ultralytics YOLOv8 segmentation model plays a pivotal role:

- **Highly Accurate Traffic Sign Detection**: YOLOv8's sophisticated algorithm allows for the precise detection of traffic signs, even in challenging urban settings. Its ability to discern signs from complex backgrounds is critical for the initial stage of our project.
- **Efficient Segmentation and Extraction**: After detection, YOLOv8 efficiently segments and extracts the traffic sign from the rest of the image. This segmentation is crucial, as it ensures that only the relevant part of the image (the traffic sign) is processed in subsequent stages, thereby optimizing the workflow.
- **Real-Time Processing Capabilities**: One of YOLOv8's standout features is its ability to process images in real time. This is essential for our project, as ADAS requires immediate information to make driving decisions. The speed of YOLOv8 ensures no lag between detection, segmentation, and interpretation.
- **Adaptability and Robustness**: The model's robustness and adaptability are key in handling the diverse range of visual inputs typical in urban settings. Whether it's varying lighting conditions, occlusions, or different sign designs, YOLOv8 maintains consistent performance.
- **Seamless Integration with Interpretive Models**: YOLOv8's output seamlessly integrates with the Gemini AI Pro Vision Model for interpretation. This compatibility is crucial for creating a cohesive system where detection, segmentation, and interpretation work in harmony.

In essence, the Ultralytics YOLOv8 model is the foundation of our traffic sign recognition system. Its role in accurately detecting and segmenting traffic signs in real time is indispensable, setting the stage for the advanced interpretative analysis performed by Gemini AI, and ultimately contributing to the overall efficacy of the ADAS.

## Gemini AI 
Gemini AI represents a breakthrough in the field of artificial intelligence, especially in the realm of image understanding and interpretation. It is an advanced deep learning model known for its exceptional capability to not just recognize objects within an image, but also to interpret and describe them in a contextually meaningful way.

## Role of Gemini AI in Our Project
In our project, Gemini AI plays an integral and transformative role. Once the traffic signs are detected and segmented by the YOLOv8 model, the extracted images of these signs are fed into the Gemini AI Pro Vision Model. Here's how Gemini AI contributes significantly to our project:

- **Deep Interpretation of Traffic Signs**: Unlike conventional models that stop at detection, Gemini AI delves deeper, providing detailed descriptions and interpretations of the traffic signs. This includes understanding the sign's meaning, which is essential for an autonomous vehicle's decision-making process.
- **Enhanced Decision-Making for ADAS**: The nuanced interpretations provided by Gemini AI are crucial for the ADAS. They enable the system to understand and react to traffic signs in a way that mimics human understanding, leading to safer and more effective navigation decisions.
- **Adaptability to Diverse Scenarios**: Gemini AI's sophisticated algorithm is adept at handling the variability and complexity of real-world traffic scenarios. Whether it's deciphering worn-out signs or interpreting signs in different weather conditions, Gemini AI ensures consistent performance.

In summary, Gemini AI elevates our project from mere detection to intelligent interpretation, making it a cornerstone of our advanced ADAS. Its ability to process and understand traffic signs in real time and in complex environments significantly enhances the overall safety and effectiveness of autonomous driving systems.

## Why the combination of YOLOv8 and Gemini AI??
- **Focused Interpretation**: Gemini AI excels in general image interpretation but lacked the ability to focus on specific regions like traffic signs.
- **Precise Segmentation**: YOLOv8 is renowned for its precise object detection and segmentation, filling the gap in Gemini AI's capabilities.
- **Combination Benefits**: The integration directs Gemini AI's interpretive power to precisely the segmented traffic signs by YOLOv8.
- **Enhanced Accuracy**: This synergy results in detailed and contextually accurate interpretations of traffic signs.
- **Improved Decision-Making**: The combination enhances the decision-making process in our Autonomous Driving Assistant System (ADAS).

Sample Input:
![U-Net Architecture with VGG Backbone](https://github.com/AnanthaPadmanaban-KrishnaKumar/Visionary-Sign-Detector/blob/main/asset/frame_26.jpg)
Sample Final Result:
![U-Net Architecture with VGG Backbone](https://github.com/AnanthaPadmanaban-KrishnaKumar/Visionary-Sign-Detector/blob/main/asset/frame_26_batch_2_0.jpg)

## Major Achievements
- **Exceptional Accuracy in Traffic Sign Segmentation**: The precision of the YOLOv8 model, coupled with its tailored adaptation for traffic sign segmentation, has resulted in exceptional accuracy. This is especially crucial in the complex and varied environments typical of urban settings. Our model's ability to discern and accurately interpret traffic signs greatly enhances the reliability of the ADAS in navigating safely through these challenging scenarios.
- **Innovative Interpretation of Traffic Signs**: Integrating the Gemini AI Pro Vision Model has brought a new dimension to our project. This model's ability to not only detect but also understand and describe traffic signs adds an invaluable layer of intelligence to the ADAS. This feature goes beyond mere detection, offering a nuanced interpretation essential for sophisticated decision-making in autonomous driving.
- **Seamless Integration with ADAS**: Achieving real-time processing and interpretation capability has been a crucial goal and success of this project. The seamless integration of our traffic sign detection and interpretation system with ADAS ensures that autonomous vehicles are equipped with up-to-the-moment, accurate information about road signs. This capability is fundamental to the safety and efficiency of autonomous vehicles, enabling them to make informed decisions instantaneously.

## Drawback
One of the main drawbacks of our current project is the significant amount of time taken by the Gemini AI Large Language Model (LLM) for processing and interpretation. This delay poses a challenge to the real-time applicability of our system in autonomous driving scenarios. Since timely decision-making is critical in ADAS, any lag, particularly in the interpretation phase, can potentially impact the safety and effectiveness of autonomous vehicles.

## Future Directions
As we advance our project to improve the efficiency and real-time applicability of our system for autonomous driving scenarios, we are integrating a strategic Natural Language Processing (NLP) component along with our ongoing efforts in Model Simplification and Hybrid Model Development. This integration aims to address the processing time challenges of the Gemini AI model. Our two-pronged approach now includes:

### Hybrid Model Development
We are concurrently developing a hybrid model that leverages the strengths of both rule-based systems and AI, including:

- **Utilizing Rule-Based Systems**: Implementing rule-based algorithms for the immediate recognition of standard and clear-cut traffic signs.
- **Leveraging AI for Complexity**: Reserving the AI component for more complex or ambiguous signs that require deeper understanding.

### NLP-Enhanced Semantic Interpretation
Integrating NLP to enhance the interpretative capabilities of our system, focusing on:

- **Semantic Analysis of Traffic Signs**: Using NLP to analyze and understand the textual information on traffic signs. This will allow the system to comprehend messages and instructions on signs, like speed limits or cautionary advice, which are crucial for safe navigation.
- **Synergistic Integration with AI and Rule-Based Systems**: The NLP component will work in tandem with both the AI and rule-based elements of our hybrid model. For signs with textual content, NLP will provide quick semantic understanding, while the AI component will handle complex interpretations that require contextual analysis.

By incorporating these two approaches – Hybrid Model Development, and NLP-Enhanced Semantic Interpretation – we aim to significantly reduce the inference time of our system. This integration is expected to not only improve the real-time functionality of our ADAS but also establish new standards for efficiency and reliability in traffic sign interpretation within the autonomous driving industry.

## Running the Project

1. run git clone https://github.com/akash6murali/visionary-sign-detector.git in your terminal.
2. once clone is complete you should see a directory by the name visionary-sign-detector.
3. cd server-app
4. inside this directory you will build a container with command: docker build --no-cache -t model-service -f Dockerfile .
The above step will build the container by exposing port 5001 to the localhost.
we build a docker network for the server and the client to communicate with each other with the command: docker network create road_signboard_network
we attach the model-service image to this container by mapping the localhost port 5001 with the docker container port 5001 with the command: docker run -d --name model-server --network road_signboard_network -p 5001:5001 model-service
with the above command executed you should see the moder-server attached to the network. Now cd client-app
sudo docker build --no-cache -t client-app -f Dockerfile .
finally we attach client app to the network so that the communication can happen between the two containers with the command: docker run -d --name client-app --network road_signboard_network \
-v /give/your/corresponding/images/in/this/directory:/input
-v /give/the/corresponding/directory/where/the/output/images/needs/to/be/stored:/output
client-app
if you were able to successfully execute all this commands you can see the output in the path mentioned in step 10.
ONE IMPORTANT STEP**: you need to generate your own API from here: API docs and place it in the config.py file in the client-app to access google's gemini vision model. Thank you for your interest in this project, and we look forward to your contributions to this repository.

## Conclusion:
In conclusion, our project marks a significant stride in enhancing Autonomous Driving Assistant Systems by synergistically combining the precision of Ultralytics YOLOv8 in traffic sign detection with the advanced interpretative capabilities of Gemini AI Pro Vision Model. This integration has led to a breakthrough in real-time, accurate traffic sign interpretation, crucial for safe and efficient autonomous navigation. By bridging the gap between detection and interpretation, our project sets a new benchmark in the realm of autonomous driving technology, paving the way for safer, more intelligent, and adaptable autonomous vehicles.
