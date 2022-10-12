from contextlib import nullcontext
from datetime import date
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganisationDetails = {}

@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html

    return render_template('index.html', currentDate=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def checkNumber():

    global number
    number = request.form['number']
    # Get Number from form and display message according to number
    #number = request.form('number')
    # Display "Number {Number} is even" if given number is even on result.html page
    if number == "":
        return render_template('result.html', numResult = "No number provided")
    elif not number.isnumeric():
        return render_template('result.html', numResult = "Not a number")
    elif int(number) % 2 == 0:
        return render_template('result.html', numResult = number + " is even")
    else:
        return render_template('result.html', numResult = number + " is odd")
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page

    # Display "Provided input is not an integer!" if value is not a number on result.html page
    

    # Write your to code here to check whether number is even or odd and render result.html page


@app.get('/studentForm')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    organization = request.form['org']

    # Append this value to studentOrganisationDetails
    studentOrganisationDetails[studentName] = organization

    # Display studentDetails.html with all students and organisations
    return render_template('studentDetails.html', studentOrganisationDetails=studentOrganisationDetails)