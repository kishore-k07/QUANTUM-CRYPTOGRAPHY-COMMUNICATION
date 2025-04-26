# key_sifting.py
def sift_and_correct(alice_bits, alice_bases, bob_bases, bob_results):
    matching_indices = [i for i in range(len(alice_bases)) if alice_bases[i] == bob_bases[i]]
    
    if not matching_indices:
        raise ValueError("No matching bases found. Cannot establish a shared key.")
    
    alice_key = [alice_bits[i] for i in matching_indices]
    bob_key = [bob_results[i] for i in matching_indices]
    qber = sum(1 for a, b in zip(alice_key, bob_key) if a != b) / len(alice_key)

    secret_key = [a for a, b in zip(alice_key, bob_key) if a == b]
    return matching_indices, secret_key, qber
