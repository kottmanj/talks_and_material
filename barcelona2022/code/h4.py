import tequila as tq
import numpy

geom="h 0.0 0.0 0.0\nh 0.0 0.0 1.5\nh 0.0 0.0 3.0\nh 0.0 0.0 4.5"
mol = tq.Molecule(geometry=geom, basis_set="sto-3g")
fci = mol.compute_energy("fci")
# transform to (orthogonalized) atomic orbitals
# makes guess for optimization easier
mol = mol.orthonormalize_basis_orbitals()

# orbital guess
guess = numpy.eye(4)
guess[0] = [1,1,0,0]
guess[1] = [1,-1,0,0]
guess[2] = [0,0,1,1]
guess[3] = [0,0,1,-1]

# optimize orbitals
U = mol.make_ansatz(name="SPA", edges=[(0,1), (2,3)])
opt = tq.chemistry.optimize_orbitals(molecule=mol, circuit=U, initial_guess=guess.T, silent=True)

print("SPA error: {:2.5f}".format(opt.energy - fci))

# update molecule
mol = opt.molecule
H = mol.make_hamiltonian()
E = tq.ExpectationValue(H=H, U=U)
result = tq.minimize(E, silent=True)
print(opt.energy)
print(result.energy)

# constuct SPA+ circuit
a = tq.Variable("a")
b = tq.Variable("b")
UR = mol.make_excitation_gate(indices=[(0,2)], angle=(a+0.5)*numpy.pi)
UR+= mol.make_excitation_gate(indices=[(1,3)], angle=(a+0.5)*numpy.pi)
UR+= mol.make_excitation_gate(indices=[(4,6)], angle=(a+0.5)*numpy.pi)
UR+= mol.make_excitation_gate(indices=[(5,7)], angle=(a+0.5)*numpy.pi)
UR+= mol.make_excitation_gate(indices=[(2,4)], angle=(b+0.5)*numpy.pi)
UR+= mol.make_excitation_gate(indices=[(3,5)], angle=(b+0.5)*numpy.pi)

# more efficient to use a qubit excitation
# see tq tutorial on graph circuits
UC = mol.make_excitation_gate(indices=[(2,4),(3,5)], angle="d")

UG = U + UR + UC + UR.dagger()
E = tq.ExpectationValue(H=H, U=UG)
result2 = tq.minimize(E, silent=True, initial_values=result.variables)
print("SPA+ error: {:2.5f}".format(result2.energy - fci))

"""
Output looks like:
SPA error: 0.01626
-1.9798878845402021
-1.979887884540202
SPA+ error: 0.00845
"""
