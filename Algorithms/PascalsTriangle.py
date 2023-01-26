file = "pascal.txt"
file2 = "sierpinski.txt"
""""
@brief Calculates factorial of number
@param n is natural number
@return natural number equals n!
"""
def Factorial(n):
    factorial = 1
    if n == 0:
        return factorial
    else:
        while(n>1):
            factorial = factorial*n
            n = n-1
    return int(factorial)
""""
@brief Calculates Newton's symbol for two numbers
@param n is natural number
@param k is natural number
@return natural number equals (n k)
"""
def NewtonsSymbol(n,k):
    if k>= 0 and n>=k:
        newtonsSymbol =int(Factorial(n)/(Factorial(k)*Factorial(n-k)))
        return newtonsSymbol
    else:
        return None
""""
@brief Calculate numbers from Pascal's triangle
@param n is number of rows is Triangle
@return list of numbers from Pascal's Triangle
"""
def PascalsTriangle(n):
    pascalsTriangle = []
    for i in range(0,n+1):
        k = i + 1
        for j in range(0,k):
            pascalsTriangle.append(NewtonsSymbol(i,j))
    return pascalsTriangle
""""
@brief Prints Pascal's triangle in nice form for numbers in range (1,999) and saves data to pascal.txt
@param pascalsTriangle is list of numbers from Pascal's triangle
"""
def PrintPascalsTriangle(pascalsTriangle):
    length = len(pascalsTriangle)
    rows = 0
    while(length>=0):
        length = length - (rows + 1)
        rows = rows + 1
    num = rows
    counter = 0
    iterator = 0
    f = open(file,"w")
    for i in range(0,rows):
        if (iterator >= len(pascalsTriangle)):
            break
        for m in range(0,num):
            print("  ",end="")
            f.write("  ")
        for mm in range(0,counter+1):
            test = iterator+1
            if(test>=len(pascalsTriangle)):
                test = test-1
            if(pascalsTriangle[test]<10):
                print(str(pascalsTriangle[iterator]) + "   ",end="")
                f.write(str(pascalsTriangle[iterator]) + "   ")
            elif(pascalsTriangle[test]>100):
                print(str(pascalsTriangle[iterator]) + " ",end="")
                f.write(str(pascalsTriangle[iterator]) + " ")
            else:
                print(str(pascalsTriangle[iterator]) + "  ",end="")
                f.write(str(pascalsTriangle[iterator]) + "  ")
            iterator = iterator+1
        for mmm in range(0,num):
            print(" ",end="")
            f.write(" ")
        print("\n",end="")
        f.write("\n")
        counter = counter+1
        num = num-1
    f.close()
""""
@brief Prints Sierpiński triangle in nice form for numbers in range (1,999) and save data to file sierpinski.txt
@param n number of rows in Sierpiński Triangle
"""
def SierpinskiTriangle(n):
    pascalsTriangle = PascalsTriangle(n)
    sierpinskiTriangle = []
    for x in range(0,len(pascalsTriangle)):
        if(pascalsTriangle[x]%2!=0):
            sierpinskiTriangle.append("#")
        else:
            sierpinskiTriangle.append(" ")
    length = len(pascalsTriangle)
    rows = 0
    while(length>=0):
        length = length - (rows + 1)
        rows = rows + 1
    num = rows
    counter = 0
    iterator = 0
    f = open(file2,"w")
    for i in range(0,rows):
        if (iterator >= len(pascalsTriangle)):
            break
        for m in range(0,num):
            print("  ",end="")
            f.write("  ")
        for mm in range(0,counter+1):
            test = iterator+1
            if(test>=len(pascalsTriangle)):
                test = test-1
            if(pascalsTriangle[test]<10):
                print(sierpinskiTriangle[iterator] + "   ",end="")
                f.write(sierpinskiTriangle[iterator] + "   ")
            elif(pascalsTriangle[test]>100):
                sierpinskiTriangle[iterator]=sierpinskiTriangle[iterator]+"  "
                print(sierpinskiTriangle[iterator] + " ",end="")
                f.write(sierpinskiTriangle[iterator] + " ")
            else:
                sierpinskiTriangle[iterator]=sierpinskiTriangle[iterator] + " "
                print(sierpinskiTriangle[iterator] + "  ",end="")
                f.write(sierpinskiTriangle[iterator] + "  ")
            iterator = iterator+1
        for mmm in range(0,num):
            print(" ",end="")
            f.write(" ")
        print("\n",end="")
        f.write("\n")
        counter = counter+1
        num = num-1
    f.close()
if __name__ == '__main__':
    PrintPascalsTriangle(PascalsTriangle(10))
    SierpinskiTriangle(100)