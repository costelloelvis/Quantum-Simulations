from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

# Create a Quantum Circuit with 11 qubits
qc = QuantumCircuit(10)
qc.h(0)

for i in range(9):
    # Add a TOFFOLI gate (control on qubit 0 , target on qubit 1)
    qc.ccx(i-1,i,i+1)
    

# Draw The Circuit
qc.draw(output='mpl')
plt.show()