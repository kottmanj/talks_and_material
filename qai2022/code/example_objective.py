import tequila as tq
import numpy
from matplotlib import pyplot as plt

# if you are using the windows version:
# the command: a**2 and similar will give you trouble when taking the gradient
# the workaround is to always use .apply(f) where function uses tq.numpy primitives
# so instead of a**2 --> a.apply(tq.numpy.square)
# reason for this: windows version uses autograd and not jax

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

dL = tq.grad(L, "a")
dL2 = tq.grad(dL, "a")

L = tq.compile(L)
dL = tq.compile(dL)
dL2 = tq.compile(dL2)

x=[]
y0=[]
y1=[]
y2=[]
for a in numpy.linspace(-5,5,100):
    x.append(a)
    y0.append(L(variables={"a":a}))
    y1.append(dL(variables={"a":a}))
    y2.append(dL2(variables={"a":a}))

plt.plot(x,y0,color="navy", linewidth=2.0)
plt.legend()
plt.xlabel("a")
plt.ylabel("L(a)")

plt.savefig("plot_l.png")

plt.figure()
plt.plot(x,y0,color="navy", linewidth=2.0, label=r"$L$")
plt.plot(x,y1,color="tab:red", linewidth=2.0, label=r"$\frac{\partial L}{\partial a}$")
plt.plot(x,y2,color="tab:green", linewidth=2.0, label=r"$\frac{\partial^2 L}{\partial^2 a}$")
plt.legend()
plt.xlabel("a")

plt.savefig("plot_l2.png")


