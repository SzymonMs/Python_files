from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.randint(100) #Random Number 0..100
print('zmienna x = {}'.format(x))

f= random.rand()
print('zmienna f = {}'.format(f)) #Random float number 0..1

randArray = random.randint(100,size=6) #rozmiar może być 2D size = (3,4)
print("tablica o rozmiarze size, złożona z liczb pseudolosowych: {}".format(randArray))
randArrayFloat = random.rand(6) #Bez podania zmiennej size, może być 2D = (2,3)
print("tablica o rozmiarze 6, złożona z liczb losowych: {}".format(randArrayFloat))

numberFromArray = random.choice([1,2,3,4,7,8,9]) #wylosowanie elementu z tablicy
print("Liczba wylosowana z tablicy: {}".format(numberFromArray))
#Funkcja choice pozwala na zdefiniowanie prawdopodobieństw poszczególnych liczb
numberFromArray = random.choice([1,2,3], p=[0.7,0.2,0.1],size=100)
print("Wektor liczb losowych z tablicy, o pewnych prawdopodobieńtwach: {}".format(numberFromArray))

array = [1,2,4,8,16,32]
print(array)
random.shuffle(array) #Permutacja tablicy, działa na orginale
print(array)
array2 = random.permutation(array) #Permutacja tablicy, tworzy kopie
print(array2)

sns.displot([0,1,2,3,4,5]) #Histogram z Seaborn module

normalDistribution = random.normal(loc = 1, scale = 2, size = 1000)
sns.displot(normalDistribution,kind='kde')
plt.show()