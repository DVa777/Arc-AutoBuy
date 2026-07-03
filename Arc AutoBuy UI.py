import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except:
        pass

import time
import pygame
from pypresence import Presence
import tkinter as tk
import tkinter.messagebox
from tkinter import BooleanVar, StringVar
from ArcAutoBuy import buygun, buyammo, clicktoclinic, buyothers, makepurchase, clicktotraiders, clicktogunshop, clicktogadgets, clicktotab, clicktoinvcategory, selectgun, selectammo, selectothers, clicktoback, focustoback
import pyautogui
arcautobuy = tk.Tk()
arcautobuy.title("Arc AutoBuy")
arcautobuy.geometry("1500x750")
arcautobuy.resizable(False,False)
img = tk.PhotoImage(file="./imgs/interfaces/inventory.png")

rpc = Presence(1522307801857265684)
rpc.connect()
rpc.update(
    details="AutoBuy - AutoEquip Loadout",
    state="For Arc Raiders",
    buttons=[{"label": "Download", "url": "https://github.com/DVa777/Arc-AutoBuy"}]
)

label = tk.Label(arcautobuy,image=img)
label.place(x=0, y=0, relwidth=1, relheight=1)

gun = tk.StringVar()
gun2 = tk.StringVar()
shield = tk.StringVar()
mk = tk.StringVar()

maingunk = tk.Radiobutton(arcautobuy,text="Kettle",background="#1a1a22",fg="gray", variable=gun, value="kettle")
maingunk.place(relx=0.075,rely=0.32,anchor="center")

mainguna = tk.Radiobutton(arcautobuy,text="Anvil",background="#1a1a22",fg="gray", variable=gun, value="anvil")
mainguna.place(relx=0.072,rely=0.38,anchor="center")

mainguni = tk.Radiobutton(arcautobuy,text="Il Toro",background="#1a1a22",fg="gray", variable=gun, value="iltoro")
mainguni.place(relx=0.157,rely=0.38,anchor="center")

mainguns = tk.Radiobutton(arcautobuy,text="Stitcher",background="#1a1a22",fg="gray", variable=gun, value="stitcher")
mainguns.place(relx=0.16,rely=0.32,anchor="center")

maingunf = tk.Radiobutton(arcautobuy,text="Ferro",background="#1a1a22",fg="gray", variable=gun, value="ferro")
maingunf.place(relx=0.245,rely=0.32,anchor="center")

maingunk2 = tk.Radiobutton(arcautobuy,text="Kettle",background="#1a1a22",fg="gray", variable=gun2, value="kettle")
maingunk2.place(relx=0.075,rely=0.54,anchor="center")

mainguna2 = tk.Radiobutton(arcautobuy,text="Anvil",background="#1a1a22",fg="gray", variable=gun2, value="anvil")
mainguna2.place(relx=0.072,rely=0.6,anchor="center")

mainguns2 = tk.Radiobutton(arcautobuy,text="Stitcher",background="#1a1a22",fg="gray", variable=gun2, value="stitcher")
mainguns2.place(relx=0.16,rely=0.54,anchor="center")

mainguni2 = tk.Radiobutton(arcautobuy,text="Il Toro",background="#1a1a22",fg="gray", variable=gun2, value="iltoro")
mainguni2.place(relx=0.16,rely=0.60,anchor="center")

maingunf2 = tk.Radiobutton(arcautobuy,text="Ferro",background="#1a1a22",fg="gray", variable=gun2, value="ferro")
maingunf2.place(relx=0.245,rely=0.54,anchor="center")

augmentc = tk.Radiobutton(arcautobuy,text="Combat",background="#1a1a22",fg="gray", variable=mk, value="combat")
augmentc.place(relx=0.075,rely=0.17,anchor="center")

augmentl = tk.Radiobutton(arcautobuy,text="Looting",background="#1a1a22",fg="gray", variable=mk, value="looting")
augmentl.place(relx=0.075,rely=0.21,anchor="center")

