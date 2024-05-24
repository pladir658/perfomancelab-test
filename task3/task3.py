import sys
file_v = open(sys.argv[1], 'r')
values_js = {}
TempKey = "FalseKey"
for line in file_v:
    if('"id":' in line):
        TempKey = line[line.index('"'):line.index(',')]
        continue
    if('"value":' in line):
        values_js.setdefault(TempKey, line[line.index('"'):line.index("\n")])
file_v.close

file_t = open(sys.argv[2], 'r')
Report = str()
TempKey = "FalseKey"
for line in file_t:
    if('"id":' in line):
        TempKey = line[line.index('"'):line.index(',')]
        Report += line
        continue
    if('"value":' in line):
        Report += line[:line.index('"')] + values_js.get(TempKey,['"value": "",']) + '\n'
    else: Report += line
        
file_t.close
file_r = open(sys.argv[3], 'w')
file_r.write(Report)
file_r.close()