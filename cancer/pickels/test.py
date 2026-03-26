import pandas as pd
import numpy as np
import pickle

# Load the random test data (example data, replace with real test cases if needed)
random_test_data = pd.DataFrame(
    np.random.randint(1, 10, size=(5, 15)),  # Generating random integers for 5 samples and 15 features
    columns=[
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
        "Biopsy",
    ],
)

# Fill in any missing values (if any)
random_test_data = random_test_data.fillna(random_test_data.mean())

# Models to test
model_files = [
    "logistic_regression.pkl",
    "decision_tree.pkl",
    "random_forest.pkl",
    "svm.pkl",
    "xgboost.pkl",
]

print("Random Test Data:")
print(random_test_data)

print("\nModel Predictions:")

for model_file in model_files:
    with open(model_file, "rb") as f:
        model = pickle.load(f)

    try:
        predictions = model.predict(random_test_data)
        print(f"{model_file.split('.')[0].replace('_', ' ').capitalize()} Predictions: {predictions}")
    except Exception as e:
        print(f"Error with {model_file.split('.')[0].replace('_', ' ').capitalize()}: {e}")