augmentt = tk.Radiobutton(arcautobuy,text="Tactical",background="#1a1a22",fg="gray", variable=mk, value="tactical")
augmentt.place(relx=0.077,rely=0.25,anchor="center")

shieldl = tk.Radiobutton(arcautobuy,text="Light",background="#1a1a22",fg="gray", variable=shield, value="light")
shieldl.place(relx=0.198,rely=0.17,anchor="center")

shieldm = tk.Radiobutton(arcautobuy,text="Medium",background="#1a1a22",fg="gray", variable=shield, value="medium")
shieldm.place(relx=0.205,rely=0.21,anchor="center")

shieldh = tk.Radiobutton(arcautobuy,text="Heavy",background="#1a1a22",fg="gray", variable=shield, value="heavy")
shieldh.place(relx=0.2,rely=0.25,anchor="center")

bvalue = BooleanVar(arcautobuy)
bvalue.set(False)

bandages = tk.Checkbutton(arcautobuy,text="Bandage",background="#1a1a22",fg="gray",variable=bvalue)
bandages.place(relx=0.746,rely=0.18,anchor="center")

shr = BooleanVar(arcautobuy)
shr.set(False)

shrecharge2 = tk.Checkbutton(arcautobuy,text="Sh. Recharger",background="#1a1a22",fg="gray",variable=shr)
shrecharge2.place(relx=0.835,rely=0.18,anchor="center")

smok = BooleanVar(arcautobuy)
smok.set(False)

smoke = tk.Checkbutton(arcautobuy,text="Smoke",background="#1a1a22",fg="gray",variable=smok)
smoke.place(relx=0.917,rely=0.18,anchor="center")

deff = BooleanVar(arcautobuy)
deff.set(False)

defib = tk.Checkbutton(arcautobuy,text="Defibrillator",background="#1a1a22",fg="gray",variable=deff)
defib.place(relx=0.746,rely=0.29,anchor="center")

light = BooleanVar(arcautobuy)
light.set(False)

ammol = tk.Checkbutton(arcautobuy,text="Light Ammo",background="#1a1a22",fg="gray", variable= light)
ammol.place(relx=0.347,rely=0.18,anchor="center")

mid = BooleanVar(arcautobuy)
mid.set(False)

ammom = tk.Checkbutton(arcautobuy,text="Medium Ammo",background="#1a1a22",fg="gray", variable=mid)
ammom.place(relx=0.447,rely=0.18,anchor="center")

hvy = BooleanVar(arcautobuy)
hvy.set(False)

ammoh = tk.Checkbutton(arcautobuy,text="Heavy Ammo",background="#1a1a22",fg="gray",variable=hvy)
ammoh.place(relx=0.55,rely=0.18,anchor="center")

sss = BooleanVar(arcautobuy)
sss.set(False)

ammos = tk.Checkbutton(arcautobuy,text="Shotgun Ammo",background="#1a1a22",fg="gray",variable=sss)
ammos.place(relx=0.65,rely=0.18,anchor="center")

lllamo = StringVar()
lllamo.set("25")

ammolll = tk.Entry(arcautobuy, textvariable=lllamo)
ammolll.place(width=25,height=25,relx=0.365,rely=0.23,anchor="center")

mmmammo = StringVar()
mmmammo.set("20")

ammomm = tk.Entry(arcautobuy, textvariable=mmmammo)
ammomm.place(width=25,height=25,relx=0.45,rely=0.23,anchor="center")

hhhammo = StringVar()
hhhammo.set("10")

ammohh = tk.Entry(arcautobuy, textvariable=hhhammo)
ammohh.place(width=25,height=25,relx=0.54,rely=0.23,anchor="center")

sssammo = StringVar()
sssammo.set("5")

ammoss = tk.Entry(arcautobuy, textvariable=sssammo)
ammoss.place(width=25,height=25,relx=0.625,rely=0.23,anchor="center")

bnd = StringVar()
bnd.set("1")

