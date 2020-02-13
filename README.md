# Face Detection and Features recognition  using DLib


Dlib is a modern C++ toolkit containing machine learning algorithms and tools for creating complex software in C++ to solve real-world problems. This library works only on the gray-scale image.

## Overview
We detect faces(multiple faces allowed) in the image with the help of the OpenCV bounding box and display the face count near the box.
We display the facial landmark coordinates and  mark  the facial landmark points, such as eyes, nose, mouth, ears, jaw-line with dots and trace the dots of jawline curve using the popular Dlib library
![alt text](https://github.com/vishakhagupta10/feature_detection/blob/master/facelandmark68.png)

## Steps to Set-Up

 1. Clone this repository.
 2. Enter into the directory

 ```
 cd Facial-landmark-Detection
 ```
 3. Install requirements using the following command
 ```
 pip install -r requirements.txt
 ```
 4. Run the image.py file for processing the image 
 ```
 python image.py
 ```
 5. Before running image.py update the name of your image file as face.jpeg which needs to be processed.

 6. Image with landmark points will be saved in the results folder.




## Result
Coordinates of respective landmark points
![alt text](https://github.com/vishakhagupta10/feature_detection/blob/master/Screenshot_result.png)


Image for detection
![alt text](https://github.com/vishakhagupta10/feature_detection/blob/master/face.jpeg)



Image after detection
![alt text](https://github.com/vishakhagupta10/feature_detection/blob/master/results/face.jpeg)





