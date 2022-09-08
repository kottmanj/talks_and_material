import tequila as tq
import numpy
from matplotlib import pyplot as plt

a = tq.Variable("a")
f = (-a**2).apply(tq.numpy.exp)

U = tq.gates.Ry(angle=f*numpy.pi, target=0)
U += tq.gates.CNOT(0,1)

U.export_to(filename="circuit_example.png")
U.export_to(filename="circuit_example_x.png", style="standard")

H = tq.paulis.from_string("-1.0*X(0)X(1)+0.5*Z(0)+Y(1)")

E = tq.ExpectationValue(H=H, U=U)
dE = tq.grad(E, "a")

L = E + (-dE**2).apply(tq.numpy.exp)

L = tq.compile(L)

H2 = tq.paulis.X(0)+tq.paulis.X(1)+tq.paulis.X([0,1])
U2 = tq.gates.Ry(angle=L*numpy.pi, target=0)
U2 += tq.gates.CNOT(0,1)
E2 = tq.ExpectationValue(H=H2, U=U2)

F = E2.apply(tq.numpy.sin)
F = tq.compile(F)

x=[]
y=[]
for a in numpy.linspace(-5,5,300):
    x.append(a)
    y.append(F(variables={"a":a}))

plt.plot(x,y,color="navy", linewidth=2.0)
plt.legend()
plt.xlabel("a")
plt.ylabel("F(a)")

plt.savefig("plot_F.png")
plt.show()

