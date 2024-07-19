FROM ubuntu:latest
LABEL authors="sean"

ENTRYPOINT ["top", "-b"]

# Use the official Python image from the Docker Hub
FROM python:3.12-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container (optional)
EXPOSE 8000

# Run the application
CMD ["python"]
#, "your_script.py"]
