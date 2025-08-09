# Use an official Python runtime as a parent image
# python:3.10-slim is a great choice for smaller, production-ready images
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make sure to update your requirements.txt to only include production dependencies
# For example, you can remove matplotlib and seaborn if they're only for notebooks.

# Copy the entire app directory from your host to /app in the container
COPY ./app /app

# Copy the saved_models directory to the container
COPY ./saved_models /app/saved_models

# Expose the port the app runs on
EXPOSE 8000

# Run the app with Gunicorn, a production-ready WSGI server
# The command tells Gunicorn to run the app in `app/main.py`
# The --bind 0.0.0.0:8000 makes the app accessible on port 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]