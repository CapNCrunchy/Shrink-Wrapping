import matplotlib.pyplot as plt
import numpy as np
import Jarvis_March as jm
import Graham_Scan as gs
import time
    
# make the data
np.random.seed(37)
x = np.random.normal(15, 6, 100)
y = np.random.normal(15, 5, len(x))
Scatter = [(x[i],y[i]) for i in range(len(x))]

plt.ion()
# plot
fig, ax = plt.subplots(figsize=(10, 8))

P1 = gs.FindInitialPoint(Scatter)
ax.scatter(x, y, s=2, c=(0,0,0))
ax.set(xlim=(0, 30),ylim=(0, 30))

m = 4
PointsOnConvexHulls = []
for i in range(int(len(Scatter)/m)):
    pos = Scatter[i*m:i*m+m]
    PointsOnConvexHulls.extend(gs.GrahamScan(pos))

FinalHull = jm.convex_hull(PointsOnConvexHulls)

for i in range(len(FinalHull)):
    if(i==0):
        line = plt.plot([FinalHull[0][0],FinalHull[-1][0]],[FinalHull[0][1],FinalHull[-1][1]],c='b')
    else:
        line = plt.plot([FinalHull[i][0],FinalHull[i-1][0]],[FinalHull[i][1],FinalHull[i-1][1]],c='b')
    print(i)
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.8)
    
