# Hamiltonian matrix
import numpy as np

def hamiltonian_matrix(deltax,potentialvalues):
    potentialvalues=np.array(potentialvalues,dtype=float)
    if deltax <= 0:
        raise ValueError("deltax must be greater than 0")
    if potentialvalues.ndim != 1:
        raise ValueError("potentialvalues must be one dimensional")
    if potentialvalues.size == 0:
        raise ValueError("potentialvalues cant be empty")

    n = len(potentialvalues)

    maindiag = 1/(deltax)**2 + potentialvalues
    offdiag = np.full(n-1,-1/2*(deltax)**2)

    hamiltonian = (np.diag(maindiag)+np.diag(offdiag,k=1)+np.diag(offdiag,k=-1))
    return hamiltonian