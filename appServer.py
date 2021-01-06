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
def tables():
    if request.method == 'POST':
        empID = request.form['nm']
        
        data=pd.read_excel(r'C:\Users\amits\Downloads\punit files\alpha version\Excel\TestingExcel.xlsx')
        data.set_index(['Name'], inplace=True)
        data.index.name=None
        result = data.loc[data.EmployeeID==empID]

        if result == None :

            return render_template('error.html')
            
        else:
            return render_template('view.html',tables=[result.to_html(classes='page')], 
            titles = ['na', 'Employee Details'])




        #return render_template('view.html',tables=[result.to_html(classes='page')], 
        #titles = ['na', 'Employee Details'])
        
        
        #if result.empty:
         #   return render_template('view.html')

       # if data.loc[data.EmployeeID==empID]:
        #    return render_template('view.html',tables=[result.to_html(classes='page')], 
       # titles = ['na', 'Employee Details'])
       # else:
       #     return render_template('error.html')
       # return render_template('view.html',tables=[result.to_html(classes='page')], 
      #  titles = ['na', 'Employee Details'])
      
      





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
