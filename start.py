from cryptography.fernet import Fernet
import os

# Fungsi untuk generate key
def generate_key():
    return Fernet.generate_key()

# Fungsi untuk enkripsi file
def encrypt_file(key, filename):
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Fungsi untuk dekripsi file
def decrypt_file(key, filename):
    fernet = Fernet(key)
    with open(filename, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

# Fungsi untuk melakukan enkripsi pada semua file dalam direktori dengan ekstensi tertentu
def encrypt_files_in_directory(directory, key, file_extensions):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and any(filename.lower().endswith(ext) for ext in file_extensions):
            encrypt_file(key, filepath)
            print(f"{filename} berhasil dienkripsi.")

# Fungsi untuk melakukan dekripsi pada semua file dalam direktori dengan ekstensi tertentu
def decrypt_files_in_directory(directory, key, file_extensions):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and any(filename.lower().endswith(ext) for ext in file_extensions):
            decrypt_file(key, filepath)
            print(f"{filename} berhasil didekripsi.")

# Fungsi untuk memilih format file
def choose_format():
    print("\nPilih format file:")
    print("1. Gambar (.jpg/.png)")
    print("2. Video (.mp4)")
    print("3. Audio (.mp3)")
    print("4. Semua format di atas")
    format_choice = input("Masukkan pilihan Anda: ")
    
    if format_choice == '1':
        return ['.jpg', '.png']
    elif format_choice == '2':
        return ['.mp4']
    elif format_choice == '3':
        return ['.mp3']
    elif format_choice == '4':
        return ['.jpg', '.png', '.mp4', '.mp3']
    else:
        print("Pilihan tidak valid. Memilih semua format.")
        return ['.jpg', '.png', '.mp4', '.mp3']

# Fungsi untuk memilih aksi (1: enkripsi, 2: dekripsi, 0: keluar)
def choose_action():
    while True:
        print("\nPilih aksi:")
        print("1. Enkripsi file dalam direktori")
        print("2. Dekripsi file dalam direktori")
        print("0. Keluar")
        
        action = input("Masukkan pilihan Anda: ")
        
        if action == '1':
            directory = input("Masukkan direktori tempat file berada: ")
            key = generate_key()
            file_extensions = choose_format()
            encrypt_files_in_directory(directory, key, file_extensions)
            print(f"Kunci enkripsi Anda: {key.decode()}")  # Menampilkan kunci enkripsi, bisa disimpan secara aman
        elif action == '2':
            directory = input("Masukkan direktori tempat file terenkripsi berada: ")
            key = input("Masukkan kunci enkripsi: ").encode()
            file_extensions = choose_format()
            decrypt_files_in_directory(directory, key, file_extensions)
        elif action == '0':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Memilih aksi utama
choose_action()
