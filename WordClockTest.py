import unittest
import datetime
import WordClock

class WordClockTest(unittest.TestCase):

    def setUp(self):
        self.wordclock = WordClock.WordClock()

    def testNoon(self):
        self.assertEquals(self.wordclock.stringify(datetime.time(12, 0, 0)), "it is 12 o'clock")

if __name__ == '__main__':
    unittest.main()
