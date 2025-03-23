import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('file1')
    parser.add_argument ('file2')
    return parser

def main():
    parser = createParser().parse_args()

    OpFile1 = open(parser.file1)
    Circle = OpFile1.readlines()
    CoordinatesCircle = Circle[0].split(" ")
    CoordinatesCircle[1]=CoordinatesCircle[1].split("\n")[0]
    OpFile1.close()

    OpFile2 = open(parser.file2)
    points = OpFile2.readlines()
    OpFile2.close()
    if(len(points)<100 ):
        for i in points:
            coor = i.split(" ")
            coor[0]=int(coor[0])
            coor[1]=int(coor[1].split("\n")[0])
            coor[0]-=int(CoordinatesCircle[0])
            coor[1]-=int(CoordinatesCircle[1])
            SummXY = coor[0]**2+coor[1]**2
            radius = int(Circle[1])**2
            if(SummXY>radius):
                print(2)
            elif(SummXY<radius):
                print(1)
            else :  print(0)
    else: print("точек больше 100")
        
main()
