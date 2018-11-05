#!/usr/bin/env python
'''This module returns both returns a binomial value in either log 
terms or in integer terms.
'''
import math
import sys
import argparse
import doctest

parser=argparse.ArgumentParser()
parser.add_argument("-n",type=int, help="integer value for total trials")
parser.add_argument("-k",type=int, help="integer value for number of successes")
parser.add_argument("--log",action="store_true", help="if added will return the log value")
parser.add_argument("--test",action="store_true",help="if added will test the choose command. It is incompatible with other flags")
args=parser.parse_args()

if not args.test and __name__=='__main__':
    if args.n<0:
        raise Exception("argument -n must be 0 or positive")

if not args.test and __name__=='__main__':
    if args.k<0:
        raise Exception("argument -k must be 0 or positive")

def runTests():
    print("testing the module...")
    if args.n:
        print("ignoring n for testing purposes")
    import doctest
    doctest.testmod()
    print("done with tests.")

def logfactorial(n,k=0):
    """ returns log values
    >>>logfactorial(3)
    3.1780538303479453
    >>>logfactorial(7)
    8.525161361065415
    >>>logfactorial(5,2)
    4.0943445622221
    >>>logfactorial(6,6)
    0
    >>>logfactorial(5,6)
    0
    """
    assert n>=0, "enter value greater than zero"
    assert type(n)==int, "enter an integer"
    assert k>=0, "Enter greater than 0"
    assert type(k), "Enter integer value"
    if(n>k):
     value=0 
     for i in range(k+1,n+1):
      logi=math.log(i)
      value=value+logi
     return(value)
    else:
     return(0)
    if __name__ == '__main__':
     import doctest
     doctest.testmod()    

def choose(n=args.n,k=args.k,log=args.log):
    '''log returns the log factorial value
    '''
    logvalue=logfactorial(n,k)-logfactorial(n-k)
    if(log):
        return(logvalue)
    else:
        return(int(round(math.exp(logvalue))))

if __name__=='__main__':
    if args.test:
        runTests()
    else:
       print(choose())


