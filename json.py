import json
import numpy as np
import math
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression


class Region:
    def __init__(self,label_name,x_points,y_points,canvas_width=1200,canvas_heigth=600,ribs_interval=10):
        self.label_name=label_name
        self.x_points=x_points
        self.y_points=y_points
        self.ribs_interval=ribs_interval
        self._canvas_width=canvas_width
        self._canvas_heigth=canvas_heigth
        self.canvas=np.zeros(shape=(self._canvas_heigth,self._canvas_width)).astype(bool)
        self.outline_canvas=np.zeros(shape=(self._canvas_heigth,self._canvas_width)).astype(bool)
        self.central_line_canvas=np.zeros(shape=(self._canvas_heigth,self._canvas_width)).astype(bool)
        self.ribs_canvas=np.zeros(shape=(self._canvas_heigth,self._canvas_width)).astype(bool)
        self.mid_points_x=[]
        self.mid_points_y=[]
        self.__run_area()
        self.__run_outline()
        self.__get_midpoints()
        self.__get_ribs()
        
    def set_canvas(self,canvas_width,canvas_heigth):
        self._canvas_width=canvas_width
        self._canvas_heigth=canvas_heigth
        self.canvas=np.zeros(shape=(self._canvas_heigth,self._canvas_width)).astype(bool)
        self.outline_canvas=np.zeros(shape=(self._canvas_heigth,self._canvas_width)).astype(bool)
        self.central_line_canvas=np.zeros(shape=(self._canvas_heigth,self._canvas_width)).astype(bool)
        self.ribs_canvas=np.zeros(shape=(self._canvas_heigth,self._canvas_width)).astype(bool)
        self.__run_area()
        self.__run_outline()
        self.__get_midpoints()
        self.__get_ribs()
        
    @property
    def area(self):
        self.bitmap=self.canvas.astype(np.uint8)
        return np.sum(self.bitmap)
    
    def plot_outline_and_central_line(self):
        plt.imshow((self.outline_canvas|self.central_line_canvas))
        plt.show()
        
    def plot_outline(self):
        plt.imshow(self.outline_canvas)
        plt.show()
    
    def plot_area(self):
        plt.imshow(self.canvas)
        plt.show()
    
    def __get_ribs(self):
        for i in range(self.ribs_interval,len(self.mid_points_x)-self.ribs_interval,self.ribs_interval):
            orth_slop=-(self.mid_points_x[i]-self.mid_points_x[i-1])/(self.mid_points_y[i]-self.mid_points_y[i-1])
            
            x=int(self.mid_points_x[i])
            y=int(self.mid_points_y[i])
            while( not self.outline_canvas[math.floor(y)][x] and not self.outline_canvas[math.floor(y)+1][x]):
                self.ribs_canvas[math.floor(y)][x]=True
                x=x+1
                y=y+orth_slop
                # plt.imshow((self.outline_canvas|self.central_line_canvas|self.ribs_canvas))
                # plt.show()
            x=int(self.mid_points_x[i])
            y=int(self.mid_points_y[i])
            while( not self.outline_canvas[math.floor(y)][x] and not self.outline_canvas[math.floor(y)+1][x]):
                self.ribs_canvas[math.floor(y)][x]=True
                x=x-1
                y=y-orth_slop
                # plt.imshow((self.outline_canvas|self.central_line_canvas|self.ribs_canvas))
                # plt.show()
        plt.imshow((self.outline_canvas|self.ribs_canvas))
        plt.show()
            
            
    def __get_midpoints(self):
        if (self.label_name =='MG'):
            for i in range(self._canvas_heigth):
                mid_point=self.__get_midpoint(self.outline_canvas[i,:])
                if(mid_point):
                    self.mid_points_x.append(mid_point)
                    self.mid_points_y.append(i)
                    
        elif (self.label_name=='TP'):
            for i in range(self._canvas_width):
                mid_point=self.__get_midpoint(self.outline_canvas[:,i])
                if(mid_point):
                    self.mid_points_x.append(i)
                    self.mid_points_y.append(mid_point())
        self.__midpoints_smoothing()
                    
    def __get_midpoint(self,_1d_array):
        points=[]
        for i in range(len(_1d_array)):
            if(_1d_array[i]):
                points.append(i)
        if(points):
            return int((points[0]+points[-1])/2)
        return None
    
    def __midpoints_smoothing(self):
        x=np.array(self.mid_points_x).reshape(-1,1)
        y=np.array(self.mid_points_y).reshape(-1,1)
        poly = PolynomialFeatures(degree = 2) 
        pr_model=LinearRegression()
        if (self.label_name =='MG'):
            y_poly = poly.fit_transform(y) 
            pr_model.fit(y_poly,x)
            x_pred=pr_model.predict(y_poly)
            self.mid_points_x=x_pred
        elif(self.label_name=='TP'):
            x_poly = poly.fit_transform(x)
            pr_model.fit(x_poly,y)
            y_pred=pr_model.predict(x_poly)
            self.mid_points_y=y_pred
        for i in range(len(self.mid_points_y)):
            self.central_line_canvas[int(self.mid_points_y[i])][int(self.mid_points_x[i])]=True
            
    def __run_outline(self):
        self._x_points=np.append(self.x_points,[self.x_points[0]],axis=0)
        self._y_points=np.append(self.y_points,[self.y_points[0]],axis=0)
        for j in range(len(self._x_points)-1):
            x1=self._x_points[j]
            x2=self._x_points[j+1]
            y1=self._y_points[j]
            y2=self._y_points[j+1]
            
            y_pointer=y1
            x_pointer=x1
                
            if(y2!=y1):
                rate=(x2-x1)/(y2-y1)
                if(y2>y1):
                    while(y_pointer<=y2):
                        self.outline_canvas[y_pointer][math.ceil(x_pointer-rate)]=True
                        for i in range(math.floor(rate)):
                            self.outline_canvas[y_pointer][math.ceil(x_pointer-rate)+i]=True
                        x_pointer=math.floor(x_pointer+rate)
                        y_pointer+=1
                else:
                    while(y_pointer>=y2):
                        self.outline_canvas[y_pointer][math.ceil(x_pointer-rate)]=True
                        for i in range(math.floor(rate)):
                            self.outline_canvas[y_pointer][math.ceil(x_pointer-rate)+i]=True
                        x_pointer=math.floor(x_pointer+rate)
                        y_pointer-=1
            else:
                if(x1<x2):
                    while(x_pointer<=x2):
                        self.outline_canvas[y_pointer][x_pointer]=True
                        x_pointer+=1
                else:
                    while(x_pointer>=x2):
                        self.outline_canvas[y_pointer][x_pointer]=True
                        x_pointer-=1
            # plt.imshow((self.outline_canvas))
            # plt.show()
        
        
    def __run_area(self):
        direction=None
        pivit=[]
        self._x_points=np.append(self.x_points,[self.x_points[0]],axis=0)
        self._y_points=np.append(self.y_points,[self.y_points[0]],axis=0)
        
        for j in range(len(self._x_points)-1):
            x1=self._x_points[j]
            x2=self._x_points[j+1]
            y1=self._y_points[j]
            y2=self._y_points[j+1]
            
            y_pointer=y1
            x_pointer=x1
            if(y2-y1):
                rate=(x2-x1)/(y2-y1)
                
                if(y_pointer<y2):         #direction:true
                    if(direction is None):
                        pass
                    elif(not direction):
                        pivit.append(j)
                    direction=True 
                    while(y_pointer<y2):
                        x_pointer=math.floor(x_pointer+rate)
                        self.__xor_operation(x_pointer,y_pointer)
                        y_pointer+=1
                    
                elif(y_pointer>y2):             #direction:false
                    if(direction is None):
                        pass
                    elif(direction):
                        pivit.append(j)
                    direction=False
                    while(y_pointer>y2):
                        x_pointer=math.floor(x_pointer+rate)
                        self.__xor_operation(x_pointer,y_pointer)
                        y_pointer-=1
        self.__clean_pivit(pivit)
        
    def __xor_operation(self,x,y):
        up=np.zeros((y-1,self._canvas_width)).astype(bool)
        down=np.zeros((self._canvas_heigth-y,self._canvas_width)).astype(bool)
        one=np.ones((1,x)).astype(bool)
        zero=np.zeros((1,self._canvas_width-x)).astype(bool)
        middle=np.append(one,zero,axis=1)
        up=np.append(up,middle,axis=0)
        mask=np.append(up,down,axis=0)
        self.canvas^=mask
    
    def __clean_pivit(self,pivit):
        for i in range(len(pivit)):
            index=pivit[i]
            self.__xor_operation(self._x_points[index], self._y_points[index])
            
        a=0
        while(self._y_points[a]==self._y_points[a+1]):
            a+=1
        if(self._y_points[a]>self._y_points[a+1]):    #向上
            begin_direction=True
        else:
            begin_direction=False                   #向下
        
        b=-1
        while(self._y_points[b]==self._y_points[b-1]):
            b-=1   
        if(self._y_points[b]<self._y_points[b-1]):    #向上
            end_direction=True
        else:                                           #向下
            end_direction=False   
            
        if(begin_direction is not end_direction):
            self.__xor_operation(self._x_points[0],self._y_points[0])
    
    
    
    
    