bandagess = tk.Entry(arcautobuy, textvariable=bnd)
bandagess.place(width=25,height=25,relx=0.75,rely=0.23,anchor="center")

idkimjusttired = StringVar()
idkimjusttired.set("1")

shrecharge = tk.Entry(arcautobuy,textvariable=idkimjusttired)
shrecharge.place(width=25,height=25,relx=0.835,rely=0.23,anchor="center")

smk = StringVar()
smk.set("1")

smokee = tk.Entry(arcautobuy,textvariable=smk)
smokee.place(width=25,height=25 ,relx=0.92,rely=0.23,anchor="center")


musicb = BooleanVar(arcautobuy)
musicb.set(True)

musicc = tk.Checkbutton(arcautobuy,text="Music",variable=musicb)
musicc.place(relx=0.75,rely=0.85,anchor="center")

notifb = BooleanVar(arcautobuy)
notifb.set(True)

notiff = tk.Checkbutton(arcautobuy,text="Notification",variable=notifb)
notiff.place(relx=0.685,rely=0.85,anchor="center")

buyb = BooleanVar(arcautobuy)
buyb.set(True)

buyyy = tk.Checkbutton(arcautobuy,text="Buy",variable=buyb)
buyyy.place(relx=0.7,rely=0.77,anchor="center")

sortb = BooleanVar(arcautobuy)
sortb.set(True)

sorttt = tk.Checkbutton(arcautobuy,text="Equip",variable=sortb)
sorttt.place(relx=0.75,rely=0.77,anchor="center")

dfb = StringVar()
dfb.set("1")

defibb = tk.Entry(arcautobuy, textvariable=dfb)
defibb.place(width=25,height=25,relx=0.75,rely=0.34,anchor="center")

timex = StringVar()
timex.set("5")

timee = tk.Entry(arcautobuy,textvariable=timex)
timee.place(width=40,height=40,relx=0.76,rely=0.93,anchor="center")


timetext = tk.Label(arcautobuy, text="Seconds Before Start! =====>",bg="white")
timetext.place(width=300,height=40,relx=0.64,rely=0.93,anchor="center")

def save():
    if light.get() and int(ammolll.get()) % 25 != 0:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("QwQ", "Light Ammo Value must be divisible by 25.")
        return

    if mid.get() and int(ammomm.get()) % 20 != 0:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("QwQ", "Medium Ammo Value must be divisible by 20.")
        return

    if hvy.get() and int(ammohh.get()) % 10 != 0:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("QwQ", "Heavy Ammo Value must be divisible by 10.")
        return

    if sss.get() and int(ammoss.get()) % 5 != 0:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("QwQ", "Shotgun Ammo Value must be divisible by 5.")
        return
    try:
        if mk.get() == "":
            mkfixed = "None"
        else:
            mkfixed = mk.get()

        if gun.get() == "":
            gunfixed = "None"
        else:
            gunfixed = gun.get()

        if gun2.get() == "":
            gun2fixed = "None"
        else:
            gun2fixed = gun2.get()

        if shield.get() == "":
            shieldfixed = "None"
        else:
            shieldfixed = shield.get()

        with open("config.txt", "w") as file:
            file.write(f"Main gun: {gunfixed}\nSecond gun: {gun2fixed}\nAugument: {mkfixed}\nShield: {shieldfixed}\nLight Ammo: {light.get()} | {ammolll.get()}\nMedium Ammo: {mid.get()} | {ammomm.get()}\nHeavy Ammo: {hvy.get()} | {ammohh.get()}\nShotgun Ammo: {sss.get()} | {ammoss.get()}\nBandage: {bvalue.get()} | {bandagess.get()}\nShiel Recharger: {shr.get()} | {idkimjusttired.get()}\nSmoke: {smok.get()} | {smokee.get()}\nDefibrillator: {deff.get()} | {defibb.get()}\nTime: {timex.get()}")
        tkinter.messagebox.showinfo("PwP", "Cfg Saved Successfuly!")
    except Exception as e:
        print(e)

