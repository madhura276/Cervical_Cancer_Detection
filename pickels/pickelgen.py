import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
data = pd.read_csv("pickels/data.csv")

# Define the top 14 features (excluding "Biopsy")
top_14_features = [
    "Age",
    "Number of sexual partners",
    "First sexual intercourse",
    "Num of pregnancies",
    "Smokes",
    "Smokes (packs/year)",
    "Hormonal Contraceptives",
    "Hormonal Contraceptives (years)",
    "STDs",
    "STDs:HPV",
    "STDs: Number of diagnosis",
    "Dx:CIN",
    "Dx:HPV",
    "Schiller",
]

# Split data into features (X) and target (y)
X = data[top_14_features]
y = data["Biopsy"]

# Handle missing values
imputer = SimpleImputer(strategy="mean")  # Replace missing values with the mean
X = pd.DataFrame(imputer.fit_transform(X), columns=top_14_features)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models
models = {
    "logistic_regression": LogisticRegression(max_iter=1000),  # Increased iterations
    "decision_tree": DecisionTreeClassifier(),
    "random_forest": RandomForestClassifier(n_estimators=100),  # Increased estimators
    "svm": SVC(probability=True),
    "xgboost": XGBClassifier(use_label_encoder=False, eval_metric="logloss", n_estimators=200),  # Increased iterations
}

# Train, evaluate, and save models
for model_name, model in models.items():
    print(f"Training {model_name}...")
    model.fit(X_train, y_train)
    
    # Save the model
    with open(f"pickels/{model_name}.pkl", "wb") as f:
        pickle.dump(model, f)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{model_name.capitalize()} Accuracy: {accuracy:.2%}")

print("All models trained, evaluated, and saved successfully.")
