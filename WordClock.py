class WordClock:
    def stringify(self, time):
        stringified = "it is "
        stringified += str(time.hour) + " "
        if time.minute != 0:
            pass
        else:
            stringified += "o'clock"
        return stringified
