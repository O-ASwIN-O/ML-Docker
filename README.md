# ML Docker Project

A complete machine learning project featuring model training with MLflow experiment tracking, Flask API for predictions, Docker containerization, and deployment on Railway.

## 🚀 Project Overview

- **ML Model:** Random Forest classifier trained on the Iris dataset
- **Experiment Tracking:** MLflow for logging parameters, metrics, and model artifacts
- **API:** Flask-based REST API serving predictions
- **Containerization:** Docker for easy deployment
- **Deployment:** Ready for Railway.app

## 📋 Features

- Automated model training during Docker build
- RESTful API endpoint for predictions
- MLflow UI for experiment visualization
- Production-ready container setup

## 🛠️ Local Development

### Prerequisites
- Python 3.12+
- Docker Desktop
- Git

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/O-ASwIN-O/ML-Docker.git
   cd ML-Docker
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model:**
   ```bash
   python train.py
   ```

4. **Run the Flask app:**
   ```bash
   python app.py
   ```

## 🐳 Docker Usage

### Build the image:
```bash
docker build -t ml-app .
```

### Run the container:
```bash
docker run -p 5000:5000 ml-app
```

### Test the API:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[5.1,3.5,1.4,0.2]}'
```

## 📊 MLflow Tracking

After training, view experiments:
```bash
mlflow ui
```
Access at: http://localhost:5000 (MLflow UI, not the API)

## 🚀 Deployment on Railway

1. **Connect Repository:**
   - Go to [Railway.app](https://railway.app)
   - Create new project → Deploy from GitHub
   - Select `O-ASwIN-O/ML-Docker`

2. **Auto-Deployment:**
   - Railway detects the Dockerfile
   - Builds and deploys automatically
   - Provides public URL

3. **Test Deployed API:**
   ```bash
   curl -X POST https://your-railway-url.up.railway.app/predict \
     -H "Content-Type: application/json" \
     -d '{"features":[5.1,3.5,1.4,0.2]}'
   ```

## 📡 API Documentation

### Endpoint: `POST /predict`

**Request Body:**
```json
{
  "features": [float, float, float, float]
}
```

**Response:**
```json
{
  "prediction": 0
}
```

**Iris Classes:**
- 0: Setosa
- 1: Versicolor
- 2: Virginica

**Example:**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[5.1,3.5,1.4,0.2]}'
# Returns: {"prediction": 0}
```

## 🏗️ Project Structure

```
ML-Docker/
├── train.py          # Model training script with MLflow
├── app.py            # Flask API server
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker build configuration
├── .dockerignore     # Docker ignore rules
├── .gitignore        # Git ignore rules
├── README.md         # This file
└── model.pkl         # Trained model (generated)
```

## 🔧 Technologies Used

- **Python 3.12**
- **scikit-learn** - Machine learning
- **MLflow** - Experiment tracking
- **Flask** - Web framework
- **Docker** - Containerization
- **Railway** - Cloud deployment

## 📈 Model Performance

- **Dataset:** Iris (150 samples, 4 features)
- **Algorithm:** Random Forest (100 estimators)
- **Accuracy:** 100% on test set
- **Features:** Sepal length, Sepal width, Petal length, Petal width

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and test
4. Submit a pull request

## 📄 License

This project is open source. Feel free to use and modify.