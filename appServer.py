import pandas as pd
import xlrd
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
        df=pd.read_excel(r'C:\Users\amits\Downloads\punit files\alpha version\Excel\TestingExcel.xlsx')
        result=(df.loc[df['Employee ID']==empID])
        return redirect(url_for('success', data=result))


#def readExcel():
    
    #user_data=empID
    
   # return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
