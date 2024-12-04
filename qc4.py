from qiskit import QuantumCircuit,  QuantumRegister
from qiskit.quantum_info import Statevector
from math import pi
import qiskit
import numpy as np
import qiskit.quantum_info as qi
from qiskit.extensions import UnitaryGate

def generic_difussor(oracle, n):
    """
    Use the oracle passed as an argument to create the oracle gate.
    Hint: 
        gateOracle = UnitaryGate(oracle)
        gateOracle.name = "Oracle" 
    
    Next, create the diffuser matrix using the formula for the diffuser: 
        2|s⟩⟨s| - 𝟙 
    Note that 𝟙 is the identity matrix of the corresponding dimensions, 
    and 's' represents the 'n' qubits in superposition. In other words, 
    each qubit passes through an H gate. However, you don't need to use gates 
    to create this matrix; you can directly construct the matrix by:
        1. Generating a matrix of ones using `np.ones((N, N))`.
        2. Multiplying it by the '2' in the formula.
        3. Adding another term derived from analyzing the formula.
        4. Subtracting the corresponding identity matrix. 
    
    Once you have the diffuser matrix, create the diffuser gate in a manner 
    similar to how you created the oracle gate.
    
    The input to this algorithm is the oracle, which contains the hidden value 
    to search for. Note that the oracle is not the starting point of the circuit. 
    The circuit begins with H gates on each qubit, which are applied outside 
    the iteration loop. 
    
    Then, in a loop that iterates `int((π/4) * sqrt(N))` times, you apply 
    the oracle gate followed by the diffuser gate. After completing all iterations, 
    obtain the state vector and return it. This state vector corresponds to the 
    number you were searching for.
    
    **Important Notes:**
    1. The `int()` in the number of iterations simply applies the floor function.
    2. The number of iterations is slightly less than `sqrt(N)` because `π/4` is 
       less than 1. Performing more iterations than necessary can lead to diverging 
       from the correct result. 
    
    Experiment by printing all intermediate values to understand how the algorithm behaves!
    
    Args: 
        oracle: An oracle with the "hidden" value to search for.
        n: The number of qubits.
    
    Returns: 
        qiskit.quantum_info.Statevector.from_instruction(grover_circuit)
    """
    gateOracle = UnitaryGate(oracle)
    gateOracle.name = "Oracle"

    N = 2**n

    ket_s = (1/np.sqrt(N))*np.ones((N, 1))
    bra_s = ket_s.transpose()

    difusser_matrix = 2*(ket_s*bra_s) - np.identity(N)

    gateDifusser = UnitaryGate(difusser_matrix)
    gateDifusser.name = "Difusser"

    iterations = int((pi/4) * np.sqrt(N))

    qr = QuantumRegister(n)
    qc = QuantumCircuit(qr)

    qc.h(qr)
    
    for i in range(iterations):

        qc.append(gateOracle, qr)
        qc.append(gateDifusser, qr)
    
    return Statevector(qc)