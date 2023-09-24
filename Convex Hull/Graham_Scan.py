import numpy as np

def OriginCos(p0,p1):
        xLeg = p1[0]-p0[0]
        yLeg = p1[1]-p0[1]
        hyp = np.sqrt(np.power(xLeg,2)+np.power(yLeg,2))
        return xLeg/hyp

def FindInitialPoint(pos_list):
    smol_pos = 0
    for i in range(len(pos_list)):
        if pos_list[smol_pos][0] == pos_list[i][0]:
            if pos_list[smol_pos][1] > pos_list[i][1]:
                smol_pos =i
        elif pos_list[smol_pos][1] > pos_list[i][1]:
            smol_pos = i
    return pos_list[smol_pos]

def SortPoints(pos,p0):
    stack = []
    for i in range(len(pos)):
        if(pos[i] != p0):
            CosVal = OriginCos(p0,pos[i])
            stack.append((CosVal,pos[i]))
    stack.sort(reverse = True)
    return stack

def GrahamScan(pos):
    p0 = FindInitialPoint(pos)
    sorted_points = SortPoints(pos,p0)
    stack = []
    stack.append(p0)
    for i in range(len(sorted_points)):
        if(i==0):
            stack.append(sorted_points[i][1])
        else:
            stack.append(sorted_points[i][1])
            p1 = stack[i-1]
            p2 = stack[i]
            p3 = stack[i+1]
            sign = np.cross([p2[0]-p1[0],p3[0]-p1[0]],[p2[1]-p1[1],p3[1]-p1[1]])
            if(sign <0):
                stack.pop(-2)
    return stack
