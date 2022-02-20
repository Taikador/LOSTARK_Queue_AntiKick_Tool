import tkinter as tk
from tkinter import filedialog, ttk, PhotoImage

import subprocess
import psutil
import pyautogui
import time
import random

root = tk.Tk()
img = PhotoImage(file='Lost.png')
root.geometry("400x100")
root.title("LOSTARK - Skipper")
root.iconphoto(True, img)

pathframe = tk.LabelFrame(root, text="Steam Executable Path")
pathframe.place(height=100, width=400, relx=0)

# Buttons
steambutton = tk.Button(pathframe, text="Browse", command=lambda: _steam_dialog())
steambutton.place(rely=0.65, relx=0.35)

startbutton = tk.Button(pathframe, text="Start", command=lambda: _main_loop())
startbutton.place(rely=0.65, relx=0.55)

label_steam = ttk.Label(pathframe, text="No Steam Executable selected")
label_steam.place(rely=0, relx=0)

def _steam_dialog():
    steampath = filedialog.askopenfilename(initialdir="C:\\Program Files (x86)\\Steam\\", title="Select Steam Executable", filetype=[("Applications", "*.exe")])
    label_steam["text"] = steampath
    return None

def _main_loop():
    _start_game()
    running = _check_game_active()

    if running == True:
        time.sleep(100)
        _connect_to_server()
    
    time.sleep(100)
    _stay_connected()

def _start_game():
    steam_path = label_steam["text"]
    game_string = " -applaunch 1599340"
    subprocess.call(steam_path + game_string)

def _check_game_active():
    running = False

    while running == False:
        running = "LOSTARK.exe" in (i.name() for i in psutil.process_iter())

        if running == True:
            return True
        else:
            continue

def _connect_to_server():
    pyautogui.moveTo(950, 918)
    pyautogui.click()

def _stay_connected():
    while 1 > 0:
        wait_time = random.randrange(290, 420)
        time.sleep(wait_time)
        pyautogui.moveTo(249, 1011)
        pyautogui.click()
        time.sleep(wait_time)
        pyautogui.moveTo(210, 1016)
        pyautogui.click()

root.mainloop()