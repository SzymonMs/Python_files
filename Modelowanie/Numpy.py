import numpy as np
numpyArr = np.array([1,2,3])
print(numpyArr)
numpyMatrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print((numpyMatrix))
print(type(numpyArr))
print(numpyMatrix.ndim)
numpyNDim = np.array([1,2,3,4], ndmin = 4)
print(numpyNDim)
print(numpyArr[-2])
longArray = np.array([1,2,3,4,5,6,7])
print(longArray[:])
print(longArray[1:5])
print(longArray[-1::-1]) #List reverse
print(longArray[0:8:2])
print(numpyMatrix[1,:]) #second row
print((np.array(['c','a','g']).dtype))
print((np.array([1,2,3,4,5]).dtype))
arrayFloat = np.array([1.1,2.2,3.3,4.5],dtype='f')
print(arrayFloat)
arrayNewInts = arrayFloat.astype(int);
arrayNewInts2 = arrayFloat.astype('i');
print(arrayNewInts)
print(arrayNewInts2)
arrString = np.array(["a","b","c"])
arrString2 = np.array(['A','B','C'])
print(arrString.dtype)
# arrStringToInt = arrString.astype(int) ERROR
# arrStringToInt = arrString.astype(int) ERROR


