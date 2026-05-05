from qiskit import QuantumCircuit
from qiskit.circuit import Qubit

qc = QuantumCircuit(2)
qc.x(0)
qc.h(0)

print(type(qc.data[0].qubits))
print(qc.data[0].qubits[0])
print(type(qc.data[0].qubits[0]._index))
