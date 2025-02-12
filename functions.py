import webbrowser
from youtubesearchpython import VideosSearch
import os
import platform
import httpx

# Platform-specific imports and setup
if platform.system() == "Windows":
    try:
        import screen_brightness_control as sbc
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        import comtypes
        from comtypes import CLSCTX_ALL
    except ImportError:
        print("Warning: screen-brightness-control, pycaw, or comtypes not installed. Volume and brightness control will not work.")
        sbc = None
        AudioUtilities = None
        IAudioEndpointVolume = None
        comtypes = None
        CLSCTX_ALL = None
else:
    print("Warning: Volume and brightness control are not supported on this platform.")
    sbc = None
    AudioUtilities = None
    IAudioEndpointVolume = None
    comtypes = None
    CLSCTX_ALL = None


def search(text):
    """Perform a Google search."""
    t = text.replace("search for", "").strip()
    url = f"https://www.google.com/search?q={t}"
    webbrowser.open(url)


class CustomVideosSearch(VideosSearch):
    def syncPostRequest(self):
        # Make a POST request without the proxies argument
        return httpx.post(self.url, json=self.payload, headers=self.headers)

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
    """Find and open a folder on the system."""
    folder_name = text.replace("open", "").replace("folder", "").strip()

    for root, dirs, _ in os.walk(search_path):
        if folder_name.lower() in [d.lower() for d in dirs]:
            path = os.path.join(root, folder_name)
            os.system(f'start "" "{path}"')
            return

    print(f"Folder '{folder_name}' not found.")


def openapp(text):
    """Open a Windows app or folder."""
    t = text.replace("open", "").strip()
    try:
        os.system(f"explorer ms-{t}:")
    except:
        os.system("start " + t)


def set_volume(level):
    """Set system volume using Pycaw (Windows only)."""
    if platform.system() != "Windows" or AudioUtilities is None or IAudioEndpointVolume is None:
        print("Volume control is not supported on this platform.")
        return

    comtypes.CoInitialize()  # Initialize COM before using Pycaw
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level / 100.0, None)
    comtypes.CoUninitialize()


def tools(text):
    """Handle system tools like brightness and volume control."""
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
        if sbc is None:
            print("Brightness control is not supported on this platform.")
        else:
            sbc.set_brightness(a)
    elif "volume" in newtext:
        set_volume(a)
