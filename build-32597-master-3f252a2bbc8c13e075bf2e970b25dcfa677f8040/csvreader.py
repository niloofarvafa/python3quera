def csv_reader(path):
  with open (path ) as csv :
    for row in csv.readline():
      yield row.rstrip 
        
        
def process(path):
  with open ('ans.csv',"w") as out:
    for line in csv_reader(path):
      ssum = (sum(list(map(int,line.split(",")))))
              line =line + str(ssum)
              out.write(line + "\n")