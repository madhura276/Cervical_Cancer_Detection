# 🧠 Cervical Cancer Detection — AI-Powered Web Application

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?style=flat-square&logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5.2-orange?style=flat-square&logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-2.1.4-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 🔗 Live Demo
👉 **[https://cervical-cancer-detection-2c52.onrender.com](https://cervical-cancer-detection-2c52.onrender.com)**

> ⚠️ Hosted on Render free tier — first load may take 30–50 seconds to wake up.

---

## 📌 Project Overview

A **web-based AI application** that predicts the risk of cervical cancer using an ensemble of 5 machine learning models. Users enter medical and lifestyle details, and the system provides individual model predictions along with an overall risk assessment.

The goal of this project is to assist in **early detection and awareness** of cervical cancer using data-driven insights.

---

## 🚀 Features

- 🔐 User Authentication (Signup & Login)
- 🤖 5 Machine Learning Models running in parallel
- 📊 Real-time Prediction with Risk Assessment
- 📈 Prediction History Tracking per user
- 📅 User Activity Monitoring (login, clicks, logout)
- 📥 Downloadable Prediction Report (PDF)
- 🌐 Fully deployed and accessible online

---

## 🤖 Machine Learning Models & Accuracy

| Model | Accuracy |
|---|---|
| Logistic Regression | 94.61% |
| Decision Tree | 95.81% |
| Random Forest | 94.61% |
| Support Vector Machine (SVM) | 94.01% |
| XGBoost | 96.41% |

### ML Workflow
1. Data loading and preprocessing (`data.csv` — real-world cervical cancer dataset)
2. Handling missing values using `SimpleImputer` (mean strategy)
3. Feature selection — top 14 clinically relevant features
4. Train/test split (80/20)
5. Training 5 independent models
6. Real-time ensemble prediction on user input
7. Risk assessment based on combined model outputs

### Risk Assessment Logic
| Model Agreement | Result |
|---|---|
| All 5 predict safe | 100% Safe |
| 4 out of 5 predict safe | 80% Safe |
| 3 out of 5 predict safe | Hospital advice recommended |
| Less than 3 predict safe | Check hospital immediately |

---

## 🛠️ Tech Stack

### Backend
- Python 3.10
- Flask 3.1

### Machine Learning
- scikit-learn (Logistic Regression, Decision Tree, Random Forest, SVM)
- XGBoost
- Pandas, NumPy, SciPy

### Frontend
- HTML5, CSS3, JavaScript
- Chart.js (Prediction Visualization)

### Deployment
- Render (Free Tier)

---

## 📂 Project Structure

```
Cervical_Cancer_Detection/
│
├── main.py                  # Flask application & routes
├── predict.py               # ML prediction logic
├── fun.py                   # Utility functions (auth, CSV ops)
├── requirements.txt         # Python dependencies
├── runtime.txt              # Python version for deployment
│
├── templates/               # HTML templates
│   ├── login.html
│   ├── signup.html
│   ├── home.html
│   ├── predict.html
│   ├── history.html
│   └── activity.html
│
├── static/
│   └── imgs/
│       └── bg.jpg
│
└── pickels/                 # Trained ML models
    ├── logistic_regression.pkl
    ├── decision_tree.pkl
    ├── random_forest.pkl
    ├── svm.pkl
    ├── xgboost.pkl
    ├── data.csv             # Training dataset
    └── pickelgen.py         # Model training script
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/madhura276/Cervical_Cancer_Detection.git
cd Cervical_Cancer_Detection
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python main.py
```

### 5. Open in browser
```
http://127.0.0.1:5000
```

---

## 🖥️ How to Use

1. **Sign up** with your email, name, and country
2. **Login** with your credentials
3. Go to **Predict** and enter your medical details
4. View **individual predictions** from all 5 models
5. See the **overall risk assessment**
6. Check **History** to view past predictions
7. Check **Activity** to see your login/usage history

---

## 📊 Input Features Used for Prediction

| Feature | Description |
|---|---|
| Age | Patient's age |
| Number of sexual partners | Total number of sexual partners |
| First sexual intercourse | Age at first sexual intercourse |
| Number of pregnancies | Total pregnancies |
| Smokes | Whether the patient smokes (Yes/No) |
| Smokes (packs/year) | Smoking intensity |
| Hormonal Contraceptives | Usage (Yes/No) |
| Hormonal Contraceptives (years) | Duration of usage |
| STDs | History of STDs (Yes/No) |
| STDs: HPV | HPV diagnosis (Yes/No) |
| STDs: Number of diagnosis | Total STD diagnoses |
| Dx: CIN | CIN diagnosis (Yes/No) |
| Dx: HPV | HPV diagnosis flag (Yes/No) |
| Schiller | Schiller test result (Yes/No) |

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.  
It should **not** be used as a substitute for professional medical advice, diagnosis, or treatment.  
Always consult a qualified healthcare professional for medical decisions.

---

## 🌟 Future Improvements

- Replace CSV storage with a proper database (SQLite / PostgreSQL)
- Add deep learning models (Neural Networks)
- Implement password hashing for security
- Add email verification on signup
- Enhance UI/UX with modern dashboard design
- Add model explainability (SHAP values)

---

## 👩‍💻 Author

**Madhura Gundluru**  
Aspiring AI/GenAI Engineer | Python | ML | LangChain | Data Science  
📍 Bangalore, India  
🔗 [LinkedIn](https://www.linkedin.com/in/madhura-gundluru/)  
🐙 [GitHub](https://github.com/madhura276)

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub!
