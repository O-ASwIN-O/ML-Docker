FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir scikit-learn mlflow flask pandas numpy joblib

COPY . .

# Train the model
RUN python train.py

EXPOSE 5000

CMD ["python", "app.py"]