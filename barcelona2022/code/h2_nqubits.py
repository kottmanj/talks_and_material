import tequila as tq

basis_set="sto-3g" # for 8 qubits example: 6-31G
R = 1.5 # change as you like
geom="H 0.0 0.0 0.0\nH 0.0 0.0 {}"

mol = tq.Molecule(geometry=geom.format(R), basis_set=basis_set)
fci = mol.compute_energy("fci")
U = mol.make_ansatz(name="SPA", edges=[(0,1)])
H = mol.make_hamiltonian()
E = tq.ExpectationValue(H=H, U=U)

# adapt options for arbitrary accuracy
result = tq.minimize(E, silent=True)
print(fci-result.energy)

# optimize orbitals
# don't have a good guess for arbitary basis .... hoping random around zero is fine
# for arbitrary accuracy you might need to play with the thresholds
opt = tq.chemistry.optimize_orbitals(circuit=U, molecule=mol, silent=True, initial_guess="random_loc=0.0_scale=1.0")
# a few bonus iterations (default is not so much)
opt = tq.chemistry.optimize_orbitals(circuit=U, molecule=opt.molecule, silent=True)
print(fci-opt.energy)
