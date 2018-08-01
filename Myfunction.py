from PIL import Image,ImageFilter,ImageFont,ImageDraw,ImageEnhance
import numpy as np
import scipy
from scipy import sparse
import scipy.sparse.linalg as splinalg
import random

#创建缩略图，用于在临时保存区显示
def creatThumb(origpicpath,height,width,num):
	imPIL = Image.open(origpicpath) 
	imPIL.save('pic/ThumbOri'+str(num)+'.png')
	imageSize = imPIL.size
	newpath='pic/Thumb'+str(num)+'.png'
	newheight=height
	newwidth=width
	#调整大小以适应所在Qlabel
	if height>=imageSize[0] and width >=imageSize[1]:
		newheight=imageSize[0]
		newwidth=imageSize[1]
	elif height<imageSize[0] and width<imageSize[0]:
		if height/imageSize[0]<width/imageSize[1]:
			newheight=height
			newwidth=int(height/imageSize[0]*imageSize[1])
		else:
			newwidth=width
			newheight=int(width/imageSize[1]*imageSize[0])
	elif height<imageSize[0]:
		newheight=height
		newwidth=int(height/imageSize[0]*imageSize[1])
	else:
		newwidth=width
		newheight=int(width/imageSize[1]*imageSize[0])
	imPIL=imPIL.resize((newheight,newwidth),Image.ANTIALIAS)
	imPIL.save(newpath)
	return newpath

#向图片中添加文字
def add_text_to_image(imagepath, text,fillColor):
	setFont=ImageFont.truetype('C:/windows/fonts/Dengl.ttf',40)
	image = Image.open(imagepath)
	image=image.convert('RGBA')
	textlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
	draw=ImageDraw.Draw(image)
	textx,texty = draw.textsize(text, font=setFont)
	text_xy = (image.size[0]-textx,image.size[1]-texty)
	draw.text(text_xy, text, font=setFont, fill=fillColor)
	image_with_text = Image.alpha_composite(image, textlay)
	return image_with_text

global V
#广度优先搜索
def bfs(G,s):
	global V
	inf = 1e12
	Q = []
	count = 0
	Q.append(s)
	#V[s[0]][s[1]] = True
	dect=[[0,-1],[0,1],[-1,0],[1,0]]
	while(Q!=[]):
		count+=1
		temp = Q[0]
		if V[temp[0]][temp[1]]==False:
			Q.remove(temp)
			continue;
		V[temp[0]][temp[1]]=False
		for i in range(0,4):
			newx=dect[i][0]+temp[0]
			newy=dect[i][1]+temp[1]
			if newx>=0 and newx<G.shape[0] and newy>=0 and newy<G.shape[1] and not G[newx][newy] and V[newx][newy]:
				Q.append((newx,newy))
		Q.remove(temp)
	return

#最小矩形包络，黑色的背景切出mask或matplotlib的画板中切出原图
def RectCutting(path,basecolor,savepath):
	img=Image.open(path)
	imgarray=np.array(img)
	marcolor=245
	if basecolor>240:
		marcolor=imgarray[0][0][0]
	row=imgarray.shape[0]
	col=imgarray.shape[1]
	#上边界检测
	topedge=-1;
	count=0
	for i in range(0,row):
		count=0
		for j in range(0,col):
			if(basecolor>240):
				if(int(imgarray[i][j][0])!=marcolor or int(imgarray[i][j][1])!=marcolor or int(imgarray[i][j][2])!=marcolor):
					topedge=i
					break
			elif(imgarray[i][j]>basecolor):
				topedge=i
				break
		if topedge!=-1:
			break
	#下边界
	botedge=row;
	for i in range(row-1,-1,-1):
		count=0
		for j in range(0,col):
			if(basecolor>240):
				if(int(imgarray[i][j][0])!=marcolor or int(imgarray[i][j][1])!=marcolor or int(imgarray[i][j][2])!=marcolor):
					botedge=i
					break
			elif(imgarray[i][j]>basecolor):
				botedge=i
				break
		if botedge!=row:
			break
	#左边界
	leftedge=-1;
	for j in range(0,col):
		count=0
		for i in range(0,row):
			if(basecolor>240):
				if(int(imgarray[i][j][0])!=marcolor or int(imgarray[i][j][1])!=marcolor or int(imgarray[i][j][2])!=marcolor):
					leftedge=j
					break
			elif(imgarray[i][j]>basecolor):
				leftedge=j
				break
		if leftedge!=-1:
			break
	#右边界
	rightedge=col;
	for j in range(col-1,-1,-1):
		count=0
		for i in range(0,row):
			if(basecolor>240):
				if(int(imgarray[i][j][0])!=marcolor or int(imgarray[i][j][1])!=marcolor or int(imgarray[i][j][2])!=marcolor):
					rightedge=j
					break
			elif(imgarray[i][j]>basecolor):
				rightedge=j
				break
		if rightedge!=col:
			break

	newimgarr=imgarray[topedge:botedge,leftedge:rightedge]
	newimg=Image.fromarray(np.uint8(newimgarr))
	newimg.save(savepath)
	return [topedge,botedge,leftedge,rightedge,newimgarr,newimg]

