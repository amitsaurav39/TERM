
from app import readExcel
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/success/<data>')
def success(data):
    return data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        empID = request.form['nm']
        excelData = readExcel()
        return redirect(url_for('success', data=excelData))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
