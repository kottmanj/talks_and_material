#dependencies
# pip install tequila-basic
# pip install pyscf
# conda install madtequila -c kottmann 
# recommended
# pip install qulacs
import tequila as tq
import numpy

# R=1.5 is equilibrium while R=5.0 is atomic
# we do atomic because there will be differences in the methods
# change to 1.5 to see that all energies are close
R1=5.0
R2=5.0 + 1.e-4 # small perturbation to break degeneracy and have consistent orbital ordering in this example
geom = "be 0.0 0.0 0.0\nH 0.0 0.0 {}\nH 0.0 0.0 -{}".format(R1,R2)

# initialize molecule and Hamiltonian
mol = tq.Molecule(geometry=geom)
H = mol.make_hamiltonian()
fci = mol.compute_energy("fci")

# initialize circuit
U = mol.make_ansatz(name="SPA")
# initialize expectationvalue and optimize cirucit paraemters
E = tq.ExpectationValue(H=H, U=U)
result = tq.minimize(E, silent=True)
print("SPA Error: {:+2.5f}".format(result.energy-fci))

# optimize orbitals
# guess assumes orbitals (1,1) (2,2) (1,1) (2,2)
# where (x,x) denotes PNO pairs (see SPA paper)
# do print(mol) to see how they are ordered (might change position due to degeneracies)
guess = numpy.eye(4)
guess[0] = [1,0,1,0]
guess[0] = [0,1,0,1]
guess[0] = [1,0,-1,0]
guess[0] = [0,1,0,-1]

opt = tq.chemistry.optimize_orbitals(circuit=U, molecule=mol, initial_guess=guess.T, silent=True)
print("OO-SPA Error: {:+2.5f}".format(opt.energy-fci))

# UpCCGSD
U = mol.make_ansatz(name="UpCCGSD")
E = tq.ExpectationValue(H=H, U=U)
# start from SPA state and from random 
result = tq.minimize(E, silent=True, initial_values=result.variables)
print("UpCCGSD Error: {:+2.5f}".format(result.energy-fci))
result = tq.minimize(E, silent=True, initial_values="random")
print("UpCCGSD Error: {:+2.5f}".format(result.energy-fci))

"""
Output will look like this:
SPA Error: +0.20216
OO-SPA Error: +0.00004
UpCCGSD Error: +0.00004
UpCCGSD Error: +0.00004
"""

