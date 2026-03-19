from flask import Flask, render_template, request, redirect
from models import Patient, ClinicQueue

app = Flask(__name__)

clinic = ClinicQueue()

@app.route('/')
def home():
    patients = clinic.get_all_patients()
    return render_template('home.html', patients=patients)

@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        patient = Patient(name)
        clinic.add_patient(patient)
        return redirect('/')
    return render_template('add.html')

@app.route('/serve')
def serve():
    clinic.serve_patient()
    return redirect('/')

@app.route('/stats')
def stats():
    total = clinic.get_total_seen()
    return render_template('stats.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)