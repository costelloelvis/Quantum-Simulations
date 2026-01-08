from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

# Create a Quantum Circuit with 11 qubits
qc = QuantumCircuit(11)

for i in range(10):
    qc.h(i)
    # Add a CNOT gate (control on qubit 0 , target on qubit 1)
    qc.cx(i, i+1)
    

# Draw The Circuit
qc.draw(output='mpl')
plt.show()