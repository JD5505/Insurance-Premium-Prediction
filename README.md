# 🏥 Insurance Premium Prediction API

A machine learning-powered REST API that predicts insurance premium categories based on user profile inputs. Built with FastAPI and served via Docker.

---

## 🚀 Demo

> Hit the `/docs` endpoint after running to get the interactive Swagger UI — no Postman needed.

---

## 📌 Problem Statement

Predicting insurance premium tiers manually is slow and inconsistent. This API automates that classification using a trained ML model, taking key user attributes as input and returning a predicted premium category instantly.

---

## 🧠 Tech Stack

| Layer | Tool |
|---|---|
| API Framework | FastAPI |
| ML Model | scikit-learn (v1.8.0) |
| Data Handling | Pandas, NumPy |
| Serialization | Joblib |
| Containerization | Docker |
| Server | Uvicorn |

---

## 📂 Project Structure

```
Insurance-Premium-Prediction/
├── app.py                  # FastAPI app & route definitions
├── Dockerfile              # Container setup
├── requirements.txt        # Python dependencies
├── Model/
│   ├── predict.py          # Model loading & inference logic
│   └── model.pkl           # Trained ML model (see note below)
└── schema/
    ├── user_input.py       # Input schema (Pydantic)
    └── user_output.py      # Output schema (Pydantic)
```

---

## ⚙️ Installation & Usage

### Option 1 — Run Locally

```bash
# Clone the repository
git clone https://github.com/JD5505/Insurance-Premium-Prediction.git
cd Insurance-Premium-Prediction

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app:app --reload
```

API will be live at: `http://127.0.0.1:8000`

---

### Option 2 — Run with Docker

```bash
# Build the image
docker build -t insurance-api .

# Run the container
docker run -p 8000:8000 insurance-api
```

API will be live at: `http://localhost:8000`

---

## 📡 API Endpoints

### `GET /`
Returns a welcome message.

### `GET /health`
Returns API health status, model version, and whether the model is loaded.

**Response:**
```json
{
  "status": "OK",
  "version": "1.0.0",
  "Port": "http://127.0.0.1:8000",
  "model loaded": true
}
```

### `POST /predict`
Predicts the insurance premium category.

**Request Body:**
```json
{
  "bmi": 24.5,
  "age_group": "adult",
  "lifestyle_risk": "low",
  "city_tier": 1,
  "income_lpa": 8.5,
  "occupation": "salaried"
}
```

**Response:**
```json
{
  "Predicted_category": "Medium"
}
```

---

## 📝 Notes

- Interactive API docs available at `http://localhost:8000/docs` (Swagger UI)

---

## 🙋 Author

**Your Name**
[LinkedIn](https://linkedin.com/in/jivan-divate-56032b292) • [GitHub](https://github.com/JD5505)
