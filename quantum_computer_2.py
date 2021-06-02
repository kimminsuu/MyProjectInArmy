from qiskit import QuantumCircuit, execute, Aer
from qiskitt.visualization import plot_histogram
circuit = QuantumCircuit(1,1)
circuit.h(0)
circuit.measure([0], [0])
circuit.draw()

from qiskit.visualization import plot_bloch_multivector
backend = Aer.get_backend9'statevector_simulator')
result = execute(circuit, backend).result()
states = result.get_statevector()
print(states)
plot_bloch_multivector(states)

#U-Gate
from numpy import pi
circuit = QuantumCircuit(1, 1)
thet, phi, lamb = pi/4, pi/4, 0
circuit.u(thet, phi, lamb, 0)
circuit.measure([0], [0])
circuit.draw()

