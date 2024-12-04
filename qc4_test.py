import qc4
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Statevector, Operator
import numpy as np
import qiskit.quantum_info as qi
import random

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_generic_difussor():
    """ Tests test_generic_difussor. This will send randomly generated
    oracles and expects the correct result.

    Args: 
        None
    """

    for n in range(2,9):
        N=2**n
        oracle=np.identity(N)
        index=random.randint(0, N-1)
        oracle[index][index]=-1
        intended_statevactor=np.zeros(N)
        intended_statevactor[index]=1
        found=qc4.generic_difussor(oracle,n)
        assert Statevector(Statevector(intended_statevactor)).equiv(found, atol=0.09)

    print("SUCCESSFUL TEST")


##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
if __name__ == '__main__':
    """ Run this to verify if tests are failing"""

    test_generic_difussor()




