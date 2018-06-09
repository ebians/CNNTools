#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

class myCNN():
    def __init__(self, input_size=(4,4), pad=1, stride=1, filter_size=(3,3) ):
        self.iwidth = input_size[0]
        self.iheight = input_size[1]
        self.fwidth = filter_size[0]
        self.fheight = filter_size[1]
        self.padding = pad
        self.stride = stride
    
    def calc(self):
        oh = ( self.iheight + 2*self.padding - self.fheight ) / self.stride + 1
        ow = ( self.iwidth + 2*self.padding - self.fwidth ) / self.stride + 1
        return (ow,oh)

if __name__ == '__main__':
    ins1 = myCNN( input_size=(4,4), pad=1, stride=1, filter_size=(3,3) )
    width, height = ins1.calc()
    print("width = %d, height = %d" % (width, height) )

    ins2 = myCNN( input_size=(7,7), pad=0, stride=2, filter_size=(3,3) )
    width, height = ins2.calc()
    print("width = %d, height = %d" % (width, height) )

    ins3 = myCNN( input_size=(28,31), pad=2, stride=3, filter_size=(5,5) )
    width, height = ins3.calc()
    print("width = %d, height = %d" % (width, height) )

#=======================
#          EOF          
#=======================