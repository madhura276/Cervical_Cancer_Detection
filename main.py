from flask import Flask, render_template, request, flash
import predict as p1
import fun

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if fun.authenticate_user(email, password):
            fun.set_mail(email)
            fun.insert_login_time(fun.getmail())
            return render_template('home.html')
        else:
            temp = []
            temp.append(('error', 'Email or Password not correct, try again'))
            return render_template('login.html', messages=temp)

    fun.set_mail("")
    return render_template('login.html')


@app.route('/logout')
def logout():
    fun.update_logout_time(fun.getmail())
    fun.set_mail("")
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        country = request.form['country']

        temp = []
        response = fun.add_user(email, password, country, name, "reg.csv")

        if response == 'User already exists in the CSV file.':
            temp.append(('error', 'User already exists. Please login.'))
            return render_template('signup.html', messages=temp)

        elif response == 'User added successfully.':
            temp.append(('success', response))
            users[email] = password
            flash('Account created successfully! Please log in.', 'success')
            return render_template('login.html', messages=temp)

    return render_template('signup.html')


@app.route('/home')
def welcome():
    fun.update_last_click_time(fun.getmail())
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    fun.update_last_click_time(fun.getmail())

    if request.method == 'POST':
        email = fun.getmail()

        # Get form data
        name = request.form.get('name')
        age = request.form.get('age')
        num_partners = request.form.get('num_partners')
        first_intercourse = request.form.get('first_intercourse')
        smokes = request.form.get('smokes')
        packs_per_year = request.form.get('packs_per_year')
        hormonal_contraceptives = request.form.get('hormonal_contraceptives')
        contraceptives_years = request.form.get('contraceptives_years')
        num_pregnancies = request.form.get('num_pregnancies')
        stds = request.form.get('stds')
        stds_hpv = request.form.get('stds_hpv')
        stds_diagnosis = request.form.get('stds_diagnosis')
        dx_cin = request.form.get('dx_cin')
        dx_hpv = request.form.get('dx_hpv')
        schiller = request.form.get('schiller')

        # Prediction
        prediction_result = p1.predict_cancer_outcome(
            age, num_partners, first_intercourse, num_pregnancies, smokes,
            packs_per_year, hormonal_contraceptives, contraceptives_years, stds,
            stds_hpv, stds_diagnosis, dx_cin, dx_hpv, schiller
        )

        # 🔥 SAFE CONVERSION FIX
        safe_result = {}
        for k, v in prediction_result.items():
            try:
                safe_result[k] = int(v)
            except:
                safe_result[k] = v

        prediction_result = safe_result

        # Save data
        fun.insert_data_to_csv(
            email, name, age, num_partners, first_intercourse, num_pregnancies,
            smokes, packs_per_year, hormonal_contraceptives, contraceptives_years,
            stds, stds_hpv, stds_diagnosis, dx_cin, dx_hpv, schiller,
            p1.evaluate_safety(prediction_result)
        )

        return render_template(
            'predict.html',
            results=prediction_result,
            name=name,
            r1=p1.evaluate_safety(prediction_result)
        )

    return render_template('predict.html')


@app.route('/history')
def user_history():
    email = fun.getmail()
    fun.update_last_click_time(email)
    user_data = fun.get_user_history(email)
    return render_template('history.html', user_data=user_data)


@app.route('/activity')
def activity():
    email = fun.getmail()
    fun.update_last_click_time(email)
    user_activity = fun.get_user_activity(email)
    return render_template('activity.html', user_activity=user_activity, email=email)


import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)