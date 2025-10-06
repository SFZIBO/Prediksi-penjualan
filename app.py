# File: app.py (Diperbarui)

from flask import Flask, render_template, request
import joblib
import json

app = Flask(__name__)

# Muat model
model = joblib.load('model_regresi.joblib')

# Muat hasil training dari file JSON
with open('training_results.json', 'r') as f:
    results = json.load(f)

# Route untuk halaman utama (prediksi)
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = ''
    if request.method == 'POST':
        try:
            rating_input = float(request.form['rating'])
            prediction = model.predict([[rating_input]])
            prediction_text = f"Estimasi Penjualan: {int(round(prediction[0])):,} unit"
        except ValueError:
            prediction_text = "Input tidak valid. Harap masukkan angka."
    
    # 'page':'home' digunakan untuk styling tab aktif
    return render_template('index.html', prediction_text=prediction_text, page='home')

# **BARU**: Route untuk halaman transparansi
@app.route('/transparency')
def transparency():
    # 'page':'transparency' digunakan untuk styling tab aktif
    return render_template('transparency.html', results=results, page='transparency')


if __name__ == '__main__':
    app.run(debug=True)