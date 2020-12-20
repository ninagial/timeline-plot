import datetime

class Event(object):
    def __init__(self, label="", date="", desc="", source=""):
        self.label=label
        dsp = [int(x) for x in date.split('-')]
        self.date=datetime.date(*dsp)
        self.desc=desc
        self.source=source
    def __str__(self):
        return "Event: {0} @ {1}".format(self.label, self.date.strftime('%d-%m-%Y'))
        pass

