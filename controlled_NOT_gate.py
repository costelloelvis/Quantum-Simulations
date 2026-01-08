from qiskit import QuantumCircuit
from qiskit import Aer, execute

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

sim = Aer.get_backend('qasm_simulator')
job = execute(qc, sim)
result = job.result()
print(result.get_counts)