import os
import time

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

os.system("cls")
osize = int(0)
direct = "C:/Program Files (x86)/Steam/steamapps"

while True:
    csize = int(get_size(direct))
    if csize == osize:
        print("Size hasnt changed since last pass")
        time.sleep(60)
        csize = int(get_size(direct))
        if csize == osize:
            print("Size still hasnt changed, assuming steam has completed\n\n SHUTTING DOWN")
            os.system("C:/WINDOWS/system32/shutdown.exe")
        else:
            print("Size has increased")
    if csize > osize:
        osize = csize
        print("Size has increased")
    time.sleep(3)
    os.system("cls")
    print("WAITING...")
    time.sleep(57)
    
 
