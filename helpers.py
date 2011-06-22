# some helper code

# this class is used to convert time to IST
from datetime import tzinfo, timedelta, datetime

class IST(tzinfo):
    def __init__(self):
        self.__offset = timedelta(hours=5, minutes=30)
        self.__dst = timedelta(hours=5, minutes=30)
        self.__name = 'IST'

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return self.__dst
