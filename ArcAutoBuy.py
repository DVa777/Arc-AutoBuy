import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except:
        pass

import time
import tkinter.messagebox
import pygame
from pyautogui import ImageNotFoundException
import cv2
import numpy as np
import pyautogui

def clicktotraiders():
    try:
        findedlocation = locateOnScreenScaled("./imgs/interfaces/traders.png", confidence=0.85)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.click()
    except ImageNotFoundException as e:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("OwO","cant find the right place are u in arc raiders?")

def clicktotab():
    findedlocation = locateOnScreenScaled("./imgs/interfaces/tab.png", confidence=0.7)
    x, y = pyautogui.center(findedlocation)
    pyautogui.moveTo(x, y)
    pyautogui.click()

def clicktoclinic():
    try:
        findedlocation = locateOnScreenScaled("./imgs/interfaces/clinic.png", confidence=0.85)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.click()
    except ImageNotFoundException as e:
        findedlocation = locateOnScreenScaled("./imgs/interfaces/clinic_2.png", confidence=0.85)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.click()


def clicktoinvcategory(category):
        try:
            findedlocation = locateOnScreenScaled(f"./imgs/interfaces/{category}.png", confidence=0.7)
            x, y = pyautogui.center(findedlocation)
            pyautogui.moveTo(x, y)
            pyautogui.click()
        except ImageNotFoundException as e:
            findedlocation = locateOnScreenScaled(f"./imgs/interfaces/{category}_2.png", confidence=0.7)
            x, y = pyautogui.center(findedlocation)
            pyautogui.moveTo(x, y)
            pyautogui.click()

def clicktogadgets():
    try:
        findedlocation = locateOnScreenScaled("./imgs/interfaces/gadgets.png", confidence=0.7)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.click()
    except ImageNotFoundException as e:
        findedlocation = locateOnScreenScaled("./imgs/interfaces/gadgets_2.png", confidence=0.7)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.click()

def clicktoback():
    try:
        findedlocation = locateOnScreenScaled("./imgs/interfaces/back.png", confidence=0.85)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.click()
    except Exception as e:
        pass

def focustoback():
    try:
        findedlocation = locateOnScreenScaled("./imgs/interfaces/back.png", confidence=0.85)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
    except Exception as e:
        pass

def clicktogunshop():
    findedlocation = locateOnScreenScaled("./imgs/interfaces/gun_shop.png", confidence=0.7)
    x, y = pyautogui.center(findedlocation)
    pyautogui.moveTo(x, y)
    pyautogui.click()

def makepurchase(ammount):
    try:
        findedlocation = locateOnScreenScaled("./imgs/interfaces/purchase.png", confidence=0.85)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
    except ImageNotFoundException as e:
        tkinter.messagebox.showerror("OwO", "u cant afford that or ur stash is full")
        try:
            pygame.mixer.music.stop()
        except Exception as e:
            pass
        return
    except Exception as e:
        pass

    while ammount > 0:
        pyautogui.mouseDown()
        time.sleep(2)
        pyautogui.mouseUp()
        ammount -= 1

    if ammount == 1:
        pyautogui.mouseDown()
        time.sleep(2)
        pyautogui.mouseUp()

def buyammo(ammo, ammount):
    if ammo == "shotgun_ammo" or ammo == "heavy_ammo":
        try:
            findedlocation = locateOnScreenScaled(f"./imgs/ammos/{ammo}.png", confidence=0.8)
            x, y = pyautogui.center(findedlocation)
            pyautogui.moveTo(x, y)
            pyautogui.click()
            makepurchase(ammount)

        except ImageNotFoundException as e:
            try:
                findedlocation = locateOnScreenScaled(f"./imgs/ammos/{ammo}_2.png", confidence=0.8)
                x, y = pyautogui.center(findedlocation)
                pyautogui.moveTo(x, y)
                pyautogui.click()
                makepurchase(ammount)
            except Exception as e:
                pass
        except Exception as e:
            pass
    else:
        try:
            findedlocation = locateOnScreenScaled(f"./imgs/ammos/{ammo}.png", confidence=0.85)
            x, y = pyautogui.center(findedlocation)
            pyautogui.moveTo(x, y)
            pyautogui.click()
            makepurchase(ammount)

        except ImageNotFoundException as e:
            try:
                findedlocation = locateOnScreenScaled(f"./imgs/ammos/{ammo}_2.png", confidence=0.85)
                x, y = pyautogui.center(findedlocation)
                pyautogui.moveTo(x, y)
                pyautogui.click()
                makepurchase(ammount)
            except Exception as e:
                pass
        except Exception as e:
            pass

