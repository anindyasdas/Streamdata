# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
class Welford(object):
     """ Implements Welford's algorithm for computing a running mean
    and standard deviation as described at: 
        http://www.johndcook.com/standard_deviation.html
    can take single values or iterables
    Properties:
        mean    - returns the mean
        std     - returns the std
        meanfull- returns the mean and std of the mean
    Usage:
        >>> foo = Welford()
        >>> foo(range(100))
        >>> foo
        <Welford: 49.5 +- 29.0114919759>
        >>> foo([1]*1000)
        >>> foo
        <Welford: 5.40909090909 +- 16.4437417146>
        >>> foo.mean
        5.409090909090906
        >>> foo.std
        16.44374171455467
        >>> foo.meanfull
        (5.409090909090906, 0.4957974674244838)
    """
    def __init__(self):
        self.K=0
        self.mean=0
        self.S=0
    def update(self, x):
        if x== None:
            return
        else:
            self.K+=1
            newM= self.mean+(x-self.mean)*1.0/self.K
            newS= self.S+ (x-self.mean)*(x-newM)
            self.mean, self.S= newM, newS
    def consume(self, lst):
        lst=iter(lst)
        for item in lst:
            self.update(item)
    def __call__(self,x):
        '''
       let you use class instances[ins= Welford(), ins([1,2,3])] as function.
       '''
        if hasattr(x,"__iter__"):
            #returns true if the object has specified attr, eg. list has attribute __iter__
            self.consume(x)
        else:
            self.update(x)
            
    @property
    def m(self):
        return (self.mean)
    @property
    def std(self):
        return(math.sqrt(self.S/(self.K-1)))
    @property
    def meanful(self):
        return (self.mean, self.std/math.sqrt(self.K))
    
    def __repr__(self):
        """
        let you use object instance as string
        """
        return ("Welford : {} +- {} ".format(self.mean, self.std))
            
        