from Dataload import *
from Trasformations import *
from SaveData import *
if __name__=='__main__':
    ordersdf=Dataload('ordjsonfile')
    orderItemsdf=Dataload('orditjsonfile')
    Transformationsdf(ordersdf,orderItemsdf).show()
    savedata()
    #orderItemsdf.printSchema()