import unittest
import datetime
import WordClock

class WordClockTest(unittest.TestCase):

    def setUp(self):
        self.wordclock = WordClock.WordClock()

    def testNoon(self):
        self.assertEquals(self.wordclock.stringify(datetime.time(12, 0, 0)), "it is 12 o'clock")

    def testOneMinuteToFullHour(self):
        self.assertEquals(self.wordclock.stringify(datetime.time(11, 59, 0)), "it is 12 o'clock")

    def testTwoMinutesToFullHour(self):
        self.assertEquals(self.wordclock.stringify(datetime.time(11, 58, 0)), "it is 12 o'clock")

    def testOneMinuteAfterFullHour(self):
        self.assertEquals(self.wordclock.stringify(datetime.time(12, 01, 0)), "it is 12 o'clock")

    def testTwoMinutesAfterFullHour(self):
        self.assertEquals(self.wordclock.stringify(datetime.time(12, 02, 0)), "it is 12 o'clock")

    def testTwoMinutesToTwenty(self):
        self.assertEquals(self.wordclock.stringify(datetime.time(12, 18, 0)), "it is 12 20")

    def testOneMinuteToTwenty(self):
        self.assertEquals(self.wordclock.stringify(datetime.time(12, 19, 0)), "it is 12 20")

    def testOneMinuteAfterTwenty(self):
        self.assertEquals(self.wordclock.stringify(datetime.time(12, 21, 0)), "it is 12 20")

    def testTwoMinutesAfterTwenty(self):
        self.assertEquals(self.wordclock.stringify(datetime.time(12, 22, 0)), "it is 12 20")

    def testThreeMinutesAfterTwenty(self):
        self.assertEquals(self.wordclock.stringify(datetime.time(12, 23, 0)), "it is 12 25")



if __name__ == '__main__':
    unittest.main()
