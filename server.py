from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")


def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")


def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        first_name = data["first name"]
        last_name = data['last name']
        sex = data['sex']
        email = data['email']
        phone_number = data['phone number']
        expectations = data['message']
        file = database.write(f'\n {first_name}, {last_name}, {sex}, {email}, {phone_number}, {expectations} ')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        first_name = data["first name"]
        last_name = data['last name']
        sex = data['sex']
        email = data['email']
        phone_number = data['phone number']
        expectations = data['message']
        csv_writer = csv.writer(database2, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([first_name,last_name,sex,email,phone_number,expectations])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou_index.html')
    else:
        return "Something went wrong, do well to check your connection and try once again"