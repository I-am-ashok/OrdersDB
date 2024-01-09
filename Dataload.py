from SparkSession import spark
import os

def variable(variablefilename='variable.txt',folder='Config'):
    filepath= os.path.abspath(os.path.join(folder,variablefilename))
    with open(filepath,'r') as file:
        var={}
        for line in file:
            key,value=map(str.strip,line.split('='))
            var[key]=value
    return var

variables=variable()

def Dataload(file):
    df=spark().read.format("json").load(variables.get(file))
    return df