import tequila as tq
from tequila.hamiltonian.paulis import X,Y,Z
from tequila.circuit.gates import Ry, ExpPauli, CNOT
import numpy

H = H = 1.5-0.5*(Z(1)-Z(0)+Z(0)*Z(1)+X(1)-Z(0)*X(1))

# create the circuit U (from the slides)
U = Ry("x", 0) + Ry("xx", 0, control=2) + CNOT(0,1) + Ry("y", 1) + Ry("yy", 1, control=2)
U.export_to(filename="circuit_state_prep.png")

E0 = tq.ExpectationValue(H=H, U=U)
E1 = tq.ExpectationValue(H=H, U=tq.gates.X(2)+U)
objective = E0 - E1
result = tq.minimize(objective, initial_values="near_zero")

variables = result.variables

# lets try
Uf = Ry(tq.Variable("control")*numpy.pi, 2)
Uf+= U.map_variables(result.variables)
f = tq.ExpectationValue(H=H, U=Uf)
f = tq.compile(f)
print("f(0) = {:+2.2f} -- should be 0".format(f({"control":0.0})))
print("f(1) = {:+2.2f} -- should be 3".format(f({"control":1.0})))

Uf.export_to(filename="circuit_uf.png")

# plot all energies (resulting from superpositions of e0 and e1
from matplotlib import pyplot as plt
x=list(numpy.linspace(0.0,1.0,25))
y=[f({"control":xx}) for xx in x]
plt.plot(x,y,label=r"$\langle H \rangle_{U_f(x)}$", color="navy")
plt.legend()
plt.savefig("state_preparation_energies.png")

print(f)
f_opt = tq.ExpectationValue(H=H, U=Uf, optimize_measurements=True)
print(f_opt)
