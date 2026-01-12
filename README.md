# Quantum-Simulations

This repository contains a collection of **quantum mechanics and quantum computing simulations**, implemented primarily in **Python**.  
The project combines **numerical quantum physics**, **quantum circuits**, and **QASM-based simulations**, with applications ranging from foundational quantum systems to quantum-dot models.

## 📂 Project Structure

QUANTUM-SIMULATIONS/
│
├── tests/ # Test scripts
│ └── bc_test.py
│
├── calculator.py # Basic quantum/math utilities
├── 3D-Hadamard.py # 3D visualization of Hadamard transformations
├── Auger-Recombination-Decay.py # Auger recombination decay simulation
├── block_rotation.gif # Quantum rotation visualization
├── block_rotation.py # Rotation operator simulations
├── cc_gate.py # Controlled-Controlled (Toffoli) gate
├── Circuit.png # Quantum circuit diagram
├── cnot_gate_11_qubits.py # CNOT gate for multi-qubit systems
├── CNOT_gate.py # Standard CNOT gate implementation
├── cnot.py # CNOT gate examples
├── controlled_NOT_gate.py # Controlled-NOT gate simulation
├── dimple_qasm.qasm # OpenQASM quantum circuit
├── Hadamard.py # Hadamard gate simulation
├── main.py # Main entry point for simulations
├── PL_of_Quantum_Dots_With_Unifo… # Photoluminescence of quantum dots
├── qas.py # QASM processing utilities
├── qasm_test.qasm # Test OpenQASM file
├── Qiskit-Circuit.py # Quantum circuit using Qiskit
├── qiskit-test.py # Qiskit test simulations
├── qsm.py # Quantum state manipulation
├── Quantum-Confined-Stark-Effect… # QCSE simulation
├── qubit-mesolve.py # Time evolution of qubits
├── quip-rabi.py # Rabi oscillation simulation
├── README.md # Project documentation
└── statevector.py # Statevector-based simulations


## 🧪 Topics Covered

- Quantum gates (Hadamard, CNOT, CCNOT)
- Multi-qubit quantum circuits
- Quantum statevectors
- Quantum circuit simulation with **Qiskit**
- OpenQASM circuit descriptions
- Rabi oscillations
- Quantum time evolution
- Quantum dots and photoluminescence
- Quantum Confined Stark Effect (QCSE)
- Auger recombination decay

## 🛠️ Tools & Libraries

- **Python 3**
- **NumPy**
- **SciPy**
- **Matplotlib**
- **Qiskit**
- **QuTiP** (for time evolution and mesolve-based simulations)
- **OpenQASM**


### 1️⃣ Clone the repository

###
git clone https://github.com/costelloelvis/quantum-simulations.git
cd quantum-simulations
###

2️⃣ Create a virtual environment (recommended)
python -m venv venv

venv\Scripts\activate     # Windows

source venv/bin/activate   # Linux

3️⃣ Install dependencies
pip install -r requirements.txt


(If requirements.txt is missing, install manually:)

pip install numpy scipy matplotlib qiskit qutip

4️⃣ Run a simulation
python main.py


Or run individual modules:

python3 Hadamard.py
python3 qiskit-test.py
python3 qutip-rabi.py

For best results: run this in visual studio code, vs codium or pycharm.

📈 Outputs & Visualizations
Quantum circuit diagrams
Statevector evolution
Bloch sphere representations
Rabi oscillation plots
Photoluminescence spectra
Animated quantum rotations (.gif)

🎓 Intended Audience
This project is suitable for:
Physics students
Computational physics learners
Quantum computing enthusiasts
Researchers exploring quantum simulations

A working knowledge of linear algebra and quantum mechanics is recommended.

🚀 Future Work
Add noise models and decoherence
Extend to multi-particle quantum systems
Implement VQE and quantum algorithms
GPU acceleration for large simulations
Improved documentation and notebooks

📜 License
This project is released under the MIT License.

👤 Author
Elvis Wanjiru
Physics | Computational & Quantum Simulations.