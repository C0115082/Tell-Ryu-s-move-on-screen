import numpy as np
import csv
import subprocess
import sys
import glob

args = sys.argv
if(len(args) == 2):
    print("Start...")
else:
    print("Nothing image's pass or Many writing")
    sys.exit()

path = args[1]
subprocess.call("python Chainer_Realtime_Multi-Person_Pose_Estimation/pose_detectorKai.py posenet Chainer_Realtime_Multi-Person_Pose_Estimation/models/coco_posenet.npz --img %s" %path)

#get points
def numpy_maker(thr):
    f = open(thr, 'r')
    mylist = []
    c = csv.reader(f)
    for row in c:
        mylist.append(row)

    aa = np.array(mylist)
    points = np.delete(aa, 2, 1)
    points = points.astype(np.int32)
    b = np.where(points == points[0,0])

    return(points[0],points[b[0][0]+1],points[b[0][1]+1],points[b[0][2]+1],points[b[0][3]+1],points[b[0][4]+1])

#ungle calculation
def kakudo_osieru_man(Ax,Ay,Bx,By,Cx,Cy):
    BA = [Bx-Ax,By-Ay]
    BC = [Bx-Cx,By-Cy]
    
    theta = (BA[0]*BC[0] + BA[1]*BC[1])/(np.sqrt(BA[0]*BA[0] + BA[1]*BA[1]) * np.sqrt(BC[0]*BC[0] + BC[1]*BC[1]))
    ang = np.arccos(theta)
    return np.rad2deg(ang)

def tell_joint_angle(hoge):
    x = numpy_maker(hoge)
    points = np.array(x) #have point:center,rightHip,leftHip,rightShoulder,leftShoulder,head
    leftDown = kakudo_osieru_man(points[4,0],points[4,1],points[0,0],points[0,1],points[2,0],points[2,1])
    under = kakudo_osieru_man(points[2,0],points[2,1],points[0,0],points[0,1],points[1,0],points[1,1])
    rightDown = kakudo_osieru_man(points[1,0],points[1,1],points[0,0],points[0,1],points[3,0],points[3,1])
    rightUp = kakudo_osieru_man(points[3,0],points[3,1],points[0,0],points[0,1],points[5,0],points[5,1])
    leftUp = kakudo_osieru_man(points[5,0],points[5,1],points[0,0],points[0,1],points[4,0],points[4,1])
    return leftDown,under,rightDown,rightUp,leftUp

def angles_dif(ho,ge):
    ho = np.array(ho)
    ge = np.array(ge)
    sa = ho-ge
    return(np.sum(np.absolute(sa)))

def near_dif(database,obj):
    database = np.array(database)
    obj = np.array(obj)
    dif = 1000000 #big number
    num = -1
    for i in range(database.shape[0]):    
        tmp = angles_dif(database[i],obj)
        if(dif > tmp):
            dif = tmp
            num = i
    return(dif,num)

def output_move(database,obj):
    anser = near_dif(database,obj)
    print("This is")
    if anser[1] in{0,18}:
        print("jump large kick")
    elif anser[1] in{1,19}:
        print("jump large punch")
    elif anser[1] in{2,20}:
        print("jump medium kick")
    elif anser[1] in{3,21}:
        print("jump medium punch")
    elif anser[1] in{4,22}:
        print("jump small kick")
    elif anser[1] in{5,23}:
        print("jump small punch")
    elif anser[1] in{6,24}:
        print("large kick")
    elif anser[1] in{7,25}:
        print("large punch")
    elif anser[1] in{8,26}:
        print("medium kick")
    elif anser[1] in{9,27}:
        print("medium punch")
    elif anser[1] in{10,28}:
        print("small kick")
    elif anser[1] in{11,29}:
        print("small punch")
    elif anser[1] in{12,30}:
        print("squat large kick")
    elif anser[1] in{13,31}:
        print("squat large punch")
    elif anser[1] in{14,32}:
        print("squat medium kick")
    elif anser[1] in{15,33}:
        print("squat medium punch")
    elif anser[1] in{16,34}:
        print("squat small kick")
    elif anser[1] in{17,35}:
        print("squat small punch")
    else:
        print("I don't know(maybe proglam erro)")
    print("maybe")

f = open("RyuMoveAngles.csv", 'r')
mylist = []
c = csv.reader(f)
for row in c:
    mylist.append(row)

aa = np.array(mylist)
bb = aa[:,::-1]
database = np.r_[aa,bb]
database = database.astype(np.float32)

obj = tell_joint_angle("point.csv")

output_move(database,obj)
