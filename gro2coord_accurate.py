# Aim: To convert .gro file from Gromacs to towhee_coords file for Towhee software

f0 = open('output_npt.gro').readlines()[-1] ### READ BOX DIMENSION ###
f1 = open('output_npt.gro').readlines()[2:-1] ### READ X,Y,Z COORDINATES ###
f99 = open('towhee_coords', 'w')

### OPEN EMPTY ARRAYS OF DESIRED VALUES ###
lx = []	### X BOX DIMENSION ###
ly = []	### Y BOX DIMENSION ###
lz = []	### Z BOX DIMENSION ###
X = []	### X COORDINATE ###
Y = []	### Y COORDINTE ###
Z = []	### Z COORDINATE ###
AtmName = []
ResName = []
GRO = [] ### TEMPORARY GRO COORDINATE FOR CHANGE SEQUENCE ###
SOL = [] ### TEMPORARY SOL COORDINATE FOR CHANGE SEQUENCE ###

count = 0 ### OPEN VARIABLE TO COUNT NUMBER OF SOL ATOMS ###

### REARRANGE .gro FILE SOL MOLECULES TO MATCH TOWHEE FORMAT ###
for line in f1:
 if 'SOL' in line:	
  SOL.append(line)	### WRITE SOL ATOMS IN ARRAYS ###
 
for line in f1:
 if 'GRO' in line:
  SOL.append(line)	### WRITE GRO ATOMS IN ARRAYS ###

### READ BOX DIMENSION AND STORE TO ARRAYS ###
box = f0.split() 
lx = float(box[0])	### STORE X BOX DIMENSION ###
ly = float(box[1])	### STORE Y BOX DIMENSION ###
lz = float(box[2])	### STORE Z BOX DIMENSION ###
 
### READ COORDINATES OF ATOMS AND STORE TO ARRAYS ### 
## UPDATE: WILL DEFINITELY READ THE COORDINATES (XYZ) INSTEAD OF COORD(YZ) AND VEL(X)
##  DUE TO SPACING ISSUE IN .gro FILE WITH LOADS OF MOLECULES ##

for line in enumerate(SOL):
 resname = line[1][5:10]
 ResName.append(resname)
 atmname = line[1][10:15]
 AtmName.append(atmname) 
 x = float(line[1][20:28])
 if x > lx:             ### CHECK IF ATOMS OUTSIDE BOX ###
  x = x - lx            ### BRING ATOMS BACK INSIDE BOX ###
 elif x < 0:            ### CHECK IF ATOMS OUTSIDE BOX ###
  x = x + lx            ### BRING ATOMS BACK INSIDE BOX ###
 X.append(x)
 y = float(line[1][28:36])
 if y > ly:
  y = y - ly
 elif y < 0:
  y = y + ly
 Y.append(y)
 z = float(line[1][36:44])
 if z > lz:
  z = z - lz
 elif z < 0:
  z = z + lz
 Z.append(z)
 count += 2

Atom_N = list((range(1,count)))

### WRITE X,Y,Z COORDINATES OF EACH ATOM IN UNIT ANGSTROM IN towhee_coords ###
for i, j, k, l, m, n in zip(X, Y, Z, AtmName, Atom_N, ResName):
 f99.write(str("%21.16f" % (i*10)) + str("%21.16f" % (j*10)) + str("%21.16f" % (k*10))+ str("%8s" % (l)) + str("%6s" % (m)) + str("%6s\n" % (n)))

f99.close()

print("      ")
print("******")
print("DONE!!")
print("******")
print("      ")

exit
