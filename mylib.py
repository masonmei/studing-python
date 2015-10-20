__author__ = 'mason'


# define class
class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print "hello {0}".format(self._name)


class Engineer(Person):
    def __init__(self, name):
        Person.__init__(self, name)

    def work(self):
        print "Fucking coder {0}".format(self._name)