#生成mask
def CreatMask(height,width):
	global V
	[t,b,l,r,arr,img]=RectCutting('pic/poi.png',245,'pic/cutpoi.png')
	newimage=img
	[t,b,l,r,arr,img]=RectCutting('pic/origPic.png',245,'pic/cutorigPic.png')
	origimage=img
	origarray=np.array(origimage)
	newarray=np.array(newimage)
	img=(newarray-origarray)
	img[img>0]=255
	img = Image.fromarray(img.astype('uint8')).convert('1')
	img = img.convert('1')
	imgarray=np.array(img)
	V=imgarray.copy()
	V.fill(True)
	bfs(imgarray,(0,0))
	newimg=Image.fromarray(np.uint8(V*255))
	newimg.save('pic/mask.png')
	[t,b,l,r,mask,q]=RectCutting('pic/mask.png',10,'pic/cutmask.png')
	cutorigarr=origarray[t:b,l:r]
	cutorimg=Image.fromarray(cutorigarr.astype('uint8'))
	cutorimg.save('pic/cutrectorigPic.png')#这是待会要用到的源图像的部分
	for i in range(0,cutorigarr.shape[0]):
		for j in range(0,cutorigarr.shape[1]):
			for k in range(0,3):
					cutorigarr[i][j][k]*=int(mask[i][j]>0)
	cutorimg=Image.fromarray(cutorigarr.astype('uint8'))
	cutorimg.save('pic/cutmaskorigPic.png')
	return creatThumb('pic/cutmaskorigPic.png',height,width,4)

#根据目标图像选中的范围重新设置mask的大小
def Resizemask(pos):
	height=pos[2]-pos[0]
	width=pos[3]-pos[1]
	mask=Image.open('pic/cutmask.png')
	origcut=Image.open('pic/cutrectorigPic.png')
	mask=mask.resize((height,width),Image.ANTIALIAS)
	origcut=origcut.resize((height,width),Image.ANTIALIAS)
	return [mask,origcut]

#获得梯度图
def getGrad(img):
	img=img.astype(float)
	extandimg=img.copy().astype(float)
	x=extandimg.shape[0]-1
	y=extandimg.shape[1]-1
	for i in range(1,x):
		for j in range(1,y):
			for k in range(0,3):
				img[i,j,k]=4*extandimg[i,j,k]-extandimg[i,j-1,k]-extandimg[i,j+1,k]-extandimg[i-1,j,k]-extandimg[i+1,j,k]	
	for j in range(1,y):
		for k in range(0,3):
			img[0,j,k]=4*extandimg[0,j,k]-extandimg[0,j-1,k]-extandimg[0,j+1,k]-extandimg[1,j,k]
			img[x,j,k]=4*extandimg[x,j,k]-extandimg[x,j-1,k]-extandimg[x,j+1,k]-extandimg[x-1,j,k]
	for i in range(1,x):
		for k in range(0,3):
			img[i,0,k]=4*extandimg[i,0,k]-extandimg[i,1,k]-extandimg[i+1,0,k]-extandimg[i-1,0,k]
			img[i,y,k]=4*extandimg[i,y,k]-extandimg[i,y-1,k]-extandimg[i+1,y,k]-extandimg[i-1,y,k]
	for k in range(0,3):
		img[0,0,k]=4*extandimg[0,0,k]-extandimg[0,1,k]-extandimg[1,0,k]
		img[0,y,k]=4*extandimg[0,y,k]-extandimg[0,y-1,k]-extandimg[1,y,k]
		img[x,0,k]=4*extandimg[x,0,k]-extandimg[x-1,0,k]-extandimg[x,1,k]
		img[x,y,k]=4*extandimg[x,y,k]-extandimg[x-1,y,k]-extandimg[x,y-1,k]
	return img

