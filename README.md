# Quantum Simulations

A collection of **quantum mechanics**, **quantum computing**, and **computational physics** simulations implemented in Python.

This repository combines numerical modeling of quantum systems with quantum circuit simulations, covering topics from fundamental quantum gates to quantum-dot physics and time-dependent quantum dynamics.

## Features

* Quantum gate implementations (Hadamard, CNOT, CCNOT/Toffoli)
* Multi-qubit statevector simulations
* Quantum circuits using Qiskit
* OpenQASM circuit execution and parsing
* Rabi oscillations and qubit dynamics
* Time evolution of quantum systems with QuTiP
* Quantum-dot photoluminescence simulations
* Quantum Confined Stark Effect (QCSE) modeling
* Auger recombination decay simulations
* Quantum visualization tools and animations

---

## Repository Structure

```text
Quantum-Simulations/
│
├── tests/
│   └── bc_test.py
│
├── calculator.py
├── 3D-Hadamard.py
├── Auger-Recombination-Decay.py
├── block_rotation.py
├── block_rotation.gif
├── cc_gate.py
├── CNOT_gate.py
├── cnot.py
├── cnot_gate_11_qubits.py
├── controlled_NOT_gate.py
├── Hadamard.py
├── main.py
├── qas.py
├── qsm.py
├── statevector.py
├── Qiskit-Circuit.py
├── qiskit-test.py
├── qubit-mesolve.py
├── quip-rabi.py
├── dimple_qasm.qasm
├── qasm_test.qasm
├── Circuit.png
├── README.md
│
├── PL_of_Quantum_Dots_*.py
└── Quantum_Confined_Stark_Effect_*.py
```

---

## Topics Covered

### Quantum Computing

* Qubits and statevectors
* Hadamard transformations
* Controlled-NOT (CNOT) gates
* Toffoli (CCNOT) gates
* Multi-qubit systems
* Quantum circuit simulation
* OpenQASM workflows
* Quantum circuit visualization

### Quantum Physics

* Rabi oscillations
* Time-dependent Schrödinger evolution
* Quantum state dynamics
* Quantum-dot photoluminescence
* Quantum Confined Stark Effect (QCSE)
* Auger recombination processes

---

## Technologies Used

* Python 3
* NumPy
* SciPy
* Matplotlib
* Qiskit
* QuTiP
* OpenQASM

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/costelloelvis/Quantum-Simulations.git
cd Quantum-Simulations
```

### Create a Virtual Environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install numpy scipy matplotlib qiskit qutip
```

Or, if available:

```bash
pip install -r requirements.txt
```

---

## Running Simulations

Run the main program:

```bash
python main.py
```

Run individual simulations:

```bash
python Hadamard.py
python qiskit-test.py
python qubit-mesolve.py
python quip-rabi.py
```

---

## Example Outputs

The simulations can generate:

* Quantum circuit diagrams
* Statevector visualizations
* Bloch sphere representations
* Rabi oscillation plots
* Quantum-dot spectra
* Animated quantum rotations
* OpenQASM circuit results

---

## Educational Applications

This repository is suitable for:

* Physics students
* Computational physics learners
* Quantum computing enthusiasts
* Undergraduate research projects
* Researchers exploring quantum simulations

A basic understanding of:

* Linear Algebra
* Quantum Mechanics
* Python Programming

is recommended.

---

## Future Development

Planned improvements include:

* Noise models and decoherence simulations
* Variational Quantum Eigensolver (VQE)
* Quantum optimization algorithms
* Multi-particle quantum systems
* GPU-accelerated simulations
* Interactive Jupyter notebooks
* Improved documentation and tutorials

---

## Contributing

Contributions, bug reports, and feature requests are welcome.

Feel free to fork the repository and submit pull requests.

---

## License

This project is released under the MIT License.

---

## Author

**Elvis Wanjiru**

Physics • Computational Physics • Quantum Computing

GitHub: https://github.com/costelloelvis

*"Exploring quantum systems through simulation, computation, and visualization."*
