

def primeFactors(someInt):
    """
    return a list of the prime factors of
    someInt.

    e.g.
    primeFactors(24)=[2,2,2,3]
    primeFactors(23)=[23]
    primeFactors(25)=[5,5]
    """
    return "stub"
import math

def listOfPrimesLessThanN(n):
    """
    list of all primes less than n
    e.g. listOfPrimesLessThanN(12)=[2,3,5,7,11]
    """
    result = []

    for i in range(2,n):
        if isPrime(i):
           result=result+[i]

    return result

def isPrime(someInt):
    """
    return True if someInt is prime
    otherwise return False

    isPrime(24)=False
    isPrime(23)=True
    """
    if someInt==2:
        return True
    for i in range(2,math.ceil(math.sqrt(someInt))+1):
      if someInt % i == 0:
        return False
    return True

def test_isPrime_2():
    assert isPrime(2)==True

def test_isPrime_3():
    assert isPrime(3)==True

def test_isPrime_4():
    assert isPrime(4)==False

def test_isPrime_5():
    assert isPrime(5)==True
    
def test_isPrime_6():
    assert isPrime(6)==False

def test_isPrime_9():
    assert isPrime(9)==False
    
def test_isPrime_1229():
    assert isPrime(1229)==True

def test_isPrime_1230():
    assert isPrime(1230)==False

def test_isPrime_1231():
    assert isPrime(1231)==True

def test_isPrime_1235():
    assert isPrime(1235)==False

def test_isPrime_1237():
    assert isPrime(1237)==True
    
    
