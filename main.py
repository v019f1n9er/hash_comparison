import hashlib
import os

def calculate_hash(file_path, algorithm):
    """Вычисляет хэш для указанного файла с использованием заданного алгоритма."""
    hash_func = getattr(hashlib, algorithm)()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_func.update(byte_block)
    return hash_func.hexdigest()

def compare_hashes(file_path, expected_hash, algorithm):
    """Сравнивает хэш файла с ожидаемым хэшем."""
    file_hash = calculate_hash(file_path, algorithm)
    result = "True" if file_hash.lower() == expected_hash.lower() else "False"
    print(f">>>{result}:\n{file_hash}\n{expected_hash}")

if __name__ == "__main__":
    # Ввод данных
    file_path = input(">>> Input path to file: ")
    
    # Проверка существования файла
    if not os.path.isfile(file_path):
        print(">>> Error: File does not exist.")
    else:
        expected_hash = input(">>> Input hash sum: ")
        algorithm = input(">>> Input hashing algorithm (e.g., sha256, md5): ")
        
        # Проверка на существование алгоритма
        if hasattr(hashlib, algorithm):
            compare_hashes(file_path, expected_hash, algorithm)
        else:
            print(">>> Error: Unsupported hashing algorithm.")
