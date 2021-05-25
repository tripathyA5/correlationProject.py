import csv
import plotly.express as px
import numpy as np 

def getDataSource(data):
    sizeOfTV=[]
    averageTimeSpent=[]
    with open (data) as file1:
        df = csv.DictReader(file1)
        for row in df:
            sizeOfTV.append(float(row['Coffee in ml']))
            averageTimeSpent.append(float(row['sleep in hours']))
    return {'x': sizeOfTV, 'y': averageTimeSpent}
def findCorrelation(data1):
    correlation=np.corrcoef(data1['x'], data1['y'])
    print(correlation)
def setup():
    data='coffee vs sleep.csv'
    dataSource = getDataSource(data)
    findCorrelation(dataSource)
setup()
