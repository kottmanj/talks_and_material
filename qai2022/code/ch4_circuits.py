import tequila as tq

mol = tq.Molecule(geometry="ch4.xyz")

lqm = mol.local_qubit_map() # sorts the SPA qubits, looks nicer, soon the degfault
# do: H = H.map_qubits(lqm) and U = U.map_qubits(lqm)
# if you want to use it
# we just do it for nicer plots here

U = mol.make_ansatz("SPA")
U.map_qubits(lqm).export_to(filename="circuit_spa.png")

U = mol.make_ansatz("SPA+S")
print(U)
tq.compile_circuit(U.map_qubits(lqm), exponential_pauli=False).export_to(filename="circuit_spa_gs.png")

U = mol.make_ansatz("SPA")
U += tq.gates.QubitExcitation("a", [2,3,4,5])
U += tq.gates.Ry(angle="b",target=0) + tq.gates.CNOT(0,1)
U.map_qubits(lqm).export_to(filename="circuit_spa_custom.png")