#用泊松方程进行梯度域上的融合
def blend(img,pos):
	[mask,srcimg]=img
	targetimg=Image.open('pic/newpic.png').convert('RGB')
	srcimg=srcimg.convert('RGB')
	maskarr=np.array(mask)
	maskarr[0,:] = 0
	maskarr[:,0] = 0
	maskarr[-1,:] = 0 
	maskarr[:,-1] = 0
	srcarr=np.array(srcimg)
	targetarr=np.array(targetimg)
	row_shift=pos[1]
	col_shift=pos[0]
	n=pos[2]-pos[0]
	m=pos[3]-pos[1]
	#获得mask中不是0的点的个数
	num_points=np.sum(maskarr!=0)

	I = np.zeros(num_points).astype(int)
	J = np.zeros(num_points).astype(int)
	count=0;
	for i in range(0,m):
		for j in range(0,n):
			if maskarr[i][j]:
				I[count] = i
				J[count] = j
				count = count+1
	index_matr = np.zeros((m,n)).astype(int);
	index_matr.fill(-1)
	for i in range(0,num_points):
		y = I[i]
		x = J[i]
		index_matr[y,x] = i
	#获得合适的梯度图
	gradimg=getGrad(srcarr)
	A = sparse.lil_matrix((num_points,num_points),dtype=int)
	
	B=np.zeros((num_points,3))

	for y in range(1,m-1):
		for x in range(1,n-1):
			if maskarr[y,x]:
				if maskarr[y-1,x]:
					A[index_matr[y,x],index_matr[y-1,x]] = -1
				else:
					for chnl in range(0,3):
						B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl] + float(targetarr[y-1+row_shift,x+col_shift,chnl])
			

				if maskarr[y,x-1]:
					A[index_matr[y,x],index_matr[y,x-1]] = -1
				else:
					for chnl in range(0,3):
						B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl]+ float(targetarr[y+row_shift,x-1+col_shift,chnl])
	
				if maskarr[y+1,x]:
					A[index_matr[y,x],index_matr[y+1,x]] = -1
				else:
					for chnl in range(0,3):
						B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl] + float(targetarr[y+1+row_shift,x+col_shift,chnl])
	
				if maskarr[y,x+1]:
					A[index_matr[y,x],index_matr[y,x+1]] = -1
				else:
					for chnl in range(0,3):
						B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl] + float(targetarr[y+row_shift,x+1+col_shift,chnl])
	

				for  chnl in range(0,3):
					B[index_matr[y,x]][chnl]= B[index_matr[y,x]][chnl] + gradimg[y,x,chnl]
				
				A[index_matr[y,x],index_matr[y,x]] = 4
	r = splinalg.cg(A, B[:,0])[0]
	g = splinalg.cg(A, B[:,1])[0]
	b = splinalg.cg(A, B[:,2])[0]
	final_img=targetarr.astype(float)
	for k in range(0,num_points):
		if r[k]<0:
			r[k]=0
		if g[k]<0:
			g[k]=0
		if b[k]<0:
			b[k]=0
		final_img[I[k]+row_shift,J[k]+col_shift,0] = min(255, r[k])
		final_img[I[k]+row_shift,J[k]+col_shift,1] =  min(255,g[k])
		final_img[I[k]+row_shift,J[k]+col_shift,2] =  min(255,b[k])
	final_img = final_img.astype(np.uint8)
	finalimg=Image.fromarray(final_img,'RGB')
	finalimg.save('pic/finalimg.png')

