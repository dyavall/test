import json
def add(id,result):
        for i in result:
            if id == i["id"]:
                 return i["value"]
            else: continue

def cycle(list,result1):
     for i in list:
          id = i["id"]
          add1 = add(id,result1)
          i["value"]=add1
          try:
               cycle(i["values"],result1)
          except:
               continue
     return list

def main(file1,file2,report):
    with open(file1,'r') as OpFile1:
        result1 = json.load(OpFile1)
    with open(file2,'r') as OpFile2:
        result2 = json.load(OpFile2)
    ppp = list(result1["tests"])
    res = list(result2["values"])
    result = cycle(ppp,res)
    result1["tests"]=result
    record = json.dumps(result1)
    with open(report, "w") as file:
        file.write(record)


main('tests.json','values.json','result.json')