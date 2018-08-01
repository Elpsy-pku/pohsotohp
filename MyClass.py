from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Myfunction import *

#子线程类

class CreatmaskHandler(QThread):
    finishSignal = QtCore.pyqtSignal(list)
    def __init__(self, h,w, parent=None):
        super(CreatmaskHandler,  self).__init__(parent)
        self.h=h
        self.w=w
     
    def run(self):
        CreatMask(self.h,self.w)
        self.finishSignal.emit(['done','!'])

class BlendHandler(QThread):
    finishSignal = QtCore.pyqtSignal(str)
    def __init__(self, pos,num, parent=None):
        super(BlendHandler,  self).__init__(parent)
        self.p=pos
        self.n=num

    def run(self):
        if self.n==0:
            blend(Resizemask(self.p),self.p)
        elif self.n==1:
            monblend(Resizemask(self.p),self.p)
        elif self.n==2:
            mixblend(Resizemask(self.p),self.p)
        self.finishSignal.emit('pic/finalimg.png')

class LCCHandler(QThread):
    finishSignal = QtCore.pyqtSignal(str)
    def __init__(self, R,G,B ,parent=None):
        super(LCCHandler,  self).__init__(parent)
        self.R=R
        self.G=G
        self.B=B
     
    def run(self):
        localColorChange(self.R,self.G,self.B)
        self.finishSignal.emit('pic/finalimg.png')