#将srcimg三个频道都转为其灰度图的值，再做blend的操作，相当于只保留纹理，不保留颜色
def monblend(img,pos):
	[mask,srcimg]=img
	targetimg=Image.open('pic/newpic.png').convert('RGB')
	srcimg=srcimg.convert('RGB')
	srcgray=srcimg.convert('L')
	maskarr=np.array(mask)
	maskarr[0,:] = 0
	maskarr[:,0] = 0
	maskarr[-1,:] = 0 
	maskarr[:,-1] = 0
	srcarr=np.array(srcimg)
	srcgrarr=np.array(srcgray)
	targetarr=np.array(targetimg)
	row_shift=pos[1]
	col_shift=pos[0]
	n=pos[2]-pos[0]
	m=pos[3]-pos[1]
	#获得mask中不是0的点的个数
	num_points=np.sum(maskarr!=0)

	I = np.zeros(num_points).astype(int)
	J = np.zeros(num_points).astype(int)
	count=0;
	for i in range(0,m):
		for j in range(0,n):
			if maskarr[i][j]:
				I[count] = i
				J[count] = j
				count = count+1
	index_matr = np.zeros((m,n)).astype(int);
	index_matr.fill(-1)
	for i in range(0,num_points):
		y = I[i]
		x = J[i]
		index_matr[y,x] = i
	#获得合适的梯度图
	srcarr[:,:,0]=srcgrarr
	srcarr[:,:,1]=srcgrarr
	srcarr[:,:,2]=srcgrarr
	gradimg=getGrad(srcarr)
	A = sparse.lil_matrix((num_points,num_points),dtype=int)
	
	B=np.zeros((num_points,3))

	for y in range(1,m-1):
		for x in range(1,n-1):
			if maskarr[y,x]:
				if maskarr[y-1,x]:
					A[index_matr[y,x],index_matr[y-1,x]] = -1
				else:
					for chnl in range(0,3):
						B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl] + float(targetarr[y-1+row_shift,x+col_shift,chnl])
			

				if maskarr[y,x-1]:
					A[index_matr[y,x],index_matr[y,x-1]] = -1
				else:
					for chnl in range(0,3):
						B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl]+ float(targetarr[y+row_shift,x-1+col_shift,chnl])
	
				if maskarr[y+1,x]:
					A[index_matr[y,x],index_matr[y+1,x]] = -1
				else:
					for chnl in range(0,3):
						B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl] + float(targetarr[y+1+row_shift,x+col_shift,chnl])
	
				if maskarr[y,x+1]:
					A[index_matr[y,x],index_matr[y,x+1]] = -1
				else:
					for chnl in range(0,3):
						B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl] + float(targetarr[y+row_shift,x+1+col_shift,chnl])
	

				for  chnl in range(0,3):
					B[index_matr[y,x]][chnl]= B[index_matr[y,x]][chnl] + gradimg[y,x,chnl]
				
				A[index_matr[y,x],index_matr[y,x]] = 4
	r = splinalg.cg(A, B[:,0])[0]
	g = splinalg.cg(A, B[:,1])[0]
	b = splinalg.cg(A, B[:,2])[0]
	final_img=targetarr.astype(float)
	for k in range(0,num_points):
		if r[k]<0:
			r[k]=0
		if g[k]<0:
			g[k]=0
		if b[k]<0:
			b[k]=0
		final_img[I[k]+row_shift,J[k]+col_shift,0] = min(255, r[k])
		final_img[I[k]+row_shift,J[k]+col_shift,1] =  min(255,g[k])
		final_img[I[k]+row_shift,J[k]+col_shift,2] =  min(255,b[k])
	final_img = final_img.astype(np.uint8)
	finalimg=Image.fromarray(final_img,'RGB')
	finalimg.save('pic/finalimg.png')

