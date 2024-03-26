import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def save_to_csv(data):
    with open('form_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Age', 'Phone', 'Proof of Identity', 'Proof of Age', 'Proof of Residence']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        age = request.form['age']
        phone = request.form['phone']
        proof_identity = request.form['proof_identity']
        proof_age = request.form['proof_age']
        proof_residence = request.form['proof_residence']
        
        # Save form data to CSV file
        form_data = {
            'Name': name,
            'Age': age,
            'Phone': phone,
            'Proof of Identity': proof_identity,
            'Proof of Age': proof_age,
            'Proof of Residence': proof_residence
        }
        save_to_csv(form_data)
        
        # Redirect to a thank you page or render a success message
        return redirect(url_for('thank_you'))
    return render_template('book.html')


@app.route('/thank-you')
def thank_you():
    return 'Thank you for submitting the form!'

if __name__ == '__main__':
    app.run(debug=True,port=50000)
