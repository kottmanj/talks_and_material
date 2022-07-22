# Required Dependencies:
# Madness from fork: github.com/kottmanj/madness (see readme for installation instruction)
# PySCF: pip install pyscf | alternative: psi4
# Not necessary but recommended (tq.minimize will be much faster):
# Qulacs: pip install qulacs
import tequila as tq

mol = tq.Molecule(geometry="ch4.xyz")

# as the UpCCD ansatz does not leave the "Hardcore-Boson" sector
# we will apply this (to save time)
# just attach "HCB" to the ansatz
# and use the hardcore_boson_hamiltonian
# the result is the same as with UpCCD and normal hamiltonian (feel free to try)

H = mol.make_hardcore_boson_hamiltonian()
U = mol.make_ansatz(name="HCB-UpCCD")
E = tq.ExpectationValue(H=H, U=U)
result = tq.minimize(E)
print("{} orbitals ".format(mol.n_orbitals))
fci = mol.compute_energy("fci")
print("VQE/MRA-PNO : {:+2.4f}".format(result.energy))
print("FCI/MRA-PNO : {:+2.4f}".format(fci))

# now some basis set comparissons
mol1 = tq.Molecule(geometry="ch4.xyz", basis_set="sto-3g")
H1 = mol1.make_hardcore_boson_hamiltonian()
U1 = mol1.make_ansatz("HCB-UpCCD") # similar to SPA
E1 = tq.ExpectationValue(H=H1,U=U1)
result1 = tq.minimize(E1, silent=True)
print("{} orbitals ".format(mol1.n_orbitals))
fci1 = mol1.compute_energy("fci")
print("VQE/STO-3G : {:+2.4f}".format(result1.energy))
print("FCI/{} : {:+2.4f}".format("STO-3G", fci1))

# one larger basis set
basis_set="6-31G"
mol2 = tq.Molecule(geometry="ch4.xyz", basis_set=basis_set)
print("{} orbitals ".format(mol2.n_orbitals))
fci2 = mol2.compute_energy("fci")
print("FCI/{} : {:+2.4f}".format(basis_set, fci2))

