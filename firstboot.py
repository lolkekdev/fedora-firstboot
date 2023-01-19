import os
import time
import requests
import scripts.launcher

version = requests.get("https://pastebin.com/raw/GzuDhXXp").text
conutilslist = "inxi, htop, neofetch, vim, ranger, rmtrash, flatpak"
codecslist = "openh264, gstreamer1-libav"


def firststep():
    print("")
    print("Welcome to 1 step of your configuration!")
    print("It's name is ConUtils")
    print("At this stage of setup, you will be prompted to install the basic console software")
    print(f"CLI software that are going to be installed: {conutilslist}")

    conutilsq = input("Proceed with installation? [Y/N] ")
    conutilsq.lower()
    if conutilsq == "y":
        print("Starting installation...")
        scripts.launcher.console()
        os.system("clear")
        print("\r\nDone")
        pass
    elif conutilsq == "n":
        print("Moving to step 2...")
        pass
    else:
        print("Operation aborted.")
        pass


def secondstep():
    print("")
    print("Welcome to 2 step of your configuration!")
    print("It's name is LibCodecs")
    print("At this stage of setup, you will be prompted to install additional audio and video codecs")
    print(f"Codecs that are going to be installed: {codecslist}")
    codecsq = input("Proceed with installation? [Y/N] ")
    codecsq.lower()
    if codecsq == "y":
        print("Starting installation...")
        scripts.launcher.codecs()
        os.system("clear")
        print("\r\nDone")
        pass
    elif codecsq == "n":
        print("Moving to step 3...")
        pass
    else:
        print("Operation aborted.")
        pass

def thirdstep():
    print("")
    print("Welcome to FINAL step of your configuration!")
    print("It's name is LibDeGPU")
    print("At this stage of setup, you will be prompted to install drivers for your GPU (if you have one)")
    print("WARNING! This step is very risky and if You don't want to play games or render videos on your PC, please,"
          "skip this step!")
    gpuq = input("Proceed with installation? [Y/N] ")
    gpuq.lower()
    if gpuq == "y":
        selection = input("Select your GPU Manufacturer [AMD/NVID]")
        selection.lower()
        if selection == "amd":
            print("Your drivers are already in kernel :)")
            pass
        elif selection == "nvid":
            scripts.launcher.nvidiadrivers()
            os.system("clear")
            print("Please, reboot after finishing!")
        else:
            pass
    elif gpuq == "n":
        print("Finishing installation...")
        pass
    else:
        print("Operation aborted.")
        print("Finishing installation...")


os.system("clear")
print("Fedora FirstBoot - Unleash GNU/Linux potential")
print("Made by AverageRussianKid")
print(f"Version: {version}")
print("")
print("This script will help you configure your Fedora GNU/Linux")

confirm = input("Ready to configure your system? [Y/N] ")
confirm.lower()

while confirm != "y" or "" and confirm != "n":
    if confirm == "y" or "":
        pass
    elif confirm == "n":
        print("Come back when you are ready! :)")

firststep()
time.sleep(2)
secondstep()
time.sleep(2)
thirdstep()

print("All done! Exiting in 5 seconds...")
print("Thanks for using my script!")
time.sleep(5)
exit(0)