#与blend相比，梯度从取源图的变为取源图与目标图梯度较大的那一个的，可以处理透明的或者非实心的图的融合
def mixblend(img,pos):
	[mask,srcimg]=img
	targetimg=Image.open('pic/newpic.png').convert('RGB')
	srcimg=srcimg.convert('RGB')
	maskarr=np.array(mask)
	maskarr[0,:] = 0
	maskarr[:,0] = 0
	maskarr[-1,:] = 0 
	maskarr[:,-1] = 0
	srcarr=np.array(srcimg)
	targetarr=np.array(targetimg)
	row_shift=pos[1]
	col_shift=pos[0]
	n=pos[2]-pos[0]
	m=pos[3]-pos[1]
	#获得mask中不是0的点的个数
	num_points=np.sum(maskarr!=0)

	I = np.zeros(num_points).astype(int)
	J = np.zeros(num_points).astype(int)
	count=0;
	for i in range(0,m):
		for j in range(0,n):
			if maskarr[i][j]:
				I[count] = i
				J[count] = j
				count = count+1		
	index_matr = np.zeros((m,n)).astype(int);
	index_matr.fill(-1)
	for i in range(0,num_points):
		y = I[i]
		x = J[i]
		index_matr[y,x] = i
	A = sparse.lil_matrix((num_points,num_points),dtype=int)
	srcarr=srcarr.astype(float)
	targetarr=targetarr.astype(float)
	B=np.zeros((num_points,3))

	for y in range(1,m-1):
		for x in range(1,n-1):
			if maskarr[y,x]:
				if maskarr[y-1,x]:
					A[index_matr[y,x],index_matr[y-1,x]] = -1
				else:
					for chnl in range(0,3):
						B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl] + float(targetarr[y-1+row_shift,x+col_shift,chnl])
			

				if maskarr[y,x-1]:
					A[index_matr[y,x],index_matr[y,x-1]] = -1
				else:
					for chnl in range(0,3):
						B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl]+ float(targetarr[y+row_shift,x-1+col_shift,chnl])
	
				if maskarr[y+1,x]:
					A[index_matr[y,x],index_matr[y+1,x]] = -1
				else:
					for chnl in range(0,3):
						B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl] + float(targetarr[y+1+row_shift,x+col_shift,chnl])
	
				if maskarr[y,x+1]:
					A[index_matr[y,x],index_matr[y,x+1]] = -1
				else:
					for chnl in range(0,3):
						B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl] + float(targetarr[y+row_shift,x+1+col_shift,chnl])
	

				for dir_grad in [-1,1]:
					for chnl in range(0,3):
						num1 = targetarr[y,x,chnl]-targetarr[y-dir_grad,x,chnl]
						num2 = srcarr[y,x,chnl] - srcarr[y-dir_grad,x,chnl]
						if abs(num1) > abs(num2):
							B[index_matr[y,x],chnl] = B[index_matr[y,x],chnl] + num1;
						else:
							B[index_matr[y,x],chnl] = B[index_matr[y,x],chnl] + num2;
						num1 = targetarr[y,x,chnl]-targetarr[y,x-dir_grad,chnl]
						num2 = srcarr[y,x,chnl] - srcarr[y,x-dir_grad,chnl]
						if abs(num1) > abs(num2):
							B[index_matr[y,x],chnl] = B[index_matr[y,x],chnl] + num1;
						else:
							B[index_matr[y,x],chnl] = B[index_matr[y,x],chnl] + num2;
				
				A[index_matr[y,x],index_matr[y,x]] = 4
	r = splinalg.cg(A, B[:,0])[0]
	g = splinalg.cg(A, B[:,1])[0]
	b = splinalg.cg(A, B[:,2])[0]
	final_img=targetarr.astype(float)
	for k in range(0,num_points):
		if r[k]<0:
			r[k]=0
		if g[k]<0:
			g[k]=0
		if b[k]<0:
			b[k]=0
		final_img[I[k]+row_shift,J[k]+col_shift,0] = min(255, r[k])
		final_img[I[k]+row_shift,J[k]+col_shift,1] =  min(255,g[k])
		final_img[I[k]+row_shift,J[k]+col_shift,2] =  min(255,b[k])
	final_img = final_img.astype(np.uint8)
	finalimg=Image.fromarray(final_img,'RGB')
	finalimg.save('pic/finalimg.png')

