import os, platform, time
try:
    import rich
    os.system('pip install rich')
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support Tolls\033[1;37m")
    time.sleep(3)
    from AKING import Menu
    Menu()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
