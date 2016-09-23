import numpy
def func(n):
    n*=n
    func(n)
    print(n)
func(numpy.arange(10**3))
