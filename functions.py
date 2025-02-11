import webbrowser
from youtubesearchpython import VideosSearch
import os
import screen_brightness_control as sbc
import ctypes
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def search(text):
    t= text.replace("search for", "")
    url = f"https://www.google.com/search?q={t}"
    webbrowser.open(url)

def play(text):
    t = text.replace("play", "").strip()
    search = VideosSearch(t, limit=1)
    results = search.result()

    if results and "result" in results and len(results["result"]) > 0:
        first_video_url = results["result"][0]["link"]
        webbrowser.open(first_video_url)
    else:
        print("No results found.")

def find_folder(text, search_path="C:\\"):
    folder_name = text.replace("open", "").replace("folder", "").strip()

    for root, dirs, _ in os.walk(search_path):
        if folder_name.lower() in [d.lower() for d in dirs]:
            path = os.path.join(root, folder_name)
            os.system(f'start "" "{path}"')
            return

    print(f"Folder '{folder_name}' not found.")

def openapp(text):
    t = text.replace("open", "").strip()
    try:
        os.system(f"explorer ms-{t}:")
    except:
        os.system("start "+t)

def set_volume(level):
    """Set system volume using Pycaw."""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None) 
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))

    volume.SetMasterVolumeLevelScalar(level / 100.0, None)

def tools(text):
    dict={"zero":0,"one":1,"two":2,"three":3,"four":4}
    newtext= text.split()
    value=newtext[-1]
    try:
        a=int(value)
    except:
        a=dict[value]

    if newtext[1]=="brightness":
        sbc.set_brightness(a)
    else:
        set_volume(a)