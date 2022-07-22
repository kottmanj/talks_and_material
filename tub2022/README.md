
# Variational Algorithms for Quantum Chemistry with Tequila
Recording of a talk I gave at the Chemistry-Departments seminar at TU Braunschweig, July 2022:  

[slides](tub.pdf)   

Some slides contain small code examples. These slides are taken from a Tequila tutorial that can be found [here](../qai2022/).    

These are the explicit files containing those examples (file names in the lower right corner of the corresponding slide):   
- [example_objective.py](../aqi2022/code/example_objective.py)
- [example_nested_objective](../qai2022/code/example_nested_objective.py)
- [ch4.py](../qai2022/code/ch4.py)  

Tequila codebase and tutorials can be found here (see also below for explicit links): [https://github.com/tequilahub](github.com/tequilahub).  

### Relevant Papers:
- Tequila Overview paper: [arxiv:2011.03057](https://arxiv.org/abs/2011.03057)
- Automatically Differentiable Unitary Coupled-Cluster: [arxiv:2011.05938](https://arxiv.org/abs/2011.05938) (applications to Adaptive Solvers and Excited States):
- Basis-Set-Free VQEs: [arxiv:2008.02819](https://arxiv.org/abs/2008.02819)
- Separable Pair Approximations: [arXiv:2105.03836](https://arxiv.org/abs/2105.03836) (compact and classically simulable quantum circuits)
- Directly Determined PNOs: [JCP:10.1063/1.5141880](https://aip.scitation.org/doi/abs/10.1063/1.5141880) (the machinery that runs in the back of the Basis-Set-Free VQE and the tequila madness interface - not on arxiv but I can send you the pdf :-))
- Overview of Unitary Coupled-CLuster: [arXiv:2109.15176](https://arxiv.org/abs/2109.15176)

### Relevant tequila tutorials (in NBViewer):  
- [basic usage](http://nbviewer.org/github/tequilahub/tequila-tutorials/blob/main/BasicUsage.ipynb): General how-to for tequila    
- [basis-set-free H2 toy code](http://nbviewer.org/github/tequilahub/tequila-tutorials/blob/main/ChemistryBasisSetFreeVQE.ipynb): Minimal qubit Hamiltonian of H2 in basis-set-free representation. If you don't have time and just want one molecule.  
- [SPA ansatz](http://nbviewer.org/github/tequilahub/tequila-tutorials/blob/main/ChemistrySeparablePairAnsatz.ipynb): Examples for the SPA ansatz and a collection of precomputed basis-set-free representations of molecules (if you don't want to compile madness).  
- [madness-interface](http://nbviewer.org/github/tequilahub/tequila-tutorials/blob/main/ChemistryMadnessInterface.ipynb): If you want to compute your own molecular orbitals from scratch.  
