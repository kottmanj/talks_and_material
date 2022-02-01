import tequila as tq
import time

start=time.time()
# dependencies needed: Psi4 or PySCF
geometry = "H 0.0 0.0 0.0\nH 0.0 0.0 1.23\nH {R} 0.0 0.0\nH {R} 0.0 1.23"
mol = tq.Molecule(geometry=geometry.format(R=1.0), basis_set="sto-3g")
H = mol.make_hamiltonian()
U0 = mol.make_upccgsd_ansatz(name="UpCCGSD")
# ground state opt
E0 = tq.ExpectationValue(H=H, U=U0)
result0 = tq.minimize(E0)
U0_opt = U0.map_variables(result0.variables)
# start from CIS (see ChemicalScience SI)
U1 = tq.gates.X([0,1,2,3,4])
U1 += tq.gates.H(2) 
U1 + tq.gates.CNOT(2,3)
U1 + tq.gates.CNOT(2,4)
U1 + tq.gates.CNOT(2,5)
# excited state ansatz (CIS + UpCCGSD)
U1 = U1 + mol.make_upccgsd_ansatz(name="UpCCGSD", include_reference=False)
E1 = tq.ExpectationValue(H=H, U=U1)
P0 = tq.paulis.Qp(U1.qubits) #same as |0><0|
S = tq.ExpectationValue(H=P0, U=U1+U0_opt.dagger())
f_ex = E1 - result0.energy*S
result1 = tq.minimize(f_ex)

print("vqe ground state : {:+2.4f}".format(result0.energy))
print("vqe excited state: {:+2.4f}".format(result1.energy))
print("walltime: {:2}s".format(time.time()-start))
