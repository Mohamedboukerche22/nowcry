import os
from cryptography.fernet import Fernet

# key = b'COLLEZ_VOTRE_CLE_ICI'
key = b'N8jnr5qAggtybY4D-GJH8rqQ4H9WRXy8MUXNw8d0Q50='
def decrypt_directory(target_dir):
    fernet = Fernet(key)
    target_extensions = ('.txt', '.jpg', '.jpeg', '.png', '.gif', '.bmp','.pdf')

    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.lower().endswith(target_extensions):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "rb") as f:
                        encrypted_data = f.read()

                    decrypted_data = fernet.decrypt(encrypted_data)

                    with open(file_path, "wb") as f:
                        f.write(decrypted_data)
                           
                    print(file_path, "decrypted successfully")

                except Exception as e:
                    print("Failed to decrypt", file_path, "-", e)

decrypt_directory("/home/mohamed/malware/test/")

