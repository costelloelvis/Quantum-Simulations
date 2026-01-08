Quantum Simulations of Quantum Gates, Time Evolution, and Quantum Dot Phenomena

Elvis Wanjiru
Department of Physics
Computational & Quantum Simulations

Abstract

We present a collection of numerical simulations exploring fundamental concepts in quantum mechanics and quantum computing, implemented using modern Python-based scientific libraries. The project integrates simulations of quantum gates, multi-qubit circuits, quantum state evolution, and OpenQASM-defined circuits, alongside physically motivated models such as Rabi oscillations, Auger recombination, quantum-dot photoluminescence, and the Quantum Confined Stark Effect (QCSE). By combining statevector methods, operator-based dynamics, and circuit-level simulations, this work provides a unified computational framework for both quantum information science and condensed-matter–inspired quantum systems.

1. Introduction

Quantum mechanics underpins modern technologies ranging from semiconductors to quantum computers. Numerical simulations play a critical role in understanding quantum systems where analytical solutions are limited or impractical. In parallel, the development of quantum computing frameworks such as Qiskit has enabled high-level abstractions for simulating and implementing quantum algorithms.

This work aims to bridge computational quantum physics and quantum information processing by providing a modular simulation framework that includes both circuit-based quantum computing models and physically motivated quantum dynamical systems. The project is designed to support learning, experimentation, and exploratory research in quantum science.

2. Computational Framework

All simulations are implemented in Python 3, leveraging well-established numerical and quantum libraries:

NumPy and SciPy for linear algebra and numerical computations

Matplotlib for visualization

Qiskit for quantum circuit construction and simulation

QuTiP for solving time-dependent and open quantum systems using master-equation approaches

OpenQASM for circuit-level quantum descriptions

The modular structure allows individual simulations to be executed independently or combined into more complex workflows.

3. Quantum Gate and Circuit Simulations

The project includes implementations of fundamental quantum gates, such as the Hadamard, CNOT, and CCNOT (Toffoli) gates. These gates are represented both as matrix operators acting on statevectors and as circuit elements within the Qiskit framework.

Multi-qubit circuits are explored through explicit statevector evolution and Qiskit-based simulations. OpenQASM files are included to demonstrate hardware-agnostic circuit descriptions and low-level quantum instruction sets.

4. Quantum State Evolution and Dynamics

Time evolution of quantum systems is investigated using both analytical operator methods and numerical solvers. Rabi oscillations in two-level systems are simulated to illustrate coherent driving and population dynamics.

For more complex systems, QuTiP’s mesolve is employed to solve the Schrödinger and master equations, enabling simulations of driven qubits and time-dependent Hamiltonians.

5. Quantum Dot and Semiconductor-Inspired Models

Beyond quantum information, the project explores quantum-dot physics, including:

Photoluminescence spectra of quantum dots

Auger recombination decay processes

Quantum Confined Stark Effect (QCSE) under applied electric fields

These simulations are motivated by nanoscale semiconductor physics and provide insight into how confinement and external fields modify electronic and optical properties.

6. Visualization and Output

Simulation outputs include:

Quantum circuit diagrams

Statevector evolution plots

Bloch sphere representations

Rabi oscillation dynamics

Photoluminescence spectra

Animated visualizations of quantum rotations

These visualizations enhance conceptual understanding and support qualitative analysis of quantum behavior.

7. Intended Applications

The framework is suitable for:

Undergraduate and postgraduate physics education

Computational physics coursework

Introductory quantum computing studies

Exploratory research in quantum simulations

Prototyping quantum algorithms and physical models

A foundational understanding of linear algebra and quantum mechanics is assumed.

8. Future Work

Planned extensions include:

Incorporation of noise models and decoherence

Simulation of multi-particle and interacting quantum systems

Implementation of variational quantum algorithms (e.g., VQE)

GPU acceleration for large-scale simulations

Expanded documentation and Jupyter notebook tutorials

9. Availability and Reproducibility

The complete source code is publicly available in a GitHub repository and is distributed under the MIT License. All simulations are reproducible using open-source software and standard Python environments.

10. Conclusion

This project demonstrates a unified approach to simulating both quantum information systems and physically motivated quantum phenomena. By combining circuit-based methods with numerical quantum dynamics, it serves as a versatile platform for education, experimentation, and early-stage research in quantum science.

Keywords

Quantum simulation, quantum computing, Qiskit, QuTiP, OpenQASM, quantum dots, Rabi oscillations, QCSE