#局部颜色变换
def localColorChange(R,G,B):
	targetimg=Image.open('pic/cutorigPic.png').convert('RGB')
	mask=Image.open('pic/mask.png').convert('1')
	maskarr=np.array(mask)
	maskarr[0,:] = 0
	maskarr[:,0] = 0
	maskarr[-1,:] = 0 
	maskarr[:,-1] = 0
	m=maskarr.shape[0]
	n=maskarr.shape[1]
	targetarr=np.array(targetimg).astype(float)
	srcarr=np.array(targetimg).astype(float)

	#获得mask中不是0的点的个数
	num_points=np.sum(maskarr!=0)

	I = np.zeros(num_points).astype(int)
	J = np.zeros(num_points).astype(int)
	count=0;
	for i in range(0,m):
		for j in range(0,n):
			if maskarr[i][j]:
				I[count] = i
				J[count] = j
				count = count+1		
	index_matr = np.zeros((m,n)).astype(int);
	index_matr.fill(-1)
	for i in range(0,num_points):
		y = I[i]
		x = J[i]
		index_matr[y,x] = i

	srcarr[:,:,0]=srcarr[:,:,0]*R
	srcarr[:,:,1]=srcarr[:,:,1]*G
	srcarr[:,:,2]=srcarr[:,:,2]*B
	srcarr[srcarr>255]=255

	gradimg=getGrad(srcarr)
	A = sparse.lil_matrix((num_points,num_points),dtype=int)
	
	B=np.zeros((num_points,3))

	for y in range(1,m-1):
		for x in range(1,n-1):
			if maskarr[y,x]:
				for dir_grad in [-1,1]:
					if maskarr[y,x+dir_grad] == 1:
						A[index_matr[y,x],index_matr[y,x+dir_grad]] = -1
					else:
						for chnl in range(0,3):
							B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl] + float(targetarr[y,x+dir_grad,chnl])
					if maskarr[y+dir_grad,x] == 1:
						A[index_matr[y,x],index_matr[y+dir_grad,x]] = -1
					else:
						for chnl in range(0,3):
							B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl] + float(targetarr[y+dir_grad,x,chnl])
				for chnl in range(0,3):
					B[index_matr[y,x]][chnl] = B[index_matr[y,x]][chnl] + gradimg[y,x,chnl]
				A[index_matr[y,x],index_matr[y,x]] = 4
			
	r = splinalg.cg(A, B[:,0])[0]
	g = splinalg.cg(A, B[:,1])[0]
	b = splinalg.cg(A, B[:,2])[0]
	final_img=targetarr.astype(float)
	for k in range(0,num_points):
		if r[k]<0:
			r[k]=0
		if g[k]<0:
			g[k]=0
		if b[k]<0:
			b[k]=0
		final_img[I[k],J[k],0] = min(255, r[k])
		final_img[I[k],J[k],1] =  min(255,g[k])
		final_img[I[k],J[k],2] =  min(255,b[k])
	final_img = final_img.astype(np.uint8)
	finalimg=Image.fromarray(final_img,'RGB')
	finalimg.save('pic/finalimg.png')

def grabcut(mask):
	import cv2
	origimg=cv2.imread('pic/cutgrabPic.png')
	newimg=cv2.imread('pic/chaePic.png')
	imag=origimg.astype(int)-newimg.astype(int)
	for i in range (0,mask.shape[0]):
		for j in range (0,mask.shape[1]):
			if imag[i][j][0]+imag[i][j][1]+imag[i][j][2]==0:
				mask[i][j]=random.randint(2,3)
			elif imag[i][j][0]+imag[i][j][1]+imag[i][j][2]<0:
				mask[i][j]=1
			else:
				mask[i][j]=0
	bgModel = np.zeros((1,65),np.float64)
	fgModel = np.zeros((1,65),np.float64)
	mask, bgModel, fgModel = cv2.grabCut(origimg,mask,None,bgModel,fgModel,5,cv2.GC_INIT_WITH_MASK)
	mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
	origimg = origimg*mask[:,:,np.newaxis]
	cv2.imwrite('pic/finalimg.png',origimg)
	return mask