class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
       """ Create a new MyTime object initialized to hrs, mins, secs.
           The values of mins and secs may be outside the range 0-59,
           but the resulting MyTime object will be normalized.
       """

       # Calculate total seconds to represent
       totalsecs = hrs*3600 + mins*60 + secs
       self.hours = totalsecs // 3600        # Split in h, m, s
       leftoversecs = totalsecs % 3600
       self.minutes = leftoversecs // 60
       self.seconds = leftoversecs % 60

    def __str__(self):
        """ return the hours, minutes and second of a MyTime object."""
        return  "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)

    def to_seconds(self):
        """ Return the number of seconds represented by this instance"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    def between(self, t1, t2):
        """ takes two MyTime objects, t1 and t2, as arguments, and returns True if
        the invoking object falls between the two times.
        Assume t1 <= t2, and make the test closed at the lower bound and open at the
        upper bound, i.e. return True if t1 <= obj < t2"""
        if t1.to_seconds() <= self.to_seconds() < t2.to_seconds():
            return True
        return False

    def __gt__(self, t2):
        """ Return True if I am strictly greater than t2 """
        return self.to_seconds() > t2.to_seconds()

    def increment(self, seconds):
        return self + MyTime(0, 0, seconds)

t1 = MyTime(5, 15, 42)
print('t1: ', t1)
print('t1 - 2 hours (i.e. -7200 seconds): ', t1.increment(-7200))
