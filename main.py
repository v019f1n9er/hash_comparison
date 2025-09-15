import hashlib
import os

def calculate_hash(file_path, algorithm):
    # Calculates the hash for the specified file using the specified algorithm
    # Получаем функцию хеширования по имени алгоритма
    hash_func = getattr(hashlib, algorithm)()
    
    # Открываем файл в двоичном режиме для чтения
    with open(file_path, "rb") as f:
        # Читаем файл блоками по 4096 байт и обновляем хеш
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_func.update(byte_block)
    
    # Возвращаем хеш в шестнадцатеричном формате
    return hash_func.hexdigest()

def compare_hashes(file_path, expected_hash, algorithm):
    # Compares the hash of the file with the expected hash
    # Вычисляем хеш файла
    file_hash = calculate_hash(file_path, algorithm)
    
    # Сравниваем вычисленный хеш с ожидаемым
    result = file_hash.lower() == expected_hash.lower()
    
    # Выводим результат сравнения и оба хеша
    print(f">>> Comparison result: {result}\nCalculated Hash: {file_hash}\nExpected Hash: {expected_hash}")

if __name__ == "__main__":
    # Запрашиваем путь к файлу у пользователя
    file_path = input(">>> Input path to file: ")
    
    # Проверяем существование файла
    if not os.path.isfile(file_path):
        print(">>> Error: File does not exist.")
    else:
        # Запрашиваем ожидаемый хеш и алгоритм хеширования
        expected_hash = input(">>> Input hash sum: ")
        algorithm = input(">>> Input hashing algorithm (e.g., sha256, md5): ")
        
        # Проверяем, поддерживается ли указанный алгоритм хеширования
        if hasattr(hashlib, algorithm):
            compare_hashes(file_path, expected_hash, algorithm)
        else:
            print(">>> Error: Unsupported hashing algorithm.")
