import hashlib
import os

# Obtener la ruta del directorio del script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Definir los hashes MD5 originales con rutas relativas
original_hashes = {
    "copia.sh": "90965b0eb20e68b7d0b59accd2a3b4fd",
    "log.txt": "0b29406e348cd5f17c2fd7b47b1012f9",
    "pass.txt": "6d5e43a730490d75968279b6adbd79ec",
    "plan-A.txt": "129ea0c67567301df1e1088c9069b946",
    "plan-B.txt": "4e9878b1c28daf4305f17af5537f062a",
    "script.py": "66bb9ec43660194bc066bd8b4d35b151",
}

# Función para calcular el hash MD5 de un archivo
def calculate_md5(file_path, block_size=65536):
    md5 = hashlib.md5()
    try:
        with open(file_path, 'rb') as file:
            for block in iter(lambda: file.read(block_size), b''):
                md5.update(block)
        return md5.hexdigest()
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al calcular el hash MD5: {e}")
        return None

# Verificar la integridad de los archivos
for file, original_hash in original_hashes.items():
    file_path = os.path.join(script_dir, file)  # Ruta completa del archivo
    calculated_hash = calculate_md5(file_path)

    if calculated_hash and calculated_hash == original_hash:
        print(f"El archivo {file} no ha sido modificado. Hash: {calculated_hash}")
    elif not calculated_hash:
        print(f"No se pudo calcular el hash para {file}.")
    else:
        print(f"El archivo {file} ha sido modificado. Hash original: {original_hash}, Hash actual: {calculated_hash}")
