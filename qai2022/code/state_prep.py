import tequila as tq
from tequila.hamiltonian.paulis import X,Y,Z
from tequila.circuit.gates import Ry, ExpPauli, CNOT
import numpy

H = H = 1.5-0.5*(Z(1)-Z(0)+Z(0)*Z(1)+X(1)-Z(0)*X(1))

n_layers=1
U = Ry("x", 0) + Ry("xx", 0, control=2) + CNOT(0,1) + Ry("y", 1) + Ry("yy", 1, control=2)
U.export_to(filename="circuit_state_prep.png")

a = tq.Variable("a")
U0 = Ry(angle=a*numpy.pi, target=0) + CNOT(0,1) + Ry(angle=(a/2)*numpy.pi, target=1)

# find GS of H
E = tq.ExpectationValue(H=H,U=U0)
result0 = tq.minimize(E, initial_values=-0.5)
# find GS of -H
result1 = tq.minimize(-E, initial_values=1.5)

# initialize the circuit that prepare those two states with fixed variables
U_GS0 = U0.map_variables(result0.variables)
U_GS1 = U0.map_variables(result1.variables)

# now the training objective 
P000 = tq.paulis.Projector("|000>")
P001 = tq.paulis.Projector("|001>")
E0 = tq.ExpectationValue(H=P000, U=U+U_GS0.dagger()) 
E1 = tq.ExpectationValue(H=P001, U=tq.gates.X(2)+U+U_GS1.dagger())
(U+U_GS1.dagger()).export_to(filename="circuit2.png")

vector = tq.QTensor([E0, E1], shape=(2,))
weights = numpy.asarray([-1.0, -1.0])

objective = vector.dot(weights)

result = tq.minimize(objective, initial_values=0.0)

for _ in range(4):
    trial = tq.minimize(objective, initial_values="random")
    if trial.energy < result.energy:
        result=trial

variables = result.variables

# lets try
Etest0 = tq.ExpectationValue(H=H, U=U)
Etest1 = tq.ExpectationValue(H=H, U=tq.gates.X(2)+U)
e0 = tq.compile(Etest0)
e1 = tq.compile(Etest1)
print("energy with |0> in last qubit: {:+2.2f} -- expecting 0".format(e0(variables=variables)))
print("energy with |1> in last qubit: {:+2.2f} -- expecting 3".format(e1(variables=variables)))



