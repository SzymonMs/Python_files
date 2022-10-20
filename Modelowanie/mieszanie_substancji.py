from matplotlib import pyplot as plt
from math import sqrt
from math import sin
Tp = 0.1 #s
beta = 0.035 #m^{5/2}/s^2
A = 1.5 #m^2
t_sim = 3600 #s
h_min = 0.0 #m
h_max = 5.0 #m
V_min = 0.0 #m^3
V_max = h_max*A #m^3
c_min = 0.0
c_max = 1.0
N = int(t_sim/Tp)+1
V = [0.0,]
c = [0.0,]
cd1 = [0.9,]
cd2 = [0.8,]
Qd2 = [0.05,]
t = [0.0,]
Qd1 = [sin(t[-1]),]
h = [0.0,]
Qo = [beta*sqrt(h[-1])]
for n in range(1,N):
    t.append(n * Tp)
    Qd1.append(sin(t[-1]))
    Qd2.append(Qd2[-1])
    h.append(min(max(Tp*(Qd1[-1]+Qd2[-1]-Qo[-1])/A+h[-1],h_min),h_max))
    V.append(min(max(Tp * (Qd1[-1] + Qd2[-1] - Qo[-1]) + V[-1],V_min),V_max))
    c.append(min(max(1/V[-1]*(Qd1[-1]*(cd1[-1]-c[-1])+Qd2[-1]*(cd2[-1]-c[-1]))*Tp+c[-1],c_min),c_max))
    Qo.append(beta*sqrt(h[-1]))

print(h[-10:])
print(c[-10:])
print(V[-10:])

plt.figure()
plt.plot(t,h)
plt.title("Wysokość h")
plt.xlabel("t [s]")
plt.ylabel("h [m]")
plt.grid()

plt.figure()
plt.plot(t,V)
plt.title("Objętość V")
plt.xlabel("t [s]")
plt.ylabel("V [m]")
plt.grid()


plt.figure()
plt.plot(t,c)
plt.title("Stężenie c")
plt.xlabel("t [s]")
plt.ylabel("c [m]")
plt.grid()

plt.figure()
plt.plot(t,Qd1)
plt.title("Dopływ Qd1")
plt.xlabel("t [s]")
plt.ylabel("Qd1 [m]")
plt.grid()

plt.show()
