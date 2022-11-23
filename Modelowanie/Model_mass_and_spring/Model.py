import control
import numpy as np
import plotly.graph_objects as px

#PARAMETRY MODELU
m = 5.0
B = 0.1
k = 0.3

#PARAMETRY SYMULACJI
Tp = 0.1
tSim = 100
N = int(tSim/Tp)+1
t = [0.0,Tp,]

#WARTOŚĆ ZADANA
xSet = [1.23,]

#REGULACJA PID
F = [0.0,0.0,]
x = [0.0,0.0,]
xMin = 0.0
xMax = 5.0
Fmin = -2.0
Fmax = 2.0
Kp = 1.0
Ti = 10.0
Td = 5.0
errorSum = 0.0
prevError = 0.0
prevInt = 0.0

#REGULACJA LQR
x1 = [0.0,]
x2 = [0.0,]
FLQR = [0.0,]
Ad = np.array([[0,-k/m],[1,-B/m]])
Bd = np.array([[1/m],[0]])
Q = np.array([[1,0],[0,1]])
R = 1
kLQR, S, E =  control.lqr(Ad,Bd,Q,R)
x2r = xSet[-1]
x1r = (B/m)*x2r
Fr = k*x2r

#SYMULACJA
for n in range(2,N):
    #PID
    error = xSet[-1]-min(max(Tp**2/m*F[-2]+(2*m-B*Tp)/m*x[-1]+(B*Tp-k*Tp**2-m)/m*x[-2],xMin),xMax)
    derivative = error - prevError
    prevError = error
    errorSum = error + prevInt
    prevInt = errorSum
    F.append(min(max(error * Kp + errorSum * Tp / Ti + derivative * Td/Tp,Fmin),Fmax))
    x.append(min(max(Tp**2/m*F[-2]+(2*m-B*Tp)/m*x[-1]+(B*Tp-k*Tp**2-m)/m*x[-2],xMin),xMax))
    xSet.append(xSet[-1])

    #LQR
    x1.append(x1[-1]-(k*Tp)/m*x2[-1]+Tp/m*FLQR[-1])
    x2.append(min(max(Tp*x1[-1]+(1-(B*Tp)/m)*x2[-1],xMin),xMax))
    FLQR.append(min(max(Fr+kLQR[0][0]*(x1r-x1[-1])+kLQR[0][1]*(x2r-x2[-1]),Fmin),Fmax))

    t.append(n * Tp)
    
#WYKRESY
fig = px.Figure()
fig2 = px.Figure()
fig.add_trace(px.Scatter(x=t, y=x2,name="xLQR"))
fig.add_trace(px.Scatter(x=t, y=x,name="xPID"))
fig.add_trace(px.Scatter(x=t,y=xSet,name="xSet"))
fig.update_layout(
    title = "Odpowiedź obiektu i wartość zadana",
    yaxis_title = "x[m]",
    xaxis_title = "t[s]",
    legend_title="Legenda",
)
fig2.add_trace(px.Scatter(x=t,y=F,name="F_PID"))
fig2.add_trace(px.Scatter(x=t,y=FLQR,name="F_LQR"))
fig2.update_layout(
    title = "Sygnał sterujący",
    yaxis_title = "F[N]",
    xaxis_title = "t[s]",
    legend_title="Legenda",
)
fig.show()
fig2.show()
