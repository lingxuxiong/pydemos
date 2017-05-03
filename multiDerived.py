class A:
    def __init__(self):
        pass

    def printFeature(self):
        print('Feature name:', 'featureA')


class B:
    def __init__(self):
        pass

    def printFeature(self):
        print('Feature name:', 'featureB')


class MultiDerived(A, B):
    def __init__(self):
        pass

    def printFeature(self):
        print('Feature name:', 'featureAB')
