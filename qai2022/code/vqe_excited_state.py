import tequila as tq
import numpy
from tequila.hamiltonian.paulis import X,Y,Z

H = 1.5-0.5*(Z(1)-Z(0)+Z(0)*Z(1)+X(1)-Z(0)*X(1))


a = tq.Variable("a")
U = tq.gates.Ry(angle=a*numpy.pi,target=0)
U+= tq.gates.CNOT(0,1)
U+= tq.gates.Ry(angle=(a/2)*numpy.pi, target=1)

U.export_to(filename="circuit.png")

from matplotlib import pyplot as plt

E = tq.ExpectationValue(H=H, U=U)
red = (E-1.0)**2

blue = tq.ExpectationValue(H=(H-1)**2, U=U)

U0 = U.map_variables({"a":-1.0})
S = tq.ExpectationValue(H=tq.paulis.Projector("|00>"), U=U+U0.dagger())
green = E + 10*S

f0 = tq.compile(E)
f1 = tq.compile(red)
f2 = tq.compile(blue)
f3 = tq.compile(green)
x=[]
y0=[]
y1=[]
y2=[]
y3=[]
for a in numpy.linspace(-2.4, 2.4, 100):
    x.append(a)
    y0.append(f0({"a":a}))
    y1.append(f1({"a":a}))
    y2.append(f2({"a":a}))
    y3.append(f3({"a":a}))

plt.plot(x,y0,color="navy", label=r"$\langle H\rangle$")
plt.xlabel("a")
plt.legend()
plt.savefig("vqe_example.png")
plt.figure()

plt.plot(x,y1,color="tab:red", label=r"$(\langle H \rangle-1)^2$")
plt.legend()
plt.savefig("red.png")
plt.figure()
plt.plot(x,y2,color="tab:blue", label=r"$\langle (H-1)^2 \rangle$")
plt.legend()
plt.savefig("blue.png")
plt.figure()
plt.plot(x,y3,color="tab:green", label=r"$\langle H  \rangle - |\langle H_0 \rangle_{U(a)U^\dagger(0)}|^2$")
plt.legend()
plt.savefig("green.png")
plt.figure()

