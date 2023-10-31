#!/usr/bin/env python3

def sumFromIequals0ToN(n):
    " compute sum 0+1+2+3+...+(n-1)+n "

    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum

def test_sumFromIequals0ToN_0():
    assert sumFromIequals0ToN(0)==0

def test_sumFromIequals0ToN_1():
    assert sumFromIequals0ToN(1)==1

def test_sumFromIequals0ToN_2():
    " 0+1+2=3 "
    assert sumFromIequals0ToN(2)==3

def test_sumFromIequals0ToN_3():
    " 0+1+2+3 = 6 "
    assert sumFromIequals0ToN(3)==6

def test_sumFromIequals0ToN_100():
    " 0+1+2+3+...+100 = 100*101/2 = 5050 "
    assert sumFromIequals0ToN(100)==5050


def factorial(n):
    " compute product 1*2*3*...*n "

    product = 1
    for i in range(1,n+1):
        product = product * i
    return product

def test_factorial_0():
    assert factorial(0)==1

def test_factorial_1():
    assert factorial(1)==1

def test_factorial_2():
    assert factorial(2)==2

def test_factorial_3():
    assert factorial(3)==6

def test_factorial_4():
    assert factorial(4)==24

def test_factorial_10():
    assert factorial(10)==3628800

def list_from_i_to_n(i,n):
    """
    make list [i,i+1,...,n]
    for example:
    list_from_i_to_n(3,7) => [3,4,5,6,7]
    list_from_i_to_n(4,6) => [4,5,6]
    """
    
    result = []
    for j in range(i,n+1):
        result = result + [j]
    return result

def test_list_from_i_to_n_0():
    assert list_from_i_to_n(0,0)==[0]

def test_list_from_i_to_n_1():
    assert list_from_i_to_n(1,5)==[1,2,3,4,5]

def test_list_from_i_to_n_2():
    assert list_from_i_to_n(2,1)==[]

def test_list_from_i_to_n_3():
    assert list_from_i_to_n(3,6)==[3,4,5,6]

def evensOnly(listOfInts):
    """
    return a new list that has only the
    even ints from listOfInts
    """

    result = []
    for x in listOfInts:
       if type(x)==int and x % 2 == 0:   # check something about x
          result.append(x)   # result = result + [x]
    return result


def test_evensOnly_1():
    assert evensOnly([1,2,3,4])==[2,4]

def test_evensOnly_2():
    assert evensOnly([1,3,5])==[]

def test_evensOnly_3():
    assert evensOnly([2,4,6,8,10])==[2,4,6,8,10]

def test_evensOnly_4():
    assert evensOnly([4,1,1,2,8,-4])==[4,2,8,-4]



def stringsLongerThan10(listOfStrings):
    """
    return a new list that has only the
    strings longer than 10
    """
    result = []
    for x in listOfStrings:
       if type(x)==str and len(x)>10:   # check something about x
          result.append(x)   # result = result + [x]
    return result



def test_stringsLongerThan10_1():
    mylist = [
    "UCSB",
    "Cal Poly San Luis Obispo",
    "Stanford",
    "University of West Texas"
        ]
    expected = [
    "Cal Poly San Luis Obispo",
    "University of West Texas"
        ]

    assert stringsLongerThan10(mylist)==expected


if __name__ == "__main__":
    print("factorial(6)=",factorial(6))
