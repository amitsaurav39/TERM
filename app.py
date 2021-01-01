import pandas as pd

def readExcel():#empID
    df = pd.read_excel (r'C:\Users\amits\Downloads\punit files\Excel\TestingExcel.xlsx') 
    #    result=(data.loc[data['Employee ID']==user_data])
    return df

