from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
import matplotlib
import numpy as np
import random

 #initial 


def diffrential_equations(a,b,c,d, initial_preys, initial_predators):
    def dX_dt(X, t=0):
        preys, predators = X
        dPrey_dt = a * preys - b * predators * preys
        dPredator_dt = d * preys * predators - c * predators

        return [dPrey_dt, dPredator_dt]
    t = np.linspace(0, 15, 1000)
    X0 = [initial_preys, initial_predators]
    X, legenda = odeint(dX_dt, X0, t, full_output=True)
    return X


def preys_vs_predators_plot(model) -> Figure:
    matplotlib.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2,1)
    ax1.plot(model)
    ax1.legend(('Preys','Predators'), frameon=True)
    ax1.set_ylabel("Population")
    ax1.set_xlabel("Time")
    ax2.plot(
    model[:,0], model[:,1]
    )
    ax2.set_ylabel("Predators")
    ax2.set_xlabel("Preys")
    fig.tight_layout(h_pad=1)
    return fig

def animated_plot(model):
    fig, ax = plt.subplots()
    plt.xlim([0,15])
    plt.ylim([0,40])
    ax.set_ylabel("Population")
    ax.set_xlabel("Time")

    y_to_update = np.linspace(0, 15, 1000)
    
    x_prey = []
    y_prey = []
    prey_to_update = model[:,0]
    line_prey, = ax.plot(0, 0)

    x_predator = []
    y_predator = []
    predator_to_update = model[:,1]
    line_predator, = ax.plot(0, 0)

    x_prey_point = 0
    y_prey_point = 0
    prey_point, = ax.plot(0,0, 'o')
    
    x_predator_point = 0
    y_predator_point = 0
    predator_point, = ax.plot(0,0, 'o')
    def animate(i):
        x_prey.append(prey_to_update[i])
        y_prey.append(y_to_update[i])
        line_prey.set_ydata(x_prey)
        line_prey.set_xdata(y_prey)

        x_prey_point = y_to_update[i]
        y_prey_point = prey_to_update[i]

        prey_point.set_xdata(x_prey_point)
        prey_point.set_ydata(y_prey_point)

        x_predator.append(predator_to_update[i])
        y_predator.append(y_to_update[i])
        line_predator.set_ydata(x_predator)
        line_predator.set_xdata(y_predator)

        x_predator_point = y_to_update[i]
        y_predator_point = predator_to_update[i]

        predator_point.set_xdata(x_predator_point)
        predator_point.set_ydata(y_predator_point)

        return line_predator, line_prey, prey_point, predator_point

    ax.legend(('Preys','Predators'), frameon=True)
    ani= FuncAnimation(
        fig, animate, interval=20, blit=True, frames=1000)
    
    ani.save('./plots/plotanimation.gif')

def animated_phase(model):
    fig, ax = plt.subplots()

    line, = ax.plot(
    model[:,0], model[:,1]
    )
    x = 0
    y = 0
    point, = ax.plot(x,y, 'o')
    ax.set_ylabel("Predators")
    ax.set_xlabel("Preys")
    def animate(i):
        x = model[i,0]
        y = model[i,1]

        point.set_xdata(x)
        point.set_ydata(y)

        return point,
    
    ani = FuncAnimation(
        fig, animate, interval=20, blit=True, frames=1000)
    ani.save('./plots/phaseanimation.gif')



