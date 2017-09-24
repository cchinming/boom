# -*- coding: utf-8 -*-  
#---------------------------------
#FILENAME:mapp.py
#目的：文化古景点数据分析
#环境：Ubuntu14 python2.7
#FILE:mapp.py,id-level.csv
#TIME:20170924
#---------------------------------
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#----------------paint the map-----------------------
plt.figure(figsize=(20,9))#define size 
m=Basemap(llcrnrlon=70,llcrnrlat=20,urcrnrlon=135,urcrnrlat=55)
m.drawcoastlines(linewidth=1.5)
m.drawcountries(linewidth=1.5)

parallels = np.arange(10.,60,10.) 
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10) # 绘制纬线
meridians = np.arange(70.,135.,10.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10) # 绘制经线
#m.readshapefile('CHN_adm_shp/CHN_adm1', 'states', drawbounds=True)

#------------------read the data---------------------
#x,y=m(np.array([90,93]),np.array([20,43]))
#m.scatter(x,y,10)
filedata=pd.read_csv('id-level.csv')
data_point=np.array(filedata['经纬度'][0:])
lon=[]		#lon
lat=[]		#lat
size=np.array
for i in range(len(data_point)):
	try:
		data=data_point[i].split(',')
		lon.append(float(data[0]))
		lat.append(float(data[1]))
	except:
		pass
else:
	del data_point
	x,y=m(lon,lat)
	m.scatter(x,y,s=40,color='red')
plt.title('view-data in china ')
plt.show()
