# visionary_sign_detector

## Introduction
In this project, we leveraged the comprehensive Cityscapes Dataset to focus on a crucial aspect of autonomous driving systems - traffic sign recognition and interpretation. Our objective was to develop a system that not only accurately identifies traffic signs in urban scenes but also provides a clear understanding of their meaning, which is essential for any effective Autonomous Driving Assistant System (ADAS).

## Core Components
- **Ultralytics YOLOv8 Segmentation Model**: At the heart of our project, we utilized the Ultralytics YOLOv8 segmentation model. This state-of-the-art model is specifically fine-tuned for the precise identification and extraction of traffic signs from varied urban scenes within the Cityscapes Dataset.
- **Traffic Sign Segmentation and Extraction**: Our custom-developed module uses the YOLOv8 model to accurately detect traffic signs. Once detected, the module segments and extracts just the traffic sign from the frame, ensuring that the focus is solely on the sign for subsequent analysis.
- **Gemini AI Pro Vision Model Integration**: Post-segmentation, the extracted traffic sign images are fed into the Gemini AI Pro Vision Model. This advanced model excels in interpreting and understanding the traffic signs, providing detailed descriptions that are crucial for informed decision-making in ADAS.


## Data Source
The [Cityscapes Dataset](https://www.cityscapes-dataset.com) is an extensive collection designed for advancing semantic urban scene understanding, primarily in the context of autonomous driving. This dataset features a comprehensive set of stereo video sequences, meticulously recorded in urban street scenes across 50 different cities. A standout aspect of the Cityscapes Dataset is its high-quality pixel-level annotations for 5,000 frames, complemented by coarser annotations for an additional 20,000 frames. These annotations encompass a wide range of urban scenarios, captured under various seasonal, weather, and lighting conditions.

This dataset serves as a benchmark in the field of computer vision, offering an essential tool for tasks such as semantic segmentation, object detection, and instance-level segmentation. Its rich annotations cover numerous classes, including roads, sidewalks, vehicles, and pedestrians, among others. The Cityscapes Dataset's detailed and diverse data make it an invaluable asset for researchers and practitioners looking to train and evaluate computer vision models on complex, real-world urban scenes.

## Major Achievements
- **Exceptional Accuracy in Traffic Sign Segmentation**: The precision of the YOLOv8 model, coupled with its tailored adaptation for traffic sign segmentation, has resulted in exceptional accuracy. This is especially crucial in the complex and varied environments typical of urban settings. Our model's ability to discern and accurately interpret traffic signs greatly enhances the reliability of the ADAS in navigating safely through these challenging scenarios.
- **Innovative Interpretation of Traffic Signs**: Integrating the Gemini AI Pro Vision Model has brought a new dimension to our project. This model's ability to not only detect but also understand and describe traffic signs adds an invaluable layer of intelligence to the ADAS. This feature goes beyond mere detection, offering a nuanced interpretation essential for sophisticated decision-making in autonomous driving.
- **Seamless Integration with ADAS**: Achieving real-time processing and interpretation capability has been a crucial goal and success of this project. The seamless integration of our traffic sign detection and interpretation system with ADAS ensures that autonomous vehicles are equipped with up-to-the-moment, accurate information about road signs. This capability is fundamental to the safety and efficiency of autonomous vehicles, enabling them to make informed decisions instantaneously.
