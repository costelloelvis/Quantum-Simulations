import matplotlib.pyplot as plt
from qiskit import QuantumCircuit

try:
    # Use from_qasm_file directly so Qiskit can find the include files automatically
    qc = QuantumCircuit.from_qasm_file('qasm_test.qasm')
    
    print("File loaded successfully!")
    qc.draw(output='mpl')
    plt.show()

except FileNotFoundError:
    print('Error: "qasm_test.qasm" file not found. Check the file path.')
except Exception as e:
    print(f"An unexpected error occurred: {e}")