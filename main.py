class Daddy(object):
    y = "y"

    def my_method(self):
        print('anak ni daddy')

    def create(self):
        pass

class Uncle(object):

    def my_method(self):
        print('anak ni pare')

class Mommy(Uncle, Daddy):
    x = "x"

    def my_method(self):
        pass