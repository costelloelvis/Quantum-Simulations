from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

#Create a qubit in superposition
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Use .draw() to see the circuit
print(qc.draw())

#Simulate locally (no explicit simulator needed)
state = Statevector(qc)
counts = state.sample_counts(1024)

#Plot results
plot_histogram(counts)
plt.show()