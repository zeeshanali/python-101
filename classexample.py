__author__ = 'hash1'


class Muslim(object):
    muslim = "success"

    def __init__(self,name):
        self.name = name



    def say_slam(self,msg):
        return "Asslaamoalikum %s and %s" % (msg, self.name)


    @classmethod
    def get_success(cls):
        return cls.muslim



i=Muslim(name="zeeshan")
print i.get_success()
print i.say_slam("ainy")

import math

print math.sqrt(4)





