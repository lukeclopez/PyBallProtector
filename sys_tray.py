from pystray import *
import pyball_protector as pyb
from PIL import Image


class SysTrayUI:
    def __init__(self):
        # *** Attributes ***
        self.icon_path = "icon.png"

        # *** Setup Menu ***
        self.menu_items = [
            MenuItem(self.check_status, lambda: pyb.toggle()),
            MenuItem("Test Notification", lambda: pyb.notify_for_break()),
            MenuItem("Settings", lambda: print("Howdy!")),
            MenuItem("Exit", self.exit),
        ]
        self.menu = Menu(*self.menu_items)

        # *** Create System Tray Icon ***
        self.icon = Icon("Test Name", menu=self.menu)
        self.icon.icon = Image.open(self.icon_path)
        self.icon.run()

    def check_status(self, *args):
        if pyb.Status.is_running:
            return "Disable"
        else:
            return "Enable"

    def exit(self, *args):
        if pyb.Status.is_running:
            pyb.disable()
        self.icon.stop()


app = SysTrayUI()
