import numpy as np
def MyOwnAdd(x,y):
    return x+y-2*x
MyOwnAdd = np.frompyfunc(MyOwnAdd,2,1) #Tworzy z własnej funkcji, funkcje która działa na ndarray
print(MyOwnAdd([1,2,4],[1,1,1]))