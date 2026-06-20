# Face Recognition Attendance System

## Overview

The Face Recognition Attendance System is an AI-powered application that automates attendance management using facial recognition technology. The system detects and recognizes registered users from a dataset of images and records attendance automatically, reducing manual effort and improving accuracy.

## Features

* Face detection using OpenCV
* Face recognition from stored image datasets
* Automatic attendance marking
* Real-time camera-based recognition
* Easy dataset management
* Fast and accurate identification
* User-friendly and scalable design

## Technologies Used

* Python
* OpenCV
* NumPy
* Git & GitHub

## Project Structure

```
face_attendance/
│
├── dataset/
│   └── chandu/
│       ├── img_5.jpg
│       ├── img_8.jpg
│       └── ...
│
├── face_detect.py
├── face_recognition.py
├── README.md
└── .gitignore
```

## How It Works

1. Store user images in the dataset folder.
2. The system reads and processes facial features.
3. A webcam captures live video frames.
4. Faces are detected and compared with the dataset.
5. When a match is found, attendance is automatically marked.

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd face_attendance
```

### Install Dependencies

```bash
pip install opencv-python numpy
```

### Run the Project

```bash
python face_recognition.py
```

## Applications

* Colleges and Universities
* Schools
* Offices and Organizations
* Training Institutes
* Workshops and Events

## Future Improvements

* Attendance database integration
* Web-based dashboard
* Multiple user recognition
* Cloud storage support
* Email and report generation
* Face mask detection support

## Learning Outcomes

Through this project, I gained practical experience in:

* Computer Vision
* Face Detection and Recognition
* Python Programming
* OpenCV
* Data Handling
* Git and GitHub Version Control

## Author

**Chandu Sai N**

B.Tech Computer Science and Engineering

Passionate about Artificial Intelligence, Computer Vision, Data Structures & Algorithms, and Software Development.
