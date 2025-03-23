import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('n')
    parser.add_argument ('m')
    return parser
def main():

    parser= createParser()
    parser= parser.parse_args()
    n = int(parser.n)
    m = int(parser.m)
    print(parser)
    result = ""
    mass1 = []
    mass2 = []
    i=1
    while i<=n : 
        mass1.append(i) 
        i+=1
    i=0
    while True:
        for y in range(0,m):
            if i==n:
                i=0
            mass2.append(mass1[i])
            if(y<m-1):
                i+=1
        print(mass2)
        result += str(mass2[0])
        if(mass2[m-1]==mass1[0]):
            break
        else : mass2.clear()
    print(result)
main()
