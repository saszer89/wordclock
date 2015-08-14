class WordClock:
    def stringify(self, time):
        stringified = "it is "

        roundedMin = int((round(time.minute / 5.0)) * 5)

        if roundedMin == 60:
            stringified += str(time.hour + 1) + " o'clock"
        elif roundedMin == 0:
            stringified += str(time.hour) + " o'clock"
        else:
            stringified += str(time.hour) + " " + str(roundedMin)

        return stringified
