### SCRIPT TO UPDATE field.top FILE AFTER EACH ADSORPTION SIMULATION ###

import os ### USE OS MODULE TO RENAME DUMMY FILE AT THE END OF SCRIPT ###

f3=open('field.top').readlines()
f4=open('input.gro').readlines() 
f99=open('dummy.top','w')

count = 0 ### OPEN COUNT ###

P=[] ### CREATE EMPTY ARRAYS TO STORE NEW NUMBER OF 'SOL' MOLECULES ###

for line in f4:      ### CALCULATE 'SOL' ATOMS ###
 if 'SOL' in line:
  count += 1

SOL = int(count/3)  ### CONVERT 'SOL' ATOMS TO MOLECULES ###

for line in f3:
 if 'SOL' in line:
  c=line.split()
  P.append(c)
  P[0][1]=int(SOL)  ### UPDATE NEW 'SOL' MOLECULES NUMBER ###

last_line = f3[-1]  ### DEFINE LAST LINE OF ORIGINAL TOPOLOGY FILE ###

### WRITE UPDATED 'SOL' MOLECULES OF TOP FILE IN A DUMMY FILE ###
for line in f3:
 if line == last_line:
  f99.write(str("%3s" % (P[0][0])) + str("%6d\n" % (P[0][1])))
 else:
  f99.write(line)

f99.close()

os.rename(r'dummy.top',r'field.top')  ### RENAME DUMMY TO ORIGINAL TOP FILE NAME ###

print("      ")
print("******")
print("DONE!!")
print("******")
print("      ")

exit
