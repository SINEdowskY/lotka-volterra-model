from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import random

X0 = [10,10]

t = np.linspace(0, 50, 100)

def f(a,b,c,d):
    def dX_dt(X, t=0):
        preys, predators = X
        dPrey_dt = a * preys - b * predators * preys
        dPredator_dt = d * preys * predators - c * predators

        return [dPrey_dt, dPredator_dt]
    
    X, legenda = odeint(dX_dt, X0, t, full_output=True)
    return X

model = f(1,0.1,0.5,0.02)

fig, (ax1, ax2) = plt.subplots(2,1)
print(model)
ax1.plot(model)

ax1.legend(('Preys','Predators'))

ax2.plot(
    model[:,0], model[:,1]
)
plt.show()

