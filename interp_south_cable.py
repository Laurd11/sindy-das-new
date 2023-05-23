import numpy as np
from pyproj import Proj
import matplotlib.pyplot as plt

## Cable lat/lon from Excel sheet
tmp = np.genfromtxt('south_cable_latlon.txt')
lat = tmp[:,0]
lon = tmp[:,1]

## Beach and repeater (optical) distances from data
d0 = 1884
d1 = 94762

## Set up DAS geometry
nc = 47500       # number of channels in 2-m data
dc = 2           # channel spacing
c = np.arange(nc,dtype=int)
c0 = int(d0//dc)
c1 = int(d1//dc) # channel numbers of beginning and end
c = c[c0:c1+1]   # cut off beginning and ending channels
nc = len(c)      # new number of channels
d = np.arange(nc)*dc # distance from first good channel

## Convert cable coordinates to northing/easting
myProj = Proj("+proj=utm +zone=10, +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
x,y = myProj(lon,lat)

## Calculate (geographic) distance along cable track
xd = np.diff(x)
yd = np.diff(y)
distd = np.sqrt(xd**2 + yd**2)
u = np.cumsum(distd)
u = np.hstack(([0],u))

## Interpolate channel locations in x,y
du = np.linspace(0,u.max(),nc)
xn = np.interp(du,u,x)
yn = np.interp(du,u,y)

## Note discrepancy between geographic and optical channel spacing
print('Optical channel spacing, ', dc)
print('Geographic channel spacing, ',du[1]-du[0])

## Convert channel locations back to lat/lon
lonn,latn = myProj(xn,yn,inverse=True)

## Plot
plt.figure()
cb = plt.scatter(lon,lat,c=u,cmap='jet')
plt.plot(lonn,latn,'k')
plt.colorbar(cb)
#plt.gca().set_aspect('equal')
plt.title('Cable points')

## Save
#np.savetxt('south_DAS_latlon.txt',np.column_stack((c,latn,lonn)))

plt.show()
