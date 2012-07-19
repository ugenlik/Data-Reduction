import csv
import math

def histogram(fn, buckSize):
    f = open(fn, 'rU')
    reader = csv.reader(f, dialect='excel')
    
    matrix = []
    
    for row in reader:
        matrix.extend(row);
        
    f.close()
    
    buckCount = int(math.ceil(256.0/buckSize))
    histogram = [0 for i in range(0,buckCount)]
    
    for i in range(0,256):
        histogram[i/buckSize] += matrix.count(str(i))
    
    return histogram

i = 0
for e in histogram("Matrices of I1.csv", 200):
    i += 1
    print "bucket", i, " ", e