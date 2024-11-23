# Use the official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the Streamlit application
CMD ["streamlit", "run", "Talk_to_Coffliza.py", "--server.port=8501", "--server.enableCORS=false"]
