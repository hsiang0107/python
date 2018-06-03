__author__ = 'twlhgs'
class A(object):
    x=1

class B(A):
    pass

class C(A):
    pass

B.x = 2
print (A.x, B.x, C.x)