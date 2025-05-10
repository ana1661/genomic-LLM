# Use NVIDIA's official PyTorch image with GPU (CUDA 11.8, Python 3.10)
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime


# Set the working directory
WORKDIR /app

# Copy requirements.txt separately and install dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy everything else
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]


