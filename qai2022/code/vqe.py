import tequila as tq
import numpy
from tequila.hamiltonian.paulis import X,Y,Z

H = 1.5-0.5*(Z(1)-Z(0)+Z(0)*Z(1)+X(1)-Z(0)*X(1))

a = tq.Variable("a")
U = tq.gates.Ry(angle=a*numpy.pi,target=0)
U+= tq.gates.CNOT(0,1)
U+= tq.gates.Ry(angle=(a/2)*numpy.pi, target=1)

E = tq.ExpectationValue(H=H, U=U)

result = tq.minimize(E, initial_values="random")

v,vv = numpy.linalg.eigh(H.to_matrix())

for i in range(len(v)):
    wfn=tq.QubitWaveFunction(vv[:,i])
    print("E({})={:+2.1f}, wfn=".format(i,v[i]), wfn)
