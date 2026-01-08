import qutip as qt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


# Qubit (a 2 qubit-level system)
H = 0 * qt.sigmaz()    # No intrinsic Hamiltonian
times = np.linspace(0, 10, 100)

#Initial state |0
psi_0 = qt.basis(2,0)

# Gate Sequence: H -> X -> Y
H_gate = (1/np.sqrt(2))*qt.Qobj([[1,1], [1,-1]])
X_gate = qt.sigmax()
Y_gate = qt.sigmay()

# Time-Dependant Hamiltonian for gates
H_t = []
glist = [H_gate, X_gate, Y_gate]
tlist = np.array([0,3,6,10])        # gate times

for i in range(3):
    H_t.append([glist[i], lambda t, args: 1.0*(t>tlist[i])*(t<tlist[i+1])])

# Simulate
result = qt.sesolve(H_t, psi_0, times)

# Plot the Bloch Sphere Trajectory
fig = plt.figure()
b = qt.Bloch(fig=fig)
ax = fig.add_subplot(111, projection='3d')

def animate(i):
    b.clear()
    b.add_states(result.states[i])
    b.show()

anim = animation.FuncAnimation(fig,animate, frames=len(result.states), interval=50)
plt.show()