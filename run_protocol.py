from initialization import initialize
from transmission import transmit
from sifting import sift_and_correct
from encryption import text_to_binary, binary_to_text, xor_encrypt

def format_bases(bases):
    return ['Z' if base == 0 else 'X' for base in bases]

def main():
    # Use a small number for clarity
    alice_bits, alice_bases, bob_bases = initialize(10)
    bob_results = transmit(alice_bits, alice_bases, bob_bases)

    print("Alice's bits:   ", alice_bits)
    print("Alice's bases:  ", format_bases(alice_bases))
    print("Bob's bases:    ", format_bases(bob_bases))
    print("Bob's results:  ", bob_results)

    try:
        matching_indices, secret_key, qber = sift_and_correct(alice_bits, alice_bases, bob_bases, bob_results)
        print("Matching indices:", matching_indices)
        print("Shared key:      ", secret_key)

        message = "bob how are you"
        binary_message = text_to_binary(message)

        encrypted_binary = xor_encrypt(binary_message, secret_key)
        decrypted_binary = xor_encrypt(encrypted_binary, secret_key)
        decrypted_message = binary_to_text(decrypted_binary)

        encrypted_readable = binary_to_text(encrypted_binary[:len(binary_message)])

        print("\nOriginal Message: ", message)
        print("Encrypted Message: ", encrypted_readable)
        print("Decrypted Message: ", decrypted_message)

    except ValueError as e:
        print("Key exchange failed:", e)

if __name__ == "__main__":
    main()
