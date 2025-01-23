import hashlib
import random
import string

def generate_random_string(length=32):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_hash():
    """Generate a random 32-character hash."""
    random_string = generate_random_string()
    hash_object = hashlib.sha256(random_string.encode())
    return hash_object.hexdigest()

def find_hash_with_two_zeros():
    """Generate hashes until one starts with two consecutive zeros."""
    for _ in range(1000):
        hash_value = generate_hash()
        if hash_value.startswith('00'):
            print(f"Found hash starting with '00': {hash_value}")
            return True
    print("No hash starting with '00' found in 1000 attempts.")
    return False

# Run the function and check if it passes
if find_hash_with_two_zeros():
    print("Test passed: Hash starting with '00' was found.")
else:
    print("Test failed: No hash starting with '00' was found.")