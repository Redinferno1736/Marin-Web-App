import webbrowser
import os
import screen_brightness_control as sbc
import ctypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import comtypes
from comtypes import CLSCTX_ALL
import httpx
from bs4 import BeautifulSoup

class CustomVideosSearch(VideosSearch):
    def __init__(self, query, limit=None, language=None, region=None):
        super().__init__(query, limit, language, region)
        self.payload = {
            "query": query,
            "context": {
                "client": {
                    "clientName": "WEB",
                    "clientVersion": "2.20210909.07.00",
                }
            }
        }

    def syncPostRequest(self):
        # Make a POST request without the proxies argument
        return httpx.post(self.url, json=self.payload, headers=self.headers)

def search(text):
    t = text.replace("search for", "")
    url = f"https://www.google.com/search?q={t}"
    webbrowser.open(url)

def play(text):
    t = text.replace("play", "").strip()
    search = CustomVideosSearch(t, limit=1)
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
        os.system("start " + t)

def set_volume(level):
    """Set system volume using Pycaw."""
    comtypes.CoInitialize()  # Initialize COM before using Pycaw

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    
    volume.SetMasterVolumeLevelScalar(level / 100.0, None)

    comtypes.CoUninitialize()

def tools(text):
    mapping = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4}
    newtext = text.split()
    
    # Ensure that at least two words exist in the text
    if len(newtext) < 3:
        print("Invalid command format")
        return
    
    value = newtext[-1]  # Extract the last word (expected number)

    try:
        a = int(value)
    except ValueError:
        a = mapping.get(value.lower(), None)  # Get the mapped value or None

    if a is None:
        print(f"Invalid number: {value}")
        return

    if "brightness" in newtext:
        sbc.set_brightness(a)
    elif "volume" in newtext:
        set_volume(a)
