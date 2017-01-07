import os
import time

print('Where is Steamapps located?')
direct = input('The default location is, C:\Program Files (x86)\Steam\steamapps\n\n ')

if os.path.isdir(direct):
    pass
else:
    print("That directory doesnt exist")
    time.sleep(3)
    print("Attempting default location")
    direct = "C:\Program Files (x86)\Steam\steamapps"
    if os.path.isdir(direct):
        pass
    else:
        print("Couldnt find steam in specified location or default location, aborting")
        time.sleep(2)
        exit()
os.system("cls")
print("Doing initial size checks on " + direct + " this may take a minute")


def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

osize = int(0)


while True:
    csize = int(get_size(direct))
    if csize == osize:
        print("Size hasnt changed since last pass")
        time.sleep(3)
        os.system("cls")
        time.sleep(57)
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
    print("WAITING 60 SECONDS BEFORE NEXT CHECK...")
    time.sleep(57)

