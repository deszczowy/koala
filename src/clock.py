import datetime
import notify2

class Clock:

    def __init__(self):
        self.reminders = []
        self.current = ("", "")
        notify2.init("Koala")

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
        n = notify2.Notification(
            "It is time!\n{}\n".format(self.current[0]),
            self.current[1],
            ""
        )
        n.set_urgency(notify2.URGENCY_CRITICAL)
        n.show()
        self.next()

    def next(self):
        self.reminders.pop(0)
        self.pick()

    def remind_past(self):
        ok = self.check_past()
        while ok:
            ok = self.check_past()