def selectammo(ammo):
    if ammo == "shotgun_ammo" or ammo == "heavy_ammo":
        try:
            findedlocation = locateOnScreenScaled(f"./imgs/ammos/{ammo}.png", confidence=0.8)
            x, y = pyautogui.center(findedlocation)
            pyautogui.moveTo(x, y)
            pyautogui.doubleClick()

        except ImageNotFoundException as e:
            try:
                findedlocation = locateOnScreenScaled(f"./imgs/ammos/{ammo}_2.png", confidence=0.8)
                x, y = pyautogui.center(findedlocation)
                pyautogui.moveTo(x, y)
                pyautogui.doubleClick()
            except Exception as e:
                pass
        except Exception as e:
            pass
    else :
        try:
            findedlocation = locateOnScreenScaled(f"./imgs/ammos/{ammo}.png", confidence=0.85)
            x, y = pyautogui.center(findedlocation)
            pyautogui.moveTo(x, y)
            pyautogui.doubleClick()

        except ImageNotFoundException as e:
            try:
                findedlocation = locateOnScreenScaled(f"./imgs/ammos/{ammo}_2.png", confidence=0.85)
                x, y = pyautogui.center(findedlocation)
                pyautogui.moveTo(x, y)
                pyautogui.doubleClick()
            except Exception as e:
                pass
        except Exception as e:
            pass

def buygun(gun):
    try:
        findedlocation = locateOnScreenScaled(f"./imgs/guns/{gun}.png", confidence=0.7)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        makepurchase(1)
    except ImageNotFoundException as e:
        findedlocation = locateOnScreenScaled(f"./imgs/guns/{gun}_2.png", confidence=0.7)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        makepurchase(1)
    except Exception as e:
        pass

def selectgun(gun):
    try:
        findedlocation = locateOnScreenScaled(f"./imgs/invguns/{gun}.png", confidence=0.85)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.doubleClick()
    except Exception as e:
        pass

def buyothers(item, ammount):
    try:
        findedlocation = locateOnScreenScaled(f"./imgs/items/{item}.png", confidence=0.7)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        makepurchase(int(ammount))
    except ImageNotFoundException as e:
        findedlocation = locateOnScreenScaled(f"./imgs/items/{item}_2.png", confidence=0.7)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        makepurchase(int(ammount))
    except Exception as e:
        pass

def selectothers(item):
    try:
        findedlocation = locateOnScreenScaled(f"./imgs/items/{item}.png", confidence=0.7)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.doubleClick()
    except ImageNotFoundException as e:
        findedlocation = locateOnScreenScaled(f"./imgs/items/{item}_2.png", confidence=0.7)
        x, y = pyautogui.center(findedlocation)
        pyautogui.moveTo(x, y)
        pyautogui.doubleClick()
    except Exception as e:
        pass

# idfk wtf is this but its work, its only method where i use full AI code cuz it solves a big problem of display resolutions (forgive me)
BASE_WIDTH = 2560
BASE_HEIGHT = 1600

screen_width, screen_height = pyautogui.size()

SCALE_X = screen_width / BASE_WIDTH
SCALE_Y = screen_height / BASE_HEIGHT
SCALES = np.arange(0.50, 1.51, 0.01)

def locateOnScreenScaled(image_path, confidence=0.85):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    template = cv2.imread(image_path)

    if template is None:
        raise FileNotFoundError(image_path)

    if SCALE_X != 1.0 or SCALE_Y != 1.0:
        template = cv2.resize(
            template,
            None,
            fx=SCALE_X,
            fy=SCALE_Y,
            interpolation=cv2.INTER_CUBIC
        )

    result = cv2.matchTemplate(
        screenshot,
        template,
        cv2.TM_CCOEFF_NORMED
    )

    _, score, _, loc = cv2.minMaxLoc(result)

    if score < confidence:
        raise ImageNotFoundException(
            f"Could not locate the image (confidence = {score:.3f})"
        )

    h, w = template.shape[:2]

    return (loc[0], loc[1], w, h)