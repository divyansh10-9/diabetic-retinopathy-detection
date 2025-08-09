# 🩺 APTOS 2019 Blindness Detection: End-to-End Deep Learning Project

## 📜 Overview
This project is an **end-to-end deep learning application** for the [APTOS 2019 Blindness Detection](https://www.kaggle.com/competitions/aptos2019-blindness-detection) competition.  
It leverages a **VGG16-based** deep learning model, a **Flask** web API, and **Docker** for containerization, enabling **real-time diabetic retinopathy diagnosis** from retinal images.

The project follows **modern MLOps best practices**, ensuring that it is **reproducible**, **portable**, and **easy to deploy**.

---

## ✨ Key Features
- **Real-Time Inference** — Diagnose diabetic retinopathy from uploaded retinal images instantly.
- **Web-Based Interface** — Simple and intuitive UI for image uploads and predictions.
- **Deep Learning Model** — Pre-trained **VGG16** with custom top layers for high accuracy.
- **Dockerized Deployment** — Consistent environment across development and production.
- **Reproducible Workflow** — Fully documented with all necessary files to rebuild from scratch.

---

## 📁 Project Structure
```plaintext
.
├── app/                      # Flask web application
│   ├── main.py               # Backend API
│   ├── templates/            # HTML templates
│   └── static/               # CSS, JS, and static assets
├── saved_models/             # Trained deep learning model
│   └── final_model_for_deployment.keras
├── notebooks/                # Jupyter notebooks for experimentation
│   └── model_comparison.ipynb
├── .gitignore                 # Git ignore file
├── Dockerfile                 # Docker build instructions
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

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
