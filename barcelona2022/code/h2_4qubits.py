import tequila as tq

R = 1.5 # change as you like
geom="H 0.0 0.0 0.0\nH 0.0 0.0 {}"

mol = tq.Molecule(geometry=geom.format(R), basis_set="sto-3g")
fci = mol.compute_energy("fci")
H = mol.make_hamiltonian()

# manual circuit construction
U = tq.gates.X(0)
U+= tq.gates.Ry(angle="a", target=2)
U+= tq.gates.CNOT(2,0)
U+= tq.gates.CNOT(0,1)
U+= tq.gates.CNOT(2,3)

E = tq.ExpectationValue(H=H, U=U)

# adapt options for arbitrary accuracy
result = tq.minimize(E, silent=True)
print(fci-result.energy)