def cfgload():
    try:
        with open("config.txt", "r") as file:
            linesss = file.readlines()
            cfgmaingun = linesss[0].split()[2]
            cfgsecondgun = linesss[1].split()[2]
            cfgaugument = linesss[2].split()[1]
            cfgshield = linesss[3].split()[1]
            cfglightammo = linesss[4].split()[2]
            cfglightammocount = linesss[4].split()[4]
            cfgmediumammo = linesss[5].split()[2]
            cfgmediumammocount = linesss[5].split()[4]
            cfgheavyammo = linesss[6].split()[2]
            cfgheavyammocount = linesss[6].split()[4]
            cfgshotgunammo = linesss[7].split()[2]
            cfgshotgunammocount = linesss[7].split()[4]
            cfgbandage = linesss[8].split()[1]
            cfgbandagecount = linesss[8].split()[3]
            cfgshieldrecharger = linesss[9].split()[2]
            cfgshieldrechargercount = linesss[9].split()[4]
            cfgsmoke = linesss[10].split()[1]
            cfgsmokecount = linesss[10].split()[3]
            cfgdefibrillator = linesss[11].split()[1]
            cfgdefibrillatorcount = linesss[11].split()[3]
            cfgtime = linesss[12].split()[1]
    except FileNotFoundError as e:
        tkinter.messagebox.showerror("Config Error", "You dont have a saved configuration")
    except Exception as e:
        pass

    if cfglightammo != "False" and int(cfglightammocount) % 25 != 0:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("QwQ", "Light Ammo Value must be divisible by 25.")
        return

    if cfgmediumammo != "False" and int(cfgmediumammocount) % 20 != 0:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("QwQ", "Medium Ammo Value must be divisible by 20.")
        return

    if cfgheavyammo != "False" and int(cfgheavyammocount) % 10 != 0:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("QwQ", "Heavy Ammo Value must be divisible by 10.")
        return

    if cfgshotgunammo != "False" and int(cfgshotgunammocount) % 5 != 0:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("QwQ", "Shotgun Ammo Value must be divisible by 5.")
        return

    if notifb.get():
        tkinter.messagebox.showinfo("UwU", f"You Have {timex.get()} Seconds to open Arc Raiders Main Menu")
    if musicb.get():
        pygame.init()
        pygame.mixer.music.load("./sounds/waiting.mp3")
        pygame.mixer.music.play()
    time.sleep(int(cfgtime))

    if buyb.get():
        clicktotraiders()
        time.sleep(0.5)
        clicktogunshop()
        time.sleep(0.5)

        for item in (cfgmaingun, cfgsecondgun):
            if item != "None":
                buyothers(item, 1)
            focustoback()

        if cfglightammo != "False":
            if cfgmaingun != "None" or cfgsecondgun != "None":
                time.sleep(3.5)
            buyammo("light_ammo", int(cfglightammocount) // 25)
        if cfgmediumammo != "False":
            if cfglightammo != "False":
                time.sleep(3.5)
            buyammo("medium_ammo", int(cfgmediumammocount) // 20)
        if cfgheavyammo != "False":
            if cfgmediumammo != "False":
                time.sleep(3.5)
            buyammo("heavy_ammo", int(cfgheavyammocount) // 10)
        if cfgshotgunammo != "False":
            if cfgheavyammo != "False":
                time.sleep(3.5)
            buyammo("shotgun_ammo", int(cfgshotgunammocount) // 5)

        if cfgaugument != "None" or cfgshield != "None" or cfgbandage != "False" or cfgdefibrillator != "False":
            clicktoclinic()
            time.sleep(0.5)

        if cfgaugument != "None":
            if cfgaugument == "combat":
                pyautogui.press("down")
                pyautogui.press("right")
                makepurchase(1)
            elif cfgaugument == "looting":
                pyautogui.press("down")
                makepurchase(1)
            elif cfgaugument == "tactical":
                pyautogui.press("down")
                pyautogui.press("right")
                pyautogui.press("right")
                makepurchase(1)

        for item in cfgshield:
            if item != "None":
                buyothers(item + "shield", 1)

        if cfgbandage != "False":
            buyothers("bandage", cfgbandagecount)
        if cfgdefibrillator != "False":
            buyothers("defibrillator", cfgdefibrillatorcount)
        if cfgshieldrecharger != "False":
            buyothers("shieldrecharger", cfgshieldrechargercount)

        if cfgsmoke != "False":
            clicktogadgets()
            time.sleep(0.5)
            buyothers("smoke", cfgsmokecount)

        if not sortb.get():
            clicktoback()
            time.sleep(0.5)
            clicktoback()
            try:
                pygame.mixer.music.stop()
            except Exception as e:
                pass

    if sortb.get():
        clicktotab()
        if cfgmaingun != "None" or cfgsecondgun != "None":
            clicktoinvcategory("weapons")
            time.sleep(0.5)
            if cfgmaingun != "None":
                selectgun(cfgmaingun)
            if cfgsecondgun != "None":
                selectgun(cfgsecondgun)

        if cfglightammo != "False" or cfgmediumammo != "False" or cfgheavyammo != "False" or cfgshotgunammo != "False":
            clicktoinvcategory("ammunition")
            time.sleep(0.5)

        if cfglightammo != "False":
            selectammo("light_ammo")
            focustoback()
        if cfgmediumammo != "False":
            selectammo("medium_ammo")
            focustoback()
        if cfgheavyammo != "False":
            selectammo("heavy_ammo")
            focustoback()
        if cfgshotgunammo != "False":
            selectammo("shotgun_ammo")

        if cfgaugument != "None":
            clicktoinvcategory("augments")
            time.sleep(0.5)
            selectothers(cfgaugument+"mk")

        if cfgshield != "None":
            clicktoinvcategory("shields")
            selectothers(cfgshield+"shield")

        if cfgbandage != "False" or cfgdefibrillator != "False" or cfgshieldrecharger != "False":
            clicktoinvcategory("quickuse")
            time.sleep(0.5)
            if cfgbandage != "False":
                selectothers("bandage")
                focustoback()
            if cfgdefibrillator != "False":
                selectothers("defibrillator")
                focustoback()
            if cfgshieldrecharger != "False":
                selectothers("shieldrecharger")
                focustoback()

        if cfgsmoke != "False":
            selectothers("smoke")

        if buyb.get() and sortb.get():
            clicktoback()
            clicktoback()
            clicktoback()
            try:
                pygame.mixer.music.stop()
            except Exception as e:
                pass
        else:
            clicktoback()
            try:
                pygame.mixer.music.stop()
            except Exception as e:
                pass

def load():
    if light.get() and int(ammolll.get()) % 25 != 0:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("QwQ", "Light Ammo Value must be divisible by 25.")
        return

    if mid.get() and int(ammomm.get()) % 20 != 0:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("QwQ", "Medium Ammo Value must be divisible by 20.")
        return

    if hvy.get() and int(ammohh.get()) % 10 != 0:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("QwQ", "Heavy Ammo Value must be divisible by 10.")
        return

    if sss.get() and int(ammoss.get()) % 5 != 0:
        pygame.init()
        pygame.mixer.music.load("./sounds/error.mp3")
        pygame.mixer.music.play()
        tkinter.messagebox.showerror("QwQ", "Shotgun Ammo Value must be divisible by 5.")
        return

    if notifb.get():
        tkinter.messagebox.showinfo("UwU", f"You Have {timex.get()} Seconds to open Arc Raiders Main Menu")
    if musicb.get():
        pygame.init()
        pygame.mixer.music.load("./sounds/waiting.mp3")
        pygame.mixer.music.play()
    time.sleep(int(timex.get()))

    if buyb.get():
        clicktotraiders()
        time.sleep(0.5)
        clicktogunshop()
        time.sleep(0.5)

        if gun.get() != "":
            buygun(gun.get())

        if gun2.get() != "":
            buygun(gun2.get())

        if light.get():
            if gun.get() != "" or gun2.get() != "":
                time.sleep(3.5)
            buyammo("light_ammo", int(ammolll.get()) // 25)

        if mid.get():
            if light.get():
                time.sleep(3.5)
            buyammo("medium_ammo", int(ammomm.get()) // 20)

        if hvy.get():
            if mid.get():
                time.sleep(3.5)
            buyammo("heavy_ammo", int(ammohh.get()) // 10)

        if sss.get():
            if hvy.get():
                time.sleep(3.5)
            buyammo("shotgun_ammo", int(ammoss.get()) // 5)

        if mk.get() != "" or bvalue.get() or deff.get() or shield.get() or shr.get():
            clicktoclinic()
            time.sleep(0.5)

        if mk.get() != "":
            if mk.get() == "combat":
                pyautogui.press("down")
                pyautogui.press("right")
                makepurchase(1)
            elif mk.get() == "looting":
                pyautogui.press("down")
                makepurchase(1)
            elif mk.get() == "tactical":
                pyautogui.press("down")
                pyautogui.press("right")
                pyautogui.press("right")
                makepurchase(1)

        if shield.get() != "":
            buyothers(shield.get() + "shield", 1)

        if bvalue.get():
            buyothers("bandage", bandagess.get())
        if deff.get():
            buyothers("defibrillator", defibb.get())
        if shr.get():
            buyothers("shieldrecharger", idkimjusttired.get())

        if smok.get():
            clicktogadgets()
            time.sleep(0.5)
            buyothers("smoke", smokee.get())

        if not sortb.get():
            try:
                pygame.mixer.music.stop()
            except Exception as e:
                pass

    if sortb.get():
        clicktotab()
        if gun.get() != "" or gun2.get() != "":
            clicktoinvcategory("weapons")
            time.sleep(0.5)
            if gun.get() != "":
                selectgun(gun.get())
                focustoback()
            if gun2.get() != "":
                selectgun(gun2.get())

        if light.get() or mid.get() or hvy.get() or sss.get():
            clicktoinvcategory("ammunition")
            time.sleep(0.5)

        if light.get():
            selectammo("light_ammo")
            focustoback()
        if mid.get():
            selectammo("medium_ammo")
            focustoback()
        if hvy.get():
            selectammo("heavy_ammo")
            focustoback()
        if sss.get():
            selectammo("shotgun_ammo")
        if mk.get() != "":
            clicktoinvcategory("augments")
            time.sleep(0.5)
            selectothers(mk.get()+"mk")


        if shield.get() != "":
            clicktoinvcategory("shields")
            time.sleep(0.5)
            selectothers(shield.get()+"shield")

        if bvalue.get() or deff.get() or shr.get():
            clicktoinvcategory("quickuse")
            time.sleep(0.5)
            if bvalue.get():
                selectothers("bandage")
                focustoback()
            if deff.get():
                selectothers("defibrillator")
                focustoback()
            if shield.get():
                selectothers("shieldrecharger")
                focustoback()

        if smok.get():
            if bvalue.get() or deff.get() or shr.get():
                selectothers("smoke")
            else:
                clicktoinvcategory("quickuse")
                time.sleep(0.5)
                selectothers("smoke")

        if buyb.get() and sortb.get():
            clicktoback()
            clicktoback()
            clicktoback()
        else:
            clicktoback()

        try:
            pygame.mixer.music.stop()
        except Exception as e:
            pass

btn = tk.Button(arcautobuy,command=save, text="SAVE LOADOUT TO CFG")
btn.place(width=200,height=50,relx=0.89,rely=0.75,anchor="center")

btn2 = tk.Button(arcautobuy,command=cfgload, text="LOAD LOADOUT FROM CFG")
btn2.place(width=230,height=50,relx=0.89,rely=0.84,anchor="center")

btn3 = tk.Button(arcautobuy,command=load, text="LOAD LOADOUT")
btn3.place(width=200,height=50,relx=0.89,rely=0.93,anchor="center")

arcautobuy.mainloop()