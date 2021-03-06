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

t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
t3 = t1 + t2
print(t3 - t1)
