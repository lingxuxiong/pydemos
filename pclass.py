class Developer():
    '''This ia a demo class'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Polygon():
    '''Define a polygon shape'''

    def __init__(self, number_of_slides):
        self.num = number_of_slides
        self.slides = [0 for i in range(self.num)]

    def inputSlides(self):
        self.slides = [float(input('Input slide' + str(i + 1) + ':')) for i in range(self.num)]

    def displaySlides(self):
        for i in range(self.num):
            print('Slide', i + 1, ' = ', self.slides[i])


class Triangle(Polygon):
    '''Triangle class derives from Polgon class.'''

    def __init__(self):
        # Polygon.__init__(self, 3)
        super().__init__(3)

    def findArea(self):
        a, b, c = self.slides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('Area is:', area)


class Quadrilateral(Polygon):
    '''Define a Quadrilateral shap with four slides
    '''

    def __init__(self):
        super().__init__(4)


class PowerTwo(object):
    """Class to implement an iterator of power of two"""

    def __init__(self, max):
        super().__init__()
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            p = self.n ** 2
            self.n += 1
            return p
        else:
            raise StopIteration
