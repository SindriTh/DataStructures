import time

class Stopwatch:
    ''' This class encapsulates a stopwatch timer '''
    def __init__(self):
        pass

    def StartTimer(self):
        self.start = time.perf_counter_ns()

    def GetDuration(self):
        return self.stop - self.start

    def StopTimer(self):
        self.stop = time.perf_counter_ns()
