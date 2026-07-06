import os,sys


def add_numbers(a,b ,c=10 ):
  if(a>0 and b>0):
     result=a+b+c
     print( "sum:",result )
  else:
      result=a*b
      print( "product:",result )
  return   result


class   Person:
    def __init__( self ,name ,age):
        self.name=name
        self.age=age

    def greet( self ):
       print("Hello "+self.name )


def process(items):
    total=0
    for i in range(0,len(items)):
        total=total+items[i]
    print( "total:",total )
    return total


data=[1,2,3]

if  __name__=="__main__":
    p=Person( "Alice",22 )
    p.greet()

    value = add_numbers( 1 ,2 )
    print(value)

    process(data)