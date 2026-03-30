import pandas as pd
import pickle

def predict_cancer_outcome(
    age, num_partners, first_intercourse, num_pregnancies, smokes,
    packs_per_year, hormonal_contraceptives, contraceptives_years, stds,
    stds_hpv, stds_diagnosis, dx_cin, dx_hpv, schiller
):
    # Convert "yes"/"no" to 1/0
    mapping = {"yes": 1, "no": 0}

    def convert(val):
        if isinstance(val, str):
            return mapping.get(val.lower(), val)
        return val

    smokes = convert(smokes)
    hormonal_contraceptives = convert(hormonal_contraceptives)
    stds = convert(stds)
    stds_hpv = convert(stds_hpv)
    dx_cin = convert(dx_cin)
    dx_hpv = convert(dx_hpv)

    # Create DataFrame
    input_data = pd.DataFrame([[  
        age, num_partners, first_intercourse, num_pregnancies, smokes,
        packs_per_year, hormonal_contraceptives, contraceptives_years, stds,
        stds_hpv, stds_diagnosis, dx_cin, dx_hpv, schiller
    ]], columns=[
        "Age", "Number of sexual partners", "First sexual intercourse",
        "Num of pregnancies", "Smokes", "Smokes (packs/year)",
        "Hormonal Contraceptives", "Hormonal Contraceptives (years)", "STDs",
        "STDs:HPV", "STDs: Number of diagnosis", "Dx:CIN", "Dx:HPV", "Schiller"
    ])

    # Convert to numeric
    input_data = input_data.apply(pd.to_numeric, errors='coerce')

    # 🔥 IMPORTANT FIX
    input_data = input_data.fillna(0)

    # Model paths
    model_files = {
        "Logistic Regression": "pickels/logistic_regression.pkl",
        "Decision Tree": "pickels/decision_tree.pkl",
        "Random Forest": "pickels/random_forest.pkl",
        "SVM": "pickels/svm.pkl",
        "XGBoost": "pickels/xgboost.pkl",
    }

    predictions = {}

    for model_name, model_file in model_files.items():
        try:
            with open(model_file, "rb") as f:
                model = pickle.load(f)

            pred = model.predict(input_data)[0]
            predictions[model_name] = int(pred)

        except Exception as e:
            predictions[model_name] = f"Error: {str(e)}"

    return predictions


def evaluate_safety(model_outputs):
    zero_count = list(model_outputs.values()).count(0)
    total_models = len(model_outputs)

    if total_models == 0:
        return "No predictions available."

    zero_percentage = (zero_count / total_models) * 100

    if zero_count == total_models:
        return "100% Safe."
    elif zero_count >= 4:
        return "80% Safe."
    elif zero_count >= 3:
        return "Getting hospital advice is recommended."
    else:
        return "Check the hospital immediately. Better to be cautious."