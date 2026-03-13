# ML Project with MLflow and Docker

This is a simple machine learning project using scikit-learn, MLflow for experiment tracking, Flask for serving the model, and Docker for containerization.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Train the model:
   ```bash
   python train.py
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

## Docker

Build the Docker image:
```bash
docker build -t ml-app .
```

Run the container:
```bash
docker run -p 5000:5000 ml-app
```

## Deployment on Railway

1. Push this code to a GitHub repository.
2. Connect the repository to Railway.app.
3. Railway will automatically detect the Dockerfile and deploy the app.
4. The app will be available at the Railway-provided URL.

## API Usage

Send a POST request to `/predict` with JSON:
```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

Response:
```json
{
  "prediction": 0
}
```