import tequila as tq
import numpy

X=tq.paulis.X
Y=tq.paulis.Y
Z=tq.paulis.Z

H = X(0)*Y(1) + 0.5*Z(0)

U = tq.gates.Ry(angle="a", target=0)
U += tq.gates.CNOT(0,1)

U.export_to(filename="circuit.png")

UX = tq.gates.Ry(angle=1.0, target=0)+tq.gates.Rx(angle=1.0, target=1)
UX.export_to(filename="circuitx.png")

E = tq.ExpectationValue(H=H, U=U)
E2 = tq.ExpectationValue(H=H, U=U, optimize_measurements=True)
print(E2)


for a in [0.0, 1.0, 2.0]:
    print(tq.simulate(E, variables={"a":a}))

from matplotlib import pyplot as plt

E = tq.compile(E, backend="cirq")
x = []
y1 = []
y2 = []
y3 = []
y4 = []
for a in numpy.linspace(0.0, numpy.pi*4, 100):
    y1.append(E(variables={"a":a}))
    y2.append(E(variables={"a":a}, samples=100))
    y3.append(E(variables={"a":a}, samples=1000))
    x.append(a)

plt.plot(x,y1, label=r"$\infty$ samples")
plt.plot(x,y2, label="100 samples")
plt.plot(x,y3, label="1000 samples")
plt.legend()
plt.savefig("plot.png")
plt.show()

