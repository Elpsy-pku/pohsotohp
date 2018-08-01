# -*- coding: utf-8 -*-
import PIL,sys,PyQt5,matplotlib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PIL import Image,ImageFilter,ImageFont,ImageDraw,ImageEnhance
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from Myfunction import *

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowTitle("Photoshop Pohsotohp!")
        self.setWindowIcon(QIcon("pic/windowicon.png"))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 680)
        self.filename="images/welcome.png"
        self.mplPic="pic/mplpic.png"
        self.mplchaPic="pic/mplchapic.png"
        self.origPic="pic/origPic.png"
        self.chaePic="pic/chaePic.png"
        self.newPic=""

        #主要由Qt Creater生成的部分
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("background-image:url(pic/universe.jpg)")
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_4 = QtWidgets.QWidget(self.centralWidget)
        self.widget_4.setObjectName("widget_4")
        self.widget_4.setStyleSheet("background-image:url(pic/temp1.png)")
        self.verticalLayout_6.addWidget(self.widget_4)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-image:url(pic/temp2.png)")
        self.verticalLayout_3.addWidget(self.widget)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_3 = QtWidgets.QWidget(self.centralWidget)
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setStyleSheet("background-image:url(pic/temp3.png)")
        self.verticalLayout_5.addWidget(self.widget_3)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.centralWidget)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet("background-image:url(pic/temp4.png)")
        self.verticalLayout_4.addWidget(self.widget_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_5 = QtWidgets.QWidget(self.centralWidget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_7.addWidget(self.widget_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolBox = QtWidgets.QToolBox(self.centralWidget)
        self.toolBox.setStyleSheet("font:bold;font-family:微软雅黑;font-size:18px;background-color:rgb(218,185,246);background-image:url(pic/toolbox.jpg)")
        self.toolBox.setObjectName("toolBox")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setGeometry(QtCore.QRect(0, 0, 103, 162))
        self.page_1.setObjectName("page_1")
        self.toolBox.addItem(self.page_1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 103, 162))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 103, 162))
        self.page_3.setObjectName("page_3")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.page_4.setGeometry(QtCore.QRect(0, 0, 103, 162))
        self.toolBox.addItem(self.page_4, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.page_5.setGeometry(QtCore.QRect(0, 0, 103, 162))
        self.toolBox.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.page_6.setGeometry(QtCore.QRect(0, 0, 103, 162))
        self.toolBox.addItem(self.page_6, "")
        self.horizontalLayout_2.addWidget(self.toolBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.setStretch(0, 8)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.widget.raise_()
        self.widget_2.raise_()
        self.widget_3.raise_()
        self.widget_4.raise_()
        self.widget_5.raise_()
        self.widget_4.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.toolBox.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        #--end Qt Creater --

        #工作图片区,以matplotlib为基础
        self.fig = Figure(figsize=(8, 6), dpi=100, tight_layout=True) 
        
        self.fig.set_facecolor("#F5F5F5") 
        self.fig.subplots_adjust(left=0.08, top=0.92, right=0.95, bottom=0.1) 

        self.canvas = FigureCanvas(self.fig) 
        self.ax = self.fig.add_subplot(111) 
        self.ax.set_axis_off() 
        self.picLabel_horizontalLayout = QtWidgets.QHBoxLayout(self.widget_5)
        self.picLabel_horizontalLayout.addWidget(self.canvas)

        #临时保存区
        self.picLabel=QtWidgets.QLabel(self.widget)
        
        self.picLabel2=QtWidgets.QLabel(self.widget_2)
        self.picLabel3=QtWidgets.QLabel(self.widget_3)
        self.picLabel.setStyleSheet("background-color:transparent")
        self.picLabel4=QtWidgets.QLabel(self.widget_4)
        self.picLabel4.setStyleSheet("background-color:transparent")
        self.picLabel2.setStyleSheet("background-color:transparent")
        self.picLabel3.setStyleSheet("background-color:transparent")
        self.picLabel_horizontalLayout1 = QtWidgets.QHBoxLayout(self.widget)
        self.picLabel_horizontalLayout1.addWidget(self.picLabel)
        self.picLabel_horizontalLayout2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.picLabel_horizontalLayout2.addWidget(self.picLabel2)
        self.picLabel_horizontalLayout3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.picLabel_horizontalLayout3.addWidget(self.picLabel3)
        self.picLabel_horizontalLayout4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.picLabel_horizontalLayout4.addWidget(self.picLabel4)
        self.picLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.picLabel.setObjectName('2')
        self.picLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.picLabel2.setObjectName('4')
        self.picLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.picLabel3.setObjectName('3')
        self.picLabel4.setAlignment(QtCore.Qt.AlignCenter)
        self.picLabel4.setObjectName('1')
        self.picLabel.haspic=False
        self.picLabel2.haspic=False
        self.picLabel3.haspic=False
        self.picLabel4.haspic=False

        #之后要用到的滑条的样式表
        self.QSliderSS='''
        QSlider::add-page:Horizontal{background-color: rgb(87, 97, 106);height:4px;}
        QSlider::sub-page:Horizontal{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231,80,229, 255), stop:1 rgba(7,208,255, 255));height:4px;}
        QSlider::groove:Horizontal{background:transparent;height:6px;}
        QSlider::handle:Horizontal{height: 30px;width:8px;margin: -8 0px;}
        '''
        self.QSliderSSR='''
        QSlider::add-page:Horizontal{background-color: rgb(87, 97, 106);height:4px;}
        QSlider::sub-page:Horizontal{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0,30,30, 255), stop:1 rgba(255,30,30, 255));height:4px;}
        QSlider::groove:Horizontal{background:transparent;height:6px;}
        QSlider::handle:Horizontal{height: 30px;width:8px;margin: -8 0px;}
        '''
        self.QSliderSSG='''
        QSlider::add-page:Horizontal{background-color: rgb(87, 97, 106);height:4px;}
        QSlider::sub-page:Horizontal{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30,0,30, 255), stop:1 rgba(30,255,30, 255));height:4px;}
        QSlider::groove:Horizontal{background:transparent;height:6px;}
        QSlider::handle:Horizontal{height: 30px;width:8px;margin: -8 0px;}
        '''
        self.QSliderSSB='''
        QSlider::add-page:Horizontal{background-color: rgb(87, 97, 106);height:4px;}
        QSlider::sub-page:Horizontal{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30,30,255, 255), stop:1 rgba(30,30,255, 255));height:4px;}
        QSlider::groove:Horizontal{background:transparent;height:6px;}
        QSlider::handle:Horizontal{height: 30px;width:8px;margin: -8 0px;}
        '''
        #---------基本操作------------
        self.pageVLayout1= QtWidgets.QVBoxLayout(self.page_1)
        #旋转按钮;
        self.rotate_Button = QtWidgets.QPushButton(self.page_1)
        self.rotate_Button.setMaximumSize(QtCore.QSize(30, 12))
        self.rotate_Button.setMinimumSize(QtCore.QSize(100, 40))
        self.pageVLayout1.addWidget(self.rotate_Button,alignment=QtCore.Qt.AlignCenter)
        self.rotate_Button.setStyleSheet("QPushButton{border-radius:10px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/blueButton.png)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.rotate_Button.setObjectName("rotate_Button")
        self.rotate_Button.clicked.connect(self.rotatePic) 
        
        # 上下翻转
        self.Vflip_Button = QtWidgets.QPushButton(self.page_1)
        self.Vflip_Button.setMaximumSize(QtCore.QSize(30, 12))
        self.Vflip_Button.setMinimumSize(QtCore.QSize(100, 40))
        self.pageVLayout1.addWidget(self.Vflip_Button,alignment=QtCore.Qt.AlignCenter)
        self.Vflip_Button.setStyleSheet("QPushButton{border-radius:10px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/redButton.png)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.Vflip_Button.setObjectName("Vflip_Button")
        self.Vflip_Button.clicked.connect(self.VflipPic)               

        # 左右翻转
        self.Hflip_Button = QtWidgets.QPushButton(self.page_1)
        self.Hflip_Button.setMaximumSize(QtCore.QSize(30, 12))
        self.Hflip_Button.setMinimumSize(QtCore.QSize(100, 40))
        self.pageVLayout1.addWidget(self.Hflip_Button,alignment=QtCore.Qt.AlignCenter)
        self.Hflip_Button.setStyleSheet("QPushButton{border-radius:10px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/purpleButton.png)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.Hflip_Button.setObjectName("Hflip_Button")
        self.Hflip_Button.clicked.connect(self.HflipPic) 
        
        #添加水印
        self.addWatermark_Button = QtWidgets.QPushButton(self.page_1)
        self.addWatermark_Button.setMaximumSize(QtCore.QSize(30, 12))
        self.addWatermark_Button.setMinimumSize(QtCore.QSize(100, 40))
        self.pageVLayout1.addWidget(self.addWatermark_Button,alignment=QtCore.Qt.AlignCenter)
        self.addWatermark_Button.setStyleSheet("QPushButton{border-radius:10px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/greenButton.png)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.addWatermark_Button.setObjectName("addWatermark_Button")
        self.addWatermark_Button.clicked.connect(self.addwatermark)

        #---------高级全局变化-----------
        self.pageVLayout2= QtWidgets.QVBoxLayout(self.page_2)
        # 锐化滑动条：
        self.sharpen_Slider = QtWidgets.QSlider(self.page_2)
        self.sharpen_Slider.setStyleSheet(self.QSliderSS)
        self.sharpen_Slider.setMaximumSize(QtCore.QSize(180, 12))
        self.sharpen_Slider.setMinimumSize(QtCore.QSize(180, 12))
        self.pageVLayout2.addWidget(self.sharpen_Slider,alignment=QtCore.Qt.AlignCenter)
        self.sharpen_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.sharpen_Slider.setObjectName("sharpen_Slider")
        self.sharpen_Slider.valueChanged.connect(self.GlobalChange)
        self.sharpen_Label = QtWidgets.QLabel(self.page_2)
        #self.sharpen_Label.setGeometry(QtCore.QRect(60, 135, 131, 31))
        self.pageVLayout2.addWidget(self.sharpen_Label)
        self.sharpen_Label.setStyleSheet("color:white;background:transparent;margin:0 auto;font:bold;font-family:微软雅黑;")
        self.sharpen_Label.setObjectName("sharpen_Label")
        self.sharpen_Label.setAlignment(QtCore.Qt.AlignCenter)
        # 模糊化滑动条：
        self.blur_Slider = QtWidgets.QSlider(self.page_2)
        self.blur_Slider.setStyleSheet(self.QSliderSS)
        self.blur_Slider.setMaximumSize(QtCore.QSize(180, 12))
        self.blur_Slider.setMinimumSize(QtCore.QSize(180, 12))
        self.pageVLayout2.addWidget(self.blur_Slider,alignment=QtCore.Qt.AlignCenter)
        self.blur_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.blur_Slider.setObjectName("blur_Slider")
        self.blur_Slider.setMinimum(0)
        self.blur_Slider.setMaximum(50)
        self.blur_Slider.valueChanged.connect(self.GlobalChange)
        self.blur_Label = QtWidgets.QLabel(self.page_2)
        self.blur_Label.setStyleSheet("color:white;background:transparent;margin:0 auto;font:bold;font-family:微软雅黑;")
        self.pageVLayout2.addWidget(self.blur_Label)
        self.blur_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.blur_Label.setObjectName("blur_Label")
        # 油画滑动条：
        self.oil_Slider = QtWidgets.QSlider(self.page_2)
        self.oil_Slider.setStyleSheet(self.QSliderSS)
        self.oil_Slider.setMaximumSize(QtCore.QSize(180, 12))
        self.oil_Slider.setMinimumSize(QtCore.QSize(180, 12))
        self.pageVLayout2.addWidget(self.oil_Slider,alignment=QtCore.Qt.AlignCenter)
        self.oil_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.oil_Slider.setObjectName("oil_Slider")
        self.oil_Slider.setMinimum(0)
        self.oil_Slider.setMaximum(30)
        self.oil_Slider.valueChanged.connect(self.GlobalChange) 
        self.oil_Label = QtWidgets.QLabel(self.page_2)
        self.oil_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.pageVLayout2.addWidget(self.oil_Label)
        self.oil_Label.setStyleSheet("color:white;background:transparent;margin:0 auto;font:bold;font-family:微软雅黑;")
        self.oil_Label.setObjectName("oil_Label")
        #保存滑动条设置
        self.saveSlider_Button = QtWidgets.QPushButton(self.page_2)
        self.saveSlider_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.saveSlider_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.pageVLayout2.addWidget(self.saveSlider_Button,alignment=QtCore.Qt.AlignCenter)
        self.saveSlider_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/pinkButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.saveSlider_Button.setObjectName("saveSlider_Button")
        self.saveSlider_Button.clicked.connect(self.saveSlider)
        #间隔
        self.spacerItem = QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.pageVLayout2.addItem(self.spacerItem)
        #浮雕按钮
        self.Emboss_Button = QtWidgets.QPushButton(self.page_2)
        self.pageVLayout2.addWidget(self.Emboss_Button,alignment=QtCore.Qt.AlignCenter)
        self.Emboss_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.Emboss_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.Emboss_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/lightblueButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.Emboss_Button.setObjectName("Emboss_Button")
        self.Emboss_Button.clicked.connect(self.embossFilter) 
        #间隔
        self.spacerItem3 = QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.pageVLayout2.addItem(self.spacerItem3)
        #轮廓按钮
        self.Contour_Button = QtWidgets.QPushButton(self.page_2)
        self.pageVLayout2.addWidget(self.Contour_Button,alignment=QtCore.Qt.AlignCenter)
        self.Contour_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.Contour_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.Contour_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/greyButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.Contour_Button.setObjectName("Contour_Button")
        self.Contour_Button.clicked.connect(self.contourFilter) 
        
        #--------涂鸦--------------
        self.pageVLayout3= QtWidgets.QVBoxLayout(self.page_3)
        #选择画笔颜色
        self.Pen_Button = QtWidgets.QPushButton(self.page_3)
        self.pageVLayout3.addWidget(self.Pen_Button,alignment=QtCore.Qt.AlignCenter)
        self.Pen_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.Pen_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.Pen_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/redButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.Pen_Button.setObjectName("Pen_Button")
        self.Pen_Button.clicked.connect(self.choosepen) 
        #选择填充颜色
        self.Penface_Button = QtWidgets.QPushButton(self.page_3)
        self.pageVLayout3.addWidget(self.Penface_Button,alignment=QtCore.Qt.AlignCenter)
        self.Penface_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.Penface_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.Penface_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/yellowButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.Penface_Button.setObjectName("Penface_Button")
        self.Penface_Button.clicked.connect(self.choosefacec) 
        #选择画笔粗细
        self.Penwidth_Button = QtWidgets.QPushButton(self.page_3)
        self.pageVLayout3.addWidget(self.Penwidth_Button,alignment=QtCore.Qt.AlignCenter)
        self.Penwidth_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.Penwidth_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.Penwidth_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/blueButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.Penwidth_Button.setObjectName("Penwidth_Button")
        self.Penwidth_Button.clicked.connect(self.choosepenwidth) 
        #开始绘图
        self.Paint_Button = QtWidgets.QPushButton(self.page_3)
        self.pageVLayout3.addWidget(self.Paint_Button,alignment=QtCore.Qt.AlignCenter)
        self.Paint_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.Paint_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.Paint_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/purpleButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.Paint_Button.setObjectName("Paint_Button")
        self.Paint_Button.clicked.connect(self.startpaint) 
        #绘图结束
        self.EndPaint_Button = QtWidgets.QPushButton(self.page_3)
        self.pageVLayout3.addWidget(self.EndPaint_Button,alignment=QtCore.Qt.AlignCenter)
        self.EndPaint_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.EndPaint_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.EndPaint_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/greenButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.EndPaint_Button.setObjectName("EndPaint_Button")
        self.EndPaint_Button.clicked.connect(self.endpaint) 

        #--------图像融合-----------
        self.pageVLayout4= QtWidgets.QVBoxLayout(self.page_4)
        #开始绘制感兴趣区域
        self.DrawROI_Button = QtWidgets.QPushButton(self.page_4)
        self.pageVLayout4.addWidget(self.DrawROI_Button,alignment=QtCore.Qt.AlignCenter)
        self.DrawROI_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.DrawROI_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.DrawROI_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/greenButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.DrawROI_Button.setObjectName("Draw_Button")
        self.DrawROI_Button.clicked.connect(self.DrawROI) 
        #开始匹配目标图片合适位置
        self.CoverROI_Button = QtWidgets.QPushButton(self.page_4)
        self.pageVLayout4.addWidget(self.CoverROI_Button,alignment=QtCore.Qt.AlignCenter)
        self.CoverROI_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.CoverROI_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.CoverROI_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/blueButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.CoverROI_Button.setObjectName("Cover_Button")
        self.CoverROI_Button.clicked.connect(self.CoverROI) 
        #开始融合
        self.Blend_Button = QtWidgets.QPushButton(self.page_4)
        self.pageVLayout4.addWidget(self.Blend_Button,alignment=QtCore.Qt.AlignCenter)
        self.Blend_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.Blend_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.Blend_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/purpleButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.Blend_Button.setObjectName("Blend_Button")
        self.Blend_Button.clicked.connect(self.Blend) 
        #高阶融合之纹理融合
        self.MonBlend_Button = QtWidgets.QPushButton(self.page_4)
        self.pageVLayout4.addWidget(self.MonBlend_Button,alignment=QtCore.Qt.AlignCenter)
        self.MonBlend_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.MonBlend_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.MonBlend_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/redButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.MonBlend_Button.setObjectName("MonBlend_Button")
        self.MonBlend_Button.clicked.connect(self.MonBlend) 
        #高阶融合之透明背景融合
        self.MixBlend_Button = QtWidgets.QPushButton(self.page_4)
        self.pageVLayout4.addWidget(self.MixBlend_Button,alignment=QtCore.Qt.AlignCenter)
        self.MixBlend_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.MixBlend_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.MixBlend_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/yellowButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.MixBlend_Button.setObjectName("MixBlend_Button")
        self.MixBlend_Button.clicked.connect(self.MixBlend) 

        #---------局部颜色变化------------
        self.pageVLayout5= QtWidgets.QVBoxLayout(self.page_5)
        #选取颜色改变区域
        self.Chooselocal_Button= QtWidgets.QPushButton(self.page_5)
        #self.saveSlider_Button.setGeometry(QtCore.QRect(60, 310, 141, 51))
        self.pageVLayout5.addWidget(self.Chooselocal_Button,alignment=QtCore.Qt.AlignCenter)
        self.Chooselocal_Button.setMaximumSize(QtCore.QSize(180, 50))
        self.Chooselocal_Button.setMinimumSize(QtCore.QSize(180, 50))
        self.Chooselocal_Button.setStyleSheet("QPushButton{border-radius:5px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/brownButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.Chooselocal_Button.setObjectName("ColorChange_Button")
        self.Chooselocal_Button.clicked.connect(self.DrawROI)
        #R滑块
        self.R_Slider = QtWidgets.QSlider(self.page_5)
        self.pageVLayout5.addWidget(self.R_Slider,alignment=QtCore.Qt.AlignCenter)
        self.R_Slider.setStyleSheet(self.QSliderSSR)
        self.R_Slider.setMaximumSize(QtCore.QSize(180, 15))
        self.R_Slider.setMinimumSize(QtCore.QSize(180, 15))
        self.R_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.R_Slider.setObjectName("R_Slider")
        self.R_Slider.setMinimum(0)
        self.R_Slider.setMaximum(8)
        #self.R_Slider.valueChanged.connect(self.LocalColorChange)
        self.R_Label = QtWidgets.QLabel(self.page_5)
        self.pageVLayout5.addWidget(self.R_Label)
        self.R_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.R_Label.setStyleSheet("color:white;background:transparent;margin:0 auto;font:bold;font-family:微软雅黑;")
        self.R_Label.setObjectName("R_Label")
        #G滑块
        self.G_Slider = QtWidgets.QSlider(self.page_5)
        self.pageVLayout5.addWidget(self.G_Slider,alignment=QtCore.Qt.AlignCenter)
        self.G_Slider.setStyleSheet(self.QSliderSSG)
        self.G_Slider.setMaximumSize(QtCore.QSize(180, 15))
        self.G_Slider.setMinimumSize(QtCore.QSize(180, 15))
        self.G_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.G_Slider.setObjectName("G_Slider")
        self.G_Slider.setMinimum(0)
        self.G_Slider.setMaximum(8)
        #self.G_Slider.valueChanged.connect(self.LocalColorChange)
        self.G_Label = QtWidgets.QLabel(self.page_5)
        self.pageVLayout5.addWidget(self.G_Label)
        self.G_Label.setObjectName("G_Label")
        self.G_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.G_Label.setStyleSheet("color:white;background:transparent;margin:0 auto;font:bold;font-family:微软雅黑;")
        #B滑块
        self.B_Slider = QtWidgets.QSlider(self.page_5)
        self.pageVLayout5.addWidget(self.B_Slider,alignment=QtCore.Qt.AlignCenter)
        self.B_Slider.setStyleSheet(self.QSliderSSB)
        self.B_Slider.setMaximumSize(QtCore.QSize(180, 15))
        self.B_Slider.setMinimumSize(QtCore.QSize(180, 15))
        self.B_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.B_Slider.setObjectName("B_Slider")
        self.B_Slider.setMinimum(0)
        self.B_Slider.setMaximum(8)
        #self.B_Slider.valueChanged.connect(self.LocalColorChange)
        self.B_Label = QtWidgets.QLabel(self.page_5)
        self.pageVLayout5.addWidget(self.B_Label)
        self.B_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.B_Label.setStyleSheet("color:white;background:transparent;margin:0 auto;font:bold;font-family:微软雅黑;")
        self.B_Label.setObjectName("B_Label")
        #开始调整颜色
        self.ColorChange_Button = QtWidgets.QPushButton(self.page_5)
        #self.saveSlider_Button.setGeometry(QtCore.QRect(60, 310, 141, 51))
        self.pageVLayout5.addWidget(self.ColorChange_Button,alignment=QtCore.Qt.AlignCenter)
        self.ColorChange_Button.setMaximumSize(QtCore.QSize(180, 50))
        self.ColorChange_Button.setMinimumSize(QtCore.QSize(180, 50))
        self.ColorChange_Button.setStyleSheet("QPushButton{border-radius:5px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/blackButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.ColorChange_Button.setObjectName("ColorChange_Button")
        self.ColorChange_Button.clicked.connect(self.LocalColorChange)
        self.spacerItem2 = QSpacerItem(20, 98, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.pageVLayout5.addItem(self.spacerItem2)
        
        #--------抠图---------
        self.pageVLayout6= QtWidgets.QVBoxLayout(self.page_6)
        #标注前景
        self.front_Button = QtWidgets.QPushButton(self.page_6)
        self.pageVLayout6.addWidget(self.front_Button,alignment=QtCore.Qt.AlignCenter)
        self.front_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.front_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.front_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/greenButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.front_Button.setObjectName("front_Button")
        self.front_Button.clicked.connect(self.drawfront)
        #标注背景
        self.back_Button = QtWidgets.QPushButton(self.page_6)
        self.pageVLayout6.addWidget(self.back_Button,alignment=QtCore.Qt.AlignCenter)
        self.back_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.back_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.back_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/redButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.back_Button.setObjectName("back_Button")
        self.back_Button.clicked.connect(self.drawback)
        #开始抠图
        self.Cut_Button = QtWidgets.QPushButton(self.page_6)
        self.pageVLayout6.addWidget(self.Cut_Button,alignment=QtCore.Qt.AlignCenter)
        self.Cut_Button.setMaximumSize(QtCore.QSize(120, 40))
        self.Cut_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.Cut_Button.setStyleSheet("QPushButton{border-radius:15px;border:1px;color:black;font-family:微软雅黑;background-image:url(pic/greyButton)}"
        "QPushButton:hover{font:Normal}""QPushButton:pressed{border-style:inset}")
        self.Cut_Button.setObjectName("Cut_Button")
        self.Cut_Button.clicked.connect(self.Grabcut)

        #菜单栏：
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 36))
        self.menuBar.setStyleSheet("background-image:url(pic/menubar.jpg);color:white ;font-size:16px;font-family:微软雅黑;")
        self.menuBar.setObjectName("menuBar")
        #文件菜单：
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        #帮助菜单：
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        #帮助：
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.triggered.connect(self.openhelp) 
        #关于作者：
        self.actionAboutme = QtWidgets.QAction(MainWindow)
        self.actionAboutme.setObjectName("actionAboutme")
        self.actionAboutme.triggered.connect(self.openaboutme) 
        #打开文件：
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.openPic) 
        #保存文件：
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.savePic) 
        
        # 保存到临时保存区：
        self.actionSaveTemp1 = QtWidgets.QAction(MainWindow)
        self.actionSaveTemp1.setObjectName("actionSaveTemp1")
        self.actionSaveTemp1.triggered.connect(self.savePic2Tem1) 
        
        self.actionSaveTemp2 = QtWidgets.QAction(MainWindow)
        self.actionSaveTemp2.setObjectName("actionSaveTemp2")
        self.actionSaveTemp2.triggered.connect(self.savePic2Tem2) 
        
        self.actionSaveTemp3 = QtWidgets.QAction(MainWindow)
        self.actionSaveTemp3.setObjectName("actionSaveTem3")
        self.actionSaveTemp3.triggered.connect(self.savePic2Tem3) 
        
        #退出按钮：
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(QCoreApplication.quit)

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveTemp1)
        self.menuFile.addAction(self.actionSaveTemp2)
        self.menuFile.addAction(self.actionSaveTemp3)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAboutme)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        #一些变量
        self.beforex = None
        self.beforey = None
        self.startx = None
        self.starty = None
        self.nowx=None
        self.nowy=None
        self.verts=[]
        self.codes=[]
        self.count=0 
        self.pressed=False
        self.drawROI=False
        self.haspicopen=False
        self.coverROI=False
        self.rectpos=[]
        self.pen=['black',2,'none']
        self.paint=False
        self.cutimg=False
        self.mask = []
        self.df=False
        self.db=False

        self.retranslateUi(MainWindow) 
        # 设置最开始显示的工具栏
        self.toolBox.setCurrentIndex(0) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #做一些类似显示用户可见的中文的事
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), _translate("MainWindow", "基本操作"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "高级全局图像变换"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "信笔涂鸦"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "图像融合"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("MainWindow", "局部颜色变换"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("MainWindow", "抠图"))
        #
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.actionHelp.setText(_translate("MainWindow", "帮助说明"))
        self.actionAboutme.setText(_translate("MainWindow", "关于作者"))
        self.actionOpen.setText(_translate("MainWindow", "导入文件到工作区"))
        self.actionSave.setText(_translate("MainWindow", "导出文件"))
        self.actionSaveTemp1.setText(_translate("MainWindow", "保存到临时保存区1"))
        self.actionSaveTemp2.setText(_translate("MainWindow", "保存到临时保存区2"))
        self.actionSaveTemp3.setText(_translate("MainWindow", "保存到临时保存区3"))
        self.actionQuit.setText(_translate("MainWindow", "退出"))
        self.rotate_Button.setText(_translate("MainWindow", "旋转"))
        self.Vflip_Button.setText(_translate("MainWindow", "上下翻转"))
        self.Hflip_Button.setText(_translate("MainWindow", "左右翻转"))
        self.addWatermark_Button.setText(_translate("MainWindow", "添加水印"))
        self.blur_Label.setText(_translate("MainWindow", "模糊化"))
        self.sharpen_Label.setText(_translate("MainWindow", "锐化"))
        self.oil_Label.setText(_translate("MainWindow", "油画"))
        self.saveSlider_Button.setText(_translate("MainWindow", "保存以上设置"))
        self.Emboss_Button.setText(_translate("MainWindow", "浮雕效果"))
        self.Contour_Button.setText(_translate("MainWindow", "轮廓显示"))
        self.Pen_Button.setText(_translate("MainWindow", "选择画笔颜色"))
        self.Penface_Button.setText(_translate("MainWindow", "选择填充颜色"))
        self.Penwidth_Button.setText(_translate("MainWindow", "选择画笔粗细"))
        self.Paint_Button.setText(_translate("MainWindow", "开始绘图"))
        self.EndPaint_Button.setText(_translate("MainWindow", "结束绘图"))
        self.DrawROI_Button.setText(_translate("MainWindow", "选择融合源"))
        self.CoverROI_Button.setText(_translate("MainWindow", "选择融合目标"))
        self.Blend_Button.setText(_translate("MainWindow", "普通融合"))
        self.MonBlend_Button.setText(_translate("MainWindow", "纹理融合"))
        self.MixBlend_Button.setText(_translate("MainWindow", "透明背景融合"))
        self.R_Label.setText(_translate("MainWindow", "R分量改变"))
        self.G_Label.setText(_translate("MainWindow", "G分量改变"))
        self.B_Label.setText(_translate("MainWindow", "B分量改变"))
        self.Chooselocal_Button.setText(_translate("MainWindow", "选取待改变颜色区域"))
        self.ColorChange_Button.setText(_translate("MainWindow", "开始改变颜色"))
        self.front_Button.setText(_translate("MainWindow", "标注前景"))
        self.back_Button.setText(_translate("MainWindow", "标注背景"))
        self.Cut_Button.setText(_translate("MainWindow", "开始抠图"))
        self.canvas.mpl_connect('button_press_event', self._onPress)
        self.canvas.mpl_connect('button_release_event', self._onRelease)
        self.canvas.mpl_connect('motion_notify_event', self._onMotion)
        self.R_Slider.setValue(1)
        self.G_Slider.setValue(1)
        self.B_Slider.setValue(1)
        #bgimg = matplotlib.image.imread('pic/bgimg.png')
        #self.fig.figimage(bgimg)
        self.setAcceptDrops(True)
#---------------------------------------------函数部分--------------------------------------
    #CreatMask线程结束对应的回调函数
    def CMEnd(self,words):
        pic=QPixmap('pic/Thumb4.png')
        self.picLabel2.setPixmap(pic)
        self.picLabel2.haspic=True
        self.drawROI=False
        self.ax.cla()
        self.ax.set_axis_off() 
        self.setImageWork('pic/newpic.png')
        self.verts=[]
        self.codes=[]

    #matplotlib鼠标绘图，三种情况：1.画mask的轮廓,release后会自动封闭并去创建mask。
    #2.用矩形框出融合时的目标位置。3.随意涂鸦
    def _onPress(self, event):
        if event.xdata is not None and event.ydata is not None and self.drawROI:
            self.pressed = True
            self.beforex = event.xdata
            self.beforey = event.ydata
            self.startx=self.beforex
            self.starty=self.beforey
            self.verts=[]
            self.codes=[]
            self.verts.append((self.startx,self.starty))
            self.codes.append(Path.MOVETO)
        elif event.xdata is not None and event.ydata is not None and self.coverROI:
            self.pressed = True
            self.beforex = event.xdata
            self.beforey = event.ydata
            self.startx=self.beforex
            self.starty=self.beforey
        elif event.xdata is not None and event.ydata is not None and self.paint:
            self.pressed = True
            self.beforex = event.xdata
            self.beforey = event.ydata
            self.startx=self.beforex
            self.starty=self.beforey
            self.verts.append((self.startx,self.starty))
            self.codes.append(Path.MOVETO)
    def _onMotion(self, event):
        if self.pressed and self.drawROI:
            if event.xdata is not None and event.ydata is not None:
                self.nowx = event.xdata
                self.nowy = event.ydata
            self.verts.append((self.nowx,self.nowy))
            self.codes.append(Path.LINETO)
            self.beforex=self.nowx
            self.beforey=self.nowy
            path = Path(self.verts, self.codes)
            patch = patches.PathPatch(path,facecolor='none',lw=2)
            self.ax.add_patch(patch)
            self.canvas.draw()
        elif self.pressed and self.coverROI:
            if event.xdata is not None and event.ydata is not None:
                self.nowx = event.xdata
                self.nowy = event.ydata
            patch=patches.Rectangle((self.startx,self.starty),self.nowx-self.startx,self.nowy-self.starty,fill=False,edgecolor='blue')
            self.ax.cla()
            self.ax.set_axis_off() 
            self.ax.add_patch(patch)
            image = matplotlib.image.imread('pic/newpic.png')
            self.ax.imshow(image,aspect='equal')
            self.canvas.draw()
        elif self.pressed and self.paint:
            if event.xdata is not None and event.ydata is not None:
                self.nowx = event.xdata
                self.nowy = event.ydata
            self.verts.append((self.nowx,self.nowy))
            self.codes.append(Path.LINETO)
            self.beforex=self.nowx
            self.beforey=self.nowy
            path = Path(self.verts, self.codes)
            patch = patches.PathPatch(path,facecolor=self.pen[2],edgecolor=self.pen[0],lw=self.pen[1])
            self.ax.add_patch(patch)
            self.canvas.draw()
    def _onRelease(self, event):
        if self.pressed and self.drawROI:
            self.pressed = False
            if event.xdata is not None and event.ydata is not None:
                self.nowx = event.xdata
                self.nowy = event.ydata
            self.verts.append((self.nowx,self.nowy))
            self.verts.append((self.startx,self.starty))
            self.codes.append(Path.LINETO)
            self.codes.append(Path.CLOSEPOLY)
            path = Path(self.verts, self.codes)
            patch = patches.PathPatch(path,facecolor='none',lw=2)
            self.ax.add_patch(patch)
            self.canvas.draw()
            self.canvas.print_png('pic/poi.png')
            from MyClass import CreatmaskHandler
            self.cm_process = CreatmaskHandler(self.picLabel2.height(),self.picLabel2.width())
            self.cm_process.finishSignal.connect(self.CMEnd)
            self.cm_process.start()
        elif self.pressed and self.coverROI:
            self.pressed = False
            if event.xdata is not None and event.ydata is not None:
                self.nowx = event.xdata
                self.nowy = event.ydata
            patch=patches.Rectangle((self.startx,self.starty),self.nowx-self.startx,self.nowy-self.starty,fill=False,edgecolor='black')
            self.ax.add_patch(patch)
            self.coverROI=False
            self.ax.cla()
            self.ax.set_axis_off() 
            self.setImageWork('pic/newpic.png')
            self.rectpos=[int(min(self.startx,self.nowx)),int(min(self.nowy,self.starty)),int(max(self.startx,self.nowx)),int(max(self.nowy,self.starty))]
        elif self.pressed and self.paint:
            self.pressed = False
            if event.xdata is not None and event.ydata is not None:
                self.nowx = event.xdata
                self.nowy = event.ydata
            self.verts.append((self.nowx,self.nowy))
            self.codes.append(Path.LINETO)
            path = Path(self.verts, self.codes)
            patch = patches.PathPatch(path,facecolor=self.pen[2],edgecolor=self.pen[0],lw=self.pen[1])
            self.ax.add_patch(patch)
            self.canvas.draw()
    #--end 鼠标绘图 --

    #鼠标拖拽交互
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("Drag-Icon"):
            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()
    
    dragMoveEvent = dragEnterEvent
                
    def dropEvent(self,e):
        if e.mimeData().hasFormat("Drag-Icon"):
            child = self.childAt(e.pos())
            if not child:
                return
            #拖拽到临时保存区
            elif child.__class__==PyQt5.QtWidgets.QLabel and hasattr(child,'haspic') and child.objectName()!='4': 
                data = e.mimeData().data("Drag-Icon")
                stream = QDataStream(data,QIODevice.ReadOnly)
                pix = QPixmap()
                textpoint=QPoint()
                stream >> pix >>textpoint
                num=textpoint.x()
                
                self.setImageTemp(child,num)
                if e.source() == self:
                    e.setDropAction(Qt.MoveAction)
                    e.accept()
                else:
                    e.acceptProposedAction()
            #托拽到工作区
            elif child.__class__==matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg:
                data = e.mimeData().data("Drag-Icon")
                stream = QDataStream(data,QIODevice.ReadOnly)
                pix = QPixmap()
                textpoint=QPoint()
                stream >> pix >>textpoint
                num=textpoint.x()
                text='pic/ThumbOri'+str(num)+'.png'
                self.setImageWork(text)
                if e.source() == self:
                    e.setDropAction(Qt.MoveAction)
                    e.accept()
                else:
                    e.acceptProposedAction()
        else:
            e.ignore()
            
    def mousePressEvent(self,event):
        child = self.childAt(event.pos())
        if not child:
            return
        if child.__class__==PyQt5.QtWidgets.QLabel and  hasattr(child,'haspic') and child.objectName()!='4' and child.haspic:
            pixmap = QPixmap(child.pixmap())
            itemData = QByteArray()
            text=QPoint()
            text.setX(int(child.objectName()))
            text.setY(int(child.objectName()))
            dataStream = QDataStream(itemData, QIODevice.WriteOnly)
            dataStream << pixmap <<text
        
            mimeData = QMimeData()
            mimeData.setData('Drag-Icon', itemData)
        
            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.setPixmap(pixmap)
            drag.setHotSpot(child.pos())
        
            tempPixmap = QPixmap(pixmap)
            painter = QPainter()
            painter.begin(tempPixmap)
            painter.fillRect(pixmap.rect(), QColor(127, 127, 127, 127))
            painter.end()
        else:
            return
        if drag.exec_(Qt.CopyAction | Qt.MoveAction, Qt.CopyAction) == Qt.MoveAction:
            child.show()
        else:
            child.show()
    #end --鼠标拖拽交互

    #setimage的两个函数，分别对应临时保存区和工作区，因为有储存等额外工作，封装一下
    def setImageTemp(self,child,filenum):
        text='pic/Thumb'+str(filenum)+'.png'
        pic=QtGui.QPixmap(text)
        child.setPixmap(pic)
        imPIL = Image.open('pic/ThumbOri'+str(filenum)+'.png') 
        imPIL.save('pic/ThumbOri'+child.objectName()+'.png')
        imPIL = Image.open('pic/Thumb'+str(filenum)+'.png') 
        imPIL.save('pic/Thumb'+child.objectName()+'.png')
        child.haspic=True

    def setImageWork(self,filepath):
        image = matplotlib.image.imread(filepath)
        self.ax.imshow(image,aspect='equal')
        self.canvas.draw()
        self.canvas.print_png(self.mplPic)
        self.temPic=Image.open(filepath)   
        self.temPic.save(self.chaePic)
        self.temPic.save('pic/newpic.png')
        self.newPic='pic/newpic.png'
        self.haspicopen=True
    #--end setimage --

    #帮助和关于作者：
    def openaboutme(self):
        self.setImageWork('pic/aboutme.png')
    def openhelp(self):
        self.setImageWork('pic/help.png')

    #打开和保存：
    def openPic(self):
        address=QFileDialog.getOpenFileName(self,"请选取一张图片","","Image files(*.png *.jpg *.jpeg *.gif);;all files(*.*)")
        self.filename=address[0]    
        if self.filename:
            self.setImageWork(self.filename)

    def savePic(self):
        saveAddress=QFileDialog.getSaveFileName(self,"保存文件","","Image files(*.png);")
        if saveAddress[0]:
            self.temPic=Image.open("pic/chaePic.png")  
            self.temPic.save(saveAddress[0])  
            print(saveAddress[0],"保存成功")

    def savePic2Tem1(self):
        self.pic=QtGui.QPixmap(creatThumb(self.chaePic,self.picLabel.height(),self.picLabel.width(),1))
        self.picLabel4.setPixmap(self.pic)
        self.picLabel4.haspic=True

    def savePic2Tem2(self):
        self.pic=QtGui.QPixmap(creatThumb(self.chaePic,self.picLabel.height(),self.picLabel.width(),2))
        self.picLabel.setPixmap(self.pic)
        self.picLabel.haspic=True

    def savePic2Tem3(self):
        self.pic=QtGui.QPixmap(creatThumb(self.chaePic,self.picLabel.height(),self.picLabel.width(),3))
        self.picLabel3.setPixmap(self.pic)
        self.picLabel3.haspic=True

    # 通过x而不是菜单栏退出，要求确认：
    def closeEvent(self, event): 
        reply = QMessageBox.question(self, 'Message', "你确定要退出吗(：__？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        if reply == QMessageBox.No:
            event.ignore()

    #-----------------------------------功能函数，简单的直接写，复杂的从Myfunction调-----------------------------
    #-------------基本操作函数-------------------
    #顺时针旋转90
    def rotatePic(self):
        if not self.haspicopen:
            return
        pic=Image.open(self.newPic)
        pic=pic.transpose(PIL.Image.ROTATE_90)
        pic.save(self.chaePic)  
        self.setImageWork(self.chaePic)

    #上下翻转
    def VflipPic(self):
        if not self.haspicopen:
            return
        pic=Image.open(self.newPic)
        pic=pic.transpose(PIL.Image.FLIP_TOP_BOTTOM)
        pic.save(self.chaePic)  
        self.setImageWork(self.chaePic)

    #左右翻转
    def HflipPic(self):
        if not self.haspicopen:
            return
        pic=Image.open(self.newPic)
        pic=pic.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        pic.save(self.chaePic)  
        self.setImageWork(self.chaePic)
    
    #添加水印
    def addwatermark(self):
        if not self.haspicopen:
            return
        input=QInputDialog.getText(self, "水印文字","请输入您想添加的文字:",QLineEdit.Normal, "I Love Python")
        colorlist=["red","black","white","yellow","green","blue","orange","pink","grey"]
        color=QInputDialog.getItem(self,"水印颜色","请选择水印颜色",colorlist)
        pic=Image.open(self.newPic)
        pic=add_text_to_image(self.newPic, input[0],color[0])
        pic.save(self.chaePic)  
        self.setImageWork(self.chaePic)
    #-------end基础操作---------

    #-------全局进阶变换--------
    #包括锐化，模糊化，油画（波形滤波），这些都属于可调节参数的filter方法
    def GlobalChange(self):
        if not self.haspicopen:
            return
        pic=Image.open(self.newPic)
        blurvalue=self.blur_Slider.value() 
        sharpenvalue=self.sharpen_Slider.value()
        oilvalue=self.oil_Slider.value()
        pic=pic.filter(ImageFilter.GaussianBlur(radius=blurvalue))#模糊化
        pic=pic.filter(ImageFilter.UnsharpMask(radius=sharpenvalue,percent=300,threshold=3))#锐化
        pic=pic.filter(ImageFilter.ModeFilter(size=oilvalue))#油画
        pic.save(self.chaePic)  
        image = matplotlib.image.imread(self.chaePic)
        self.ax.imshow(image,aspect='equal')
        self.canvas.draw()
    #保存上述设置，从而使展示的图与之后的编辑或保存操作一致
    def saveSlider(self):
        if not self.haspicopen:
            return
        self.setImageWork(self.chaePic)
        self.blur_Slider.setValue(0)
        self.sharpen_Slider.setValue(0)
        self.oil_Slider.setValue(0)
    #浮雕
    def embossFilter(self):
        if not self.haspicopen:
            return
        pic=Image.open(self.newPic)
        pic=pic.filter(ImageFilter.EMBOSS)
        pic.save(self.chaePic)  
        self.setImageWork(self.chaePic)
    #轮廓
    def contourFilter(self):
        if not self.haspicopen:
            return
        pic=Image.open(self.newPic)
        pic=pic.filter(ImageFilter.CONTOUR)
        pic.save(self.chaePic)  
        self.setImageWork(self.chaePic)
    #-------end全局进阶变换--------

    #-------涂鸦-------------
    #选择画笔颜色
    def choosepen(self):
        colorlist=["black","red","white","yellow","green","blue","orange","pink","grey"]
        input=QInputDialog.getItem(self, "画笔颜色","请选择一种画笔的颜色:",colorlist)
        self.pen[0]=input[0]
    def choosefacec(self):
        colorlist=["none","black","red","white","yellow","green","blue","orange","pink","grey"]
        input=QInputDialog.getItem(self, "填充颜色","请选择一种填充颜色，默认为无:",colorlist)
        self.pen[2]=input[0]
    def choosepenwidth(self):
        widthlist=['1','2','3','4','5','6','7','8','9']
        input=QInputDialog.getItem(self, "画笔粗细","请选择线条宽度:",widthlist)
        self.pen[1]=int(input[0])
    def startpaint(self):
        if not self.haspicopen:
            self.setImageWork('pic/blank.png')
        self.paint=True
    def endpaint(self):
        if not self.haspicopen:
            return
        self.canvas.print_png(self.chaePic)
        RectCutting(self.chaePic,245,self.chaePic)
        self.paint=False
        self.verts=[]
        self.codes=[]
        self.ax.cla()
        self.ax.set_axis_off() 
        self.setImageWork(self.chaePic)
    #-------图像融合---------
    #在源图片上用鼠标圈出感兴趣区域
    def DrawROI(self):
        if not self.haspicopen:
            return
        self.drawROI=True
        pic=Image.open(self.mplPic)
        pic.save(self.origPic)
    #框选目标图片对应区域
    def CoverROI(self):
        if not self.picLabel2.haspic:
            reply = QMessageBox.information(self,'message','你尚未选择图像融合操作的源图像')
        else:
            self.coverROI=True
    #普通融合
    def Blend(self):
        if not self.picLabel2.haspic or self.rectpos==[]:
            reply = QMessageBox.information(self,'message','请确保已选择源图像和目标图像')
        else:
            from MyClass import BlendHandler
            self.bd_process = BlendHandler(self.rectpos,0)
            self.bd_process.finishSignal.connect(self.getImageBlend)
            self.bd_process.start()
            #blend(Resizemask(self.rectpos),self.rectpos)
            #self.setImageWork('pic/finalimg.png')
    #仅保留源图像的纹理进行融合
    def MonBlend(self):
        if not self.picLabel2.haspic or self.rectpos==[]:
            reply = QMessageBox.information(self,'message','请确保已选择源图像和目标图像')
        else:
            from MyClass import BlendHandler
            self.bd_process = BlendHandler(self.rectpos,1)
            self.bd_process.finishSignal.connect(self.getImageBlend)
            self.bd_process.start()
    #针对透明或者有洞的情况进行融合
    def MixBlend(self):
        if not self.picLabel2.haspic or self.rectpos==[]:
            reply = QMessageBox.information(self,'message','请确保已选择源图像和目标图像')
        else:
            from MyClass import BlendHandler
            self.bd_process = BlendHandler(self.rectpos,2)
            self.bd_process.finishSignal.connect(self.getImageBlend)
            self.bd_process.start()
    #子线程对应的回调函数
    def getImageBlend(self,path):
        reply = QMessageBox.question(self, 'Message', "图像融合完成了，是否加载到工作区？(按No储存到本地)",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.setImageWork(path)
        if reply == QMessageBox.No:
            saveAddress=QFileDialog.getSaveFileName(self,"保存文件","","Image files(*.png)")
            if saveAddress[0]:
                self.temPic=Image.open("pic/finalimg.png")  
                self.temPic.save(saveAddress[0])  
                print(saveAddress[0],"保存成功")
    #---------end图像融合--------

    #---------局部颜色改变------
    def LocalColorChange(self):
        if not self.picLabel2.haspic:
            reply = QMessageBox.information(self,'message','请确保已选择待改变位置')
        else:
            from MyClass import LCCHandler
            self.lcc_process = LCCHandler(self.R_Slider.value(),self.G_Slider.value(),self.B_Slider.value())
            self.lcc_process.finishSignal.connect(self.getColorChange)
            self.lcc_process.start()
    def getColorChange(self,path):
        self.R_Slider.setValue(1)
        self.G_Slider.setValue(1)
        self.B_Slider.setValue(1)
        reply = QMessageBox.question(self, 'Message', "局部颜色改变完成了，是否加载到工作区？(按No储存到本地)",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.setImageWork(path)
        if reply == QMessageBox.No:
            saveAddress=QFileDialog.getSaveFileName(self,"保存文件","","Image files(*.png)")
            if saveAddress[0]:
                self.temPic=Image.open("pic/finalimg.png")  
                self.temPic.save(saveAddress[0])  
                print(saveAddress[0],"保存成功")
    #-------end局部颜色改变-------

    #-------抠图---------------
    #开始抠图
    #标注前景
    def drawfront(self):
        if not self.haspicopen:
            return
        elif self.cutimg and self.front_Button.text()==u'标注前景':
            reply = QMessageBox.information(self,'message','您已经进行了标注但还没有进行抠图')
            return
        if self.cutimg==False:
            self.canvas.print_png('pic/beforecutPic.png')
            RectCutting('pic/beforecutPic.png',245,'pic/cutgrabPic.png')
            self.cutimg=True
            self.pen=['white',4,'white']
            self.startpaint()
            self.front_Button.setText(u'结束标注')
        else:
            self.endpaint()
            self.pen=['black',2,'none']
            self.front_Button.setText(u'标注前景')
    #标注背景
    def drawback(self):
        if not self.haspicopen:
            return
        elif self.cutimg and self.back_Button.text()==u'标注背景':
            reply = QMessageBox.information(self,'message','您已经进行了标注但还没有进行抠图')
            return
        if self.cutimg==False:
            self.canvas.print_png('pic/beforegrabPic.png')
            RectCutting('pic/beforegrabPic.png',245,'pic/cutgrabPic.png')
            self.cutimg=True
            self.pen=['black',4,'black']
            self.startpaint()
            self.back_Button.setText(u'结束标注')
        else:
            self.endpaint()
            self.pen=['black',2,'none']
            self.back_Button.setText(u'标注背景')
    def Grabcut(self):
        self.cutimg=False
        try:
            import cv2  
        except:
            reply = QMessageBox.information(self,'message','抱歉，但您似乎没有安装opencv')
            return
        try:
            self.mask=np.zeros(cv2.imread('pic/cutgrabPic.png').shape[:2],np.uint8)
            grabcut(self.mask)
            self.setImageWork('pic/finalimg.png')
        except:
            reply = QMessageBox.information(self,'message','抱歉，但似乎您的标注与原图产生了奇妙的化学反应，失败了，QAQ')

qapp=QApplication(sys.argv)
app=Ui_MainWindow()
app.show()
sys.exit(qapp.exec_())
