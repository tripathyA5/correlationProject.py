import csv
import plotly.express as px
import numpy as np 

def getDataSource(data):
    sizeOfTV=[]
    averageTimeSpent=[]
    with open (data) as file1:
        df = csv.DictReader(file1)
        for row in df:
            sizeOfTV.append(float(row['Marks In Percentage']))
            averageTimeSpent.append(float(row['Days Present']))
    return {'x': sizeOfTV, 'y': averageTimeSpent}
def findCorrelation(data1):
    correlation=np.corrcoef(data1['x'], data1['y'])
    print(correlation)
def setup():
    data='correlation2.csv'
    dataSource = getDataSource(data)
    findCorrelation(dataSource)
setup()
