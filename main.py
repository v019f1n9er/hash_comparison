import hashlib
import os

def calculate_hash(file_path, algorithm):
    """Calculates the hash for the specified file using the specified algorithm."""
    hash_func = getattr(hashlib, algorithm)()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_func.update(byte_block)
    return hash_func.hexdigest()

def compare_hashes(file_path, expected_hash, algorithm):
    """Compares the hash of the file with the expected hash."""
    file_hash = calculate_hash(file_path, algorithm)
    result = "True" if file_hash.lower() == expected_hash.lower() else "False"
    print(f">>>{result}:\n{file_hash}\n{expected_hash}")

if __name__ == "__main__":
    # Data entry
    # Ввод данныхs
    file_path = input(">>> Input path to file: ")
    
    # Checking the existence of a file
    # Проверка наличия файла
    if not os.path.isfile(file_path):
        print(">>> Error: File does not exist.")
    else:
        expected_hash = input(">>> Input hash sum: ")
        algorithm = input(">>> Input hashing algorithm (e.g., sha256, md5): ")
        
        # Checking for the existence of an algorithm
        # Проверка на наличие алгоритма
        if hasattr(hashlib, algorithm):
            compare_hashes(file_path, expected_hash, algorithm)
        else:
            print(">>> Error: Unsupported hashing algorithm.")

