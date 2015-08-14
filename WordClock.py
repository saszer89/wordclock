class WordClock:
    def stringify(self, time):
        stringified = "it is "

        if time.minute in [59]:
            stringified += str(time.hour + 1) + " " + "o'clock"
        if time.minute in [0]:
            stringified += str(time.hour) + " " + "o'clock"
        else:
            pass
        return stringified
