import tequila as tq

# dependencies: needs special fork of madness installed
# go to: https://github.com/kottmanj/madness and follow the instructions there
# if you are on a linux system it should work straight away
# with mac and windows the build script might need adaptions

mol = tq.Molecule(geometry="c2h6.xyz")
H_HCB = mol.make_hardcore_boson_hamiltonian()
U_HCB = mol.make_ansatz("HCB-SPA")
E = tq.ExpectationValue(H=H_HCB, U=U_HCB)
print(H_HCB.n_qubits)
result = tq.minimize(E)