# class Image:
#     def __init__(self,file_name):
#         self.file_name=file_name
#         self.region_list=[]
#         self.MG_list=[]
#         self.TP_list=[]
    
    
#     def add_region(self,region):
#         self.region_list.append(region)
#         if(region.label_name=="TP"):
#             self.TP_list.append(region)
#         elif(region.label_name=="MG"):
#             self.MG_list.append(region)

#     def plot(self):
#         pass




with open('C:/Users/tnt/Desktop/JSON/test.json','r')as f:
    JSON=json.load(f)
    

item=JSON['P0000000112_LOWER_TRANS.PNG184078']
regions=item['regions']


shape_attributes=(regions[1])['shape_attributes']
all_points_x=shape_attributes['all_points_x']
all_points_y=shape_attributes['all_points_y']
region_attributes=(regions[2])['region_attributes']
label_name=region_attributes['LabelName']  


for k in range(19):
    shape_attributes=(regions[k])['shape_attributes']
    all_points_x=shape_attributes['all_points_x']
    all_points_y=shape_attributes['all_points_y']
    region_attributes=(regions[k])['region_attributes']
    label_name=region_attributes['LabelName']  
    print(label_name)
    reg=Region(label_name,all_points_x,all_points_y)
    # reg.plot_area()
    # reg.plot_outline()
    # reg.plot_outline_and_central_line()



    