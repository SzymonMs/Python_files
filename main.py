#####LISTA#####
lista=[1,2,55,"apple"]
lista.append(6)   #dodaje element na końcu listy
lista.insert(0,77)   #wstawia element 77 na pozycje 0
lista.remove(2)   #usuwa pierwszy element, który jest równy 2
lista.pop(1)   #usuwa element o indeksie jeden
lista.pop()   #usuwa ostatni element
lista.clear()   #usuwa wszystko z listy
lista=[1,1,1,4]
lista.reverse()   #odwraca liste, nie zwraca wartości, trzeba printować osobno
print(lista)

#####KROTKA#####
tuple=1,1,5,'hello'   #pakowanie krotki
print(tuple[2])
u=tuple,(2,4,'a')   #zagnieżdżanie krotki
print(u)
pusta_krotka=()
krotka_z_jednym_elementem=1,
print(krotka_z_jednym_elementem)

#####ZBIÓR#####
zbior={'a','b','c','d','a'}
print(zbior)   #usuwa duplikaty, bo w zbiorze nie m duplikatu, 'a' wystąpi tylko raz
a=set('hahkklacadjk')
b=set('hijiahklac')
print(a)   #zwraca poszczegolne znaki ze zbioru a
c=a-b   #różnica zbiorów
d=a|b   #suma zbiorów
e=a&b   #iloczyn zbiorów
f=a^b   #różnica symetryczna zbiorów

#####SŁOWNIK#####
telefony={'ania':456789123,'ola':123456987,'iza':123}
dictionary={x: x**2 for x in (2,4,6)}   #słownik 2:4,4:16,6:36
slownik=dict(sape=1,guido=2,ala=3)
print(slownik)
