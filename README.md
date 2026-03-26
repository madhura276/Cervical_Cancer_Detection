# 🧠 Web-Based Infrastructure for Optimized Cervical Cancer Detection and Screening

## 📌 Project Overview
This project is a **web-based AI application** designed to predict the risk of cervical cancer using multiple machine learning models.  
Users can enter medical and lifestyle details, and the system provides predictions along with a risk assessment.

The goal of this project is to assist in **early detection and awareness** of cervical cancer.

---

## 🚀 Features

- 🔐 User Authentication (Login & Signup)
- 📊 AI-Based Prediction System
- 🤖 Multiple Machine Learning Models:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Support Vector Machine (SVM)
  - XGBoost
- 📈 Prediction Visualization (Charts)
- 🧾 User History Tracking
- 📅 Activity Monitoring
- 📥 Downloadable Prediction Report (PDF)

---

## 🧠 Machine Learning Workflow

1. Data preprocessing and cleaning
2. Feature selection based on medical attributes
3. Training multiple ML models
4. Model evaluation and comparison
5. Real-time prediction using trained models

---

## 🛠️ Technologies Used

### 💻 Backend
- Python
- Flask

### 📊 Machine Learning
- Scikit-learn
- XGBoost
- Pandas
- NumPy

### 🌐 Frontend
- HTML
- CSS
- JavaScript

### 📈 Visualization
- Chart.js

---

## 📂 Project Structure
project/
│
├── main.py # Flask application
├── predict.py # ML prediction logic
├── fun.py # Utility functions
├── templates/ # HTML files
│ ├── login.html
│ ├── signup.html
│ ├── home.html
│ ├── predict.html
│ ├── history.html
│ └── activity.html
│
├── pickels/ # Trained ML models
├── reg.csv # User data
└── README.md

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository
git clone https://github.com/your-username/cervical-cancer-detection.git
cd cervical-cancer-detection

### 2️⃣ Install dependencies

pip install flask pandas numpy scikit-learn xgboost

### 3️⃣ Run the application
python main.py

### 4️⃣ Open in browser
http://127.0.0.1:5000/

## Prediction Output:
Each model gives a prediction:
0 → No Cancer
1 → Cancer
Final result is generated based on combined model outputs.

## ⚠️ Disclaimer
This project is for educational and research purposes only.
It should not be used as a substitute for professional medical advice.

## 👩‍💻 Author

Madhura Gundluru
Passionate about AI, Data Science & Full Stack Development
Focused on building impactful real-world applications

## 🌟 Future Improvements
Improve model accuracy with larger datasets
Add deep learning models
Deploy as a live web application
Enhance UI/UX with advanced dashboards

## ⭐ Support
If you like this project, consider giving it a ⭐ on GitHub!
