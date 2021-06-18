import datetime

try:
    import notify2 as Notifier
except ImportError:
    from plyer import notification as Notifier

from sys import platform
from enums import *

class Clock:

    def __init__(self):
        self.reminders = []
        self.current = ("", "")
        try:
            Notifier.init("Koala")
        except:
            pass
        self.os = Os.Unknown
        self.check_platform()
    
    def check_platform(self):
        if platform == "linux" or platform == "linux2":
            self.os = Os.Linux
        elif platform == "win32":
            self.os = Os.Windows

    def reboot(self, reminders_list):
        self.reminders.clear()
        self.reminders = reminders_list
        sorted(self.reminders)
        self.pick()

    def pick(self):
        if len(self.reminders) > 0:
            self.current = self.reminders[0]
        else:
            self.current = ("0", "0")

    def check(self):
        stamp = datetime.datetime.now().isoformat(timespec='seconds').replace("T", " ")
        if stamp == self.current[0]:
            self.go()

    def check_past(self):
        stamp = datetime.datetime.now().isoformat(timespec='seconds').replace("T", " ")
        if self.current[0] != "0" and stamp >= self.current[0]:
            self.go()
            return True
        return False

    def go(self):
        if self.os == Os.Linux:
            self.go_linux()
        elif self.os == Os.Windows:
            self.go_windows()
        self.next()

    def go_linux(self):
        n = Notifier.Notification(
            "It is time!\n{}\n".format(self.current[0]),
            self.current[1],
            ""
        )
        n.set_urgency(Notifier.URGENCY_CRITICAL)
        n.show()

    def go_windows(self):
        Notifier.notify(
            title = "It is time!\n{}\n".format(self.current[0]),
            message = self.current[1],
            app_icon = None,
            timeout = 60
        )

    def next(self):
        self.reminders.pop(0)
        self.pick()

    def remind_past(self):
        ok = self.check_past()
        while ok:
            ok = self.check_past()
