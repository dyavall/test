import json
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('values')
    parser.add_argument ('tests')
    parser.add_argument ('report')
    return parser

def add(id,values):
        for i in values:
            if id == i["id"]:
                 return i["value"]
            else: continue

def cycle(list,values):
     for i in list:
          id = i["id"]
          add1 = add(id,values)
          i["value"]=add1
          try:
               cycle(i["values"],values)
          except:
               continue
     return list
def main():
     parser = createParser().parse_args()
     with open(parser.tests,'r') as OpFile1:
        tests = json.load(OpFile1)
     with open(parser.values,'r') as OpFile2:
        values = json.load(OpFile2)

     result = cycle(list(tests["tests"]),list(values["values"]))
     tests["tests"]=result
     repord = json.dumps(tests)
     with open(parser.report, "w") as file:
        file.write(repord)


main()
