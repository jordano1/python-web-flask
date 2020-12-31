from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask_mail import Mail
import csv

app = Flask(__name__)
mail = Mail(app)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}
    

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject}{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('ty.html', usr=data)
        except:
            return 'did not save, error!', 
    else:
        return 'failed! something went wrong'
        #data = request.form['email', 'message', 'subject']

# @app.route('/works/')
# def works():
#     return render_template('works.html')


# @app.route('/work/')
# def work():
#     return render_template('work.html')

# @app.route('/about/')
# def about_me():
#     return render_template('about.html')


# @app.route('/contact/')
# def contact_me():
#     return render_template('contact.html')


# @app.route('/components/')
# def components():
#     return render_template('components.html')

