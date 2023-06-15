import subprocess
from PIL import Image
import io


def get_window_id(name):
        try:
            result = subprocess.run(['xdotool', 'search', '--onlyvisible', '--name', '.'],
                                    capture_output=True, text=True, check=True)
            window_ids = result.stdout.strip().split('\n')
            for window_id in window_ids:
                result = subprocess.run(['xdotool', 'getwindowname', window_id],
                                        capture_output=True, text=True, check=True)
                if result.stdout.strip() == name:
                    return window_id

            raise NoSuchWindowException(name)

        except subprocess.CalledProcessError as e:
            raise e

def PressKey(key):
    process = subprocess.run(['xdotool', 'keydown', str(key)])

def ReleaseKey(key):
    process = subprocess.run(['xdotool', 'keyup', str(key)])

idd = get_window_id("Trackmania")

process = subprocess.run(['xdotool', 'windowfocus', '--sync', str(idd)])
PressKey("BackSpace")