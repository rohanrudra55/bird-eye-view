import glob
import cv2
import numpy as np
import logging


class TopVis:
    """
    Parameters:
            x_c     = x coordinate on image
            y_c     = y coordinate in image
            mark    = to mark then images
            pt_sv   = to save points on local
            tolog   = to genarate log
            mouse   = to enable mouse read
            count   = count the  number of points read
            width   = output image dimenssion 
            height  = output image dimenssion
            usr_pts = sorce points to transform
            fix_pts = destination points of transform

    Input:
            Image to perfrom transform 
    
    Return:
            Transform image of size dsize
    
    """
    def __init__(self,dsize=[],save=False,log=False,mouse=False,mark=False,frame='',src=[]):
        self.x_c=0
        self.y_c=0
        self.count=0
        self.usr_pts=src
        self.height=dsize[1]
        self.width=dsize[0]
        self.fix_pts=[(0,0),(self.width,0),(0,self.height),(self.width,self.height)]
        self.pt_sv=save
        self.tolog=log
        self.mouse=mouse
        self.mark=mark
        # ERROS HANDEL
        if self.tolog:
            logging.basicConfig(filename='../../../topvis.log',
                            format='%(asctime)s %(message)s',
                            filemode='w')
            print('LOG FILE CREATED')
            self.logger = logging.getLogger()


    def mouseInput(self,event, x, y, flags, param):
        # To read mouse call back and update x,y 
        # coordinate and count number
        
        if event == cv2.EVENT_LBUTTONDOWN:
            self.x_c=x
            self.y_c=y
            self.usr_points.append((x_c,y_c))
            self.count+=1

    def markpt(self,points,src=None,col=(0,0,255)):
        # To mark the points on image

        for point in points:    
            LB = str(point)
            font = cv2.QT_FONT_BLACK
            cv2.putText(src,LB,point,font,1,color=col)
            cv2.circle(src,point,radius=10,color=col,thickness=2)
        return src


    def transform(self,image=None):
        # To transform the image
        
        if image.all()==None:
            self.disable('')
 
        if self.mark and self.mouse:
            if len(self.fix_pts)>0:
                image=self.markpt(self.fix_pts,image)
            if len(self.usr_pts) >0:
                image=self.markpt(self.usr_pts,image,(0,255,0))
        
        else:
            if len(self.fix_pts) == 4 and len(self.fix_pts) == 4:
                self.count=4
                if self.mark or self.mouse:
                    self.disable()
            else:
                pass #ERROR

        if self.count>=4:
            self.mark=False
            src=np.array(self.usr_pts,dtype=np.float32)
            dest=np.array(self.fix_pts,dtype=np.float32)
            try:
                mat=cv2.getPerspectiveTransform(src,dest)
                image=cv2.warpPerspective(image,mat,dsize=(self.width,self.height))
            except AssertionError:
                pass #error
                self.pt_sv=False
        return image
    
    def disable(self,msg):
        # To handel certain wrong inputs 
        #Warning
        self.mark=False
        self.mouse=False
        self.pt_sv=False