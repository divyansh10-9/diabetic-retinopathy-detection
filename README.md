APTOS 2019 Blindness Detection: An End-to-End Deep Learning Project


📜 Project Overview
This project is an end-to-end machine learning application for the APTOS 2019 Blindness Detection competition. It leverages a VGG16 deep learning model, a Flask-based web API, and Docker for containerization. The solution provides a real-time diagnosis of diabetic retinopathy from an uploaded retinal image.

The project is structured to follow modern MLOps best practices, ensuring that the application is reproducible, portable, and easy to deploy.

✨ Key Features
Real-time Inference: Diagnoses diabetic retinopathy in real-time from user-uploaded images.

Web-based Interface: A simple and intuitive web front-end for image uploads and predictions.

Deep Learning Model: Utilizes a pre-trained VGG16 model with a custom top layer for high-accuracy classification.

Containerized with Docker: The entire application is packaged into a Docker container, guaranteeing a consistent environment across development and production.

Reproducible Workflow: The repository includes all the necessary files to build the application from scratch.

📁 Project Structure
.
├── app/                      # The production-ready Flask web application
│   ├── main.py               # The core Flask backend API
│   ├── templates/            # HTML templates for the frontend
│   └── static/               # CSS, JS, and other static files
├── saved_models/             # Directory to store the trained deep learning model
│   └── final_model_for_deployment.keras
├── notebooks/                # Jupyter notebooks for model training and experimentation
│   └── model_comparison.ipynb
├── .gitignore                # Files and directories ignored by Git
├── Dockerfile                # Instructions for building the Docker image
├── requirements.txt          # Python dependencies for the application
└── README.md                 # Project README file (this file)
🚀 Setup and Installation
1. Clone the Repository
First, clone this repository to your local machine and navigate to the project directory.

Bash

git clone https://github.com/<your-username>/<your-repository-name>.git
cd <your-repository-name>
2. Acquire the Dataset (For Training Only)
The dataset and trained model are not included in this repository. To replicate the training process, you must download the APTOS 2019 Blindness Detection dataset from Kaggle and place the files inside a data/ directory in the project root.

3. Run the Application Locally with Docker
The easiest way to get the application running is by using Docker.

1. Build the Docker Image
The Dockerfile contains all the instructions to create a self-contained image of your application. Run the following command from the project's root directory:

Bash

docker build -t aptos-app .
This may take a few minutes as it downloads the base Python image and installs all dependencies.

2. Run the Docker Container
Once the image is built, run it as a container. This command maps the container's port 8000 to your local machine's port 8000.

Bash

docker run -p 8000:8000 aptos-app
3. Access the Application
Open your web browser and navigate to http://localhost:8000. You should see the web application running, ready for you to upload a retinal image for a diagnosis.
