def main(file1,file2):
    OpFile1 = open(file1)
    circle = OpFile1.readlines()
    CoordinatesCircle = circle[0].split(" ")
    CoordinatesCircle[1] =CoordinatesCircle[1][0]
    OpFile1.close()

    OpFile2 = open(file2)
    points = OpFile2.readlines()
    if(len(points)>100):
        print("Точек больше 100")
        return 0
    for i in points:
        coor = i.split(" ")
        coor[0]=int(coor[0])
        coor[1]=int(coor[1][0])
        coor[0]-=int(CoordinatesCircle[0])
        coor[1]-=int(CoordinatesCircle[1])
        nnn = coor[0]**2+coor[1]**2
        radius = int(circle[1])**2
        if(nnn>radius):
            print(2)
        elif(nnn<radius):
            print(1)
        else :  print(0)
        
main("file1.txt","file2.txt")