import os
import zipfile
import hashlib

dir_path = 'recording-files'
total_mp4_files = 0

def calculate_sha256(file_path):
    """Calcula el hash SHA256 de un archivo."""
    with open(file_path, 'rb') as f:
        file_hash = hashlib.sha256()
        # Leer y actualizar el hash en fragmentos para evitar
        # el uso excesivo de memoria
        for byte_block in iter(lambda: f.read(4096), b""):
            file_hash.update(byte_block)
        return file_hash.hexdigest()

# Listar todos los archivos en el directorio especificado
all_files = os.listdir(dir_path)

# Filtrar solo los archivos .zip
# zip_files = [f for f in all_files if f.endswith('.zip')]
zip_files = [f for f in all_files if f.endswith('.zip') and not f.startswith('._')]

# Iterar a través de cada archivo .zip, contar los archivos .mp4 y calcular su hash
for zip_file in zip_files:
    # print(f'Procesando {zip_file}')
    full_path = os.path.join(dir_path, zip_file)
    with zipfile.ZipFile(full_path, 'r') as z:
        mp4_files = [f for f in z.namelist() if f.endswith('.mp4')]
        num_mp4 = len(mp4_files)
        total_mp4_files += num_mp4
    # file_hash = calculate_sha256(full_path)
    file_size = os.path.getsize(full_path)
    # print(f'El archivo ZIP {zip_file} contiene {num_mp4} archivos .mp4 y tiene el hash SHA256: {file_hash}.')
    print(f'{zip_file};{file_size};{num_mp4}')

print(f'\nTotal de archivos .mp4 en todos los archivos ZIP: {total_mp4_files}')
