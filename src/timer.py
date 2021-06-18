from PyQt5.QtCore import QTimer

class Timer:

    interval = 7000
    ticking = 1000

    def __init__(self, parent):
        self.parent = parent
        self.schedule = QTimer(parent)
        self.messages = QTimer(parent)
        self.searches = QTimer(parent)
        self.reminder = QTimer(parent)
        self.prepare()
        self.tic = 0

    def prepare(self):
        self.schedule.timeout.connect(self.schedule_tic)
        self.schedule.start(self.interval)

        self.messages.timeout.connect(self.message_tic)
        self.messages.start(self.ticking)

        self.searches.timeout.connect(self.search_tic)
        self.searches.start(self.ticking)

        self.reminder.timeout.connect(self.reminder_tic)
        self.reminder.start(self.ticking)

    def schedule_tic(self):
        self.parent.action_save()
    
    def message_tic(self):
        if self.tic > 0:
            self.tic -= 1
        if self.tic == 1:
            self.parent.clear_message()
    
    def search_tic(self):
        self.parent.search_up()

    def reminder_tic(self):
        self.parent.remind_me()
        
    def start(self):
        self.tic = 5