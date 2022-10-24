# Symulator zbiornika z dopłyewm i odpłyewm swobodnym https://www.cs.put.poznan.pl/pzakrzewski/pa/pa_wykład_2.pdf
from math import sqrt
from matplotlib import pyplot as plt
import plotly.graph_objects as px

def PrintPlot(fig,x,y,name,title,xaxis,yaxis, print = True):
    fig.add_trace(px.Scatter(x=x, y=y, mode='lines', name=name))
    fig.update_layout(
        title = title,
        yaxis_title=yaxis,
        xaxis_title=xaxis,
        legend_title="Legenda",
    )
    if(print):
        fig.show()
def PyplotPlot():
    plt.figure
    plt.plot(t, h)
    plt.title("Wysokość h")
    plt.xlabel("t [s]")
    plt.ylabel("h [m]")
    plt.grid()

    plt.figure()
    plt.plot(t, Qo)
    plt.plot(t, Qd)
    plt.title("Odpływ oraz Dopływ")
    plt.xlabel("t [s]")
    plt.ylabel(r'$Q_o, Q_d \  [\frac{m^3}{s}]$')
    plt.grid()
#biblioteki bokeh, plotly
A = 1.5 #m^2
beta = 0.035 #m^{5/2}/s
h_min = 0.0 #m
h_max = 5.0 #m
Tp = 0.1 #s
t_sim = 3600 #s
N = int(t_sim/Tp)+1 #ile kroków symulacji
h = [0.0,]
t = [0.0,]
Qd = [0.05,] #zmienna sterująca, dopływ
Qo = [beta*sqrt(h[-1])] #zakłócenie, odpływ
for n in range(1,N):
    t.append(n*Tp)
    Qd.append(Qd[-1])
    h.append(min(max(Tp*(Qd[-1]-Qo[-1])/A+h[-1],h_min),h_max)) #czy to wyliczone h mieści się między h_min a h_max
    #h.append(Tp*(Qd[-1]-Qo[-1])/A+h[-1])
    Qo.append(beta*sqrt(h[-1]))
print(h[-10:])
print(Qd[-1],Qo[-1]) #jeżeli te dwie wartości są równe to jest stan ustalony bo Adh/dt=Qd-Qo to stan ustalony Qd=Qo
# Pierwszy układ współrzędnych h(t) a drugi Qd(t) i Qo(t)


PyplotPlot()

fig = px.Figure()
fig2 = px.Figure()

PrintPlot(fig,t,h,'wysokość','Wysokość','t[s]','h[m]')
PrintPlot(fig2,t,Qo,'odpływ','Odpływ i dopływ','t[s]','Qo[m^3/s]',print=False)
PrintPlot(fig2,t,Qd,'dopływ','Odpływ i dopływ','t[s]','Qo[m^3/s]')

#plt.show()


