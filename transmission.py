# transmission.py
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def transmit(alice_bits, alice_bases, bob_bases):
    bob_results = []
    simulator = AerSimulator()

    for i in range(len(alice_bits)):
        qc = QuantumCircuit(1, 1)
        
        # Alice's preparation of qubit
        if alice_bases[i] == 0:
            if alice_bits[i] == 1:
                qc.x(0)  # Apply X gate (bit flip)
        else:
            if alice_bits[i] == 1:
                qc.x(0)  # Apply X gate (bit flip)
            qc.h(0)  # Apply Hadamard gate to create superposition

        # Bob's measurement
        if bob_bases[i] == 1:
            qc.h(0)  # Apply Hadamard gate if Bob's base is 1
        qc.measure(0, 0)

        # Run the quantum circuit with the simulator
        job = simulator.run(qc, shots=1, memory=True)
        result = job.result()
        measured_bit = int(result.get_memory()[0])  # Get the measured bit

        bob_results.append(measured_bit)

    return bob_results
