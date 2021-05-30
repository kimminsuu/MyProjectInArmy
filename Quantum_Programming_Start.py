#양자컴퓨팅. 0과1이 정해진 기존 컴퓨터와 달리, 0과1이 정해지지 않은 상태로 통신을 하고 확인하는 순간 결정이 되는 양자역학 이론을 이용한 기술.
#양자컴퓨팅이 활성화되어 쓰일 경우 슈퍼컴퓨터로 1만년간 계산할 것을 200초안에 끝낼 수 있을 정도의 처리속도가 가능해진다고 함.

#파이썬의 qiskit이라는 모듈이 있음
%matplotlib inline
from qiskit import QuantumCircuit, execute, Aer
from quskit.visualization import plot_histogram

circuit = QuantumCircuit(2, 2)
circuit.x(0)
circuit.h(1)
circuit.measure([0,1],[0,1])
circuit.draw()

backend = Aer.get_backend('qasm_simulator')
results = execute(circuit, backend).result()
counts = results.get_counts()
print(counts)
plot_histogram(counts)
