# Aim : To convert .pdb file from MC to .gro file for MD

f1 = open('box_01_step_00000000010000.pdb').readlines()[:-2] ### SKIP 2 LINES AT THE END OF .pdb FILE ###
f2 = open('towhee_input').readlines()[35:38] ### READ BOX DIMENSION (NEED TO ENSURE CONSISTENCY IN towhee_input FILE) ###
f9 = open('input.gro', 'w')

########## CALCULATE NUMBER OF ATOMS IN THE BOX ############################

count = 0
for line in f1:
 count += 1

########## CREATE EMPTY ARRAYS OF DESIRED VALUES ##########################

P = []		# box dimension              from *towhee_final*
indx = []	# index of molecules         from *.pdb file*
atom = []	# name of atom               from *.pdb file*
resd = []	# name of residue (SOL/GRO)  from *.pdb file*
at_n = []	# atom sequence number       from *.pdb file*
x_pt = []	# x coordinate of each atoms from *.pdb file*
y_pt = []	# y coordinate of each atoms from *.pdb file*
z_pt = []	# z coordinate of each atoms from *.pdb file*
SOL  = []	# rearrange GRO top SOL bottom
############## WRITE TITLE AND NUMBER OF ATOMS ON .gro FILE ##################

f9.write('GRAPHENE OXIDE\n')
f9.write(str("%5d\n" % (count)))

############# READ DIMENSION OF BOX AND CONVERT UNIT TO nm ##################

for line in f2:
  c = line.split()
  P.append(c)
xbox = float(P[0][0])*0.1	# convert from A to nm
ybox = float(P[1][1])*0.1	# convert from A to nm
zbox = float(P[2][2])*0.1	# convert from A to nm

############ READ .pdb FILE AND STORE DESIRED VALUES #########################

for line in f1:
 if 'GRO' in line:
  SOL.append(line)

for line in f1:
 if 'SOL' in line:
  SOL.append(line)

for line in SOL:
 #split line into columns
 s=line.split()
 #store value in columns
 indx=(int(s[1]))
 atom=(str(s[2]))
 resd=(str(s[3]))
 at_n=(int(s[4]))
 x_pt=(float(s[5])*0.1)		# convert from A to nm
 y_pt=(float(s[6])*0.1)	 	# convert from A to nm
 z_pt=(float(s[7])*0.1) 	# convert from A to nm

############ WRITE DESIRED VALUES TO .gro FILE ################################

 f9.write(str("%5d" % (at_n)) + str("%3s" % (resd)) + str("%7s" % (atom)) + str("%5s" % (indx)) + str("%8.3f" % (x_pt)) + str("%8.3f" % (y_pt)) + str("%8.3f\n" % (z_pt)))

########### WRITE BOX DIMENSION AT THE BOTTOM OF .gro FILE ####################

f9.write(str("%10.5f" % (xbox)) + str("%10.5f" % (ybox)) + str("%10.5f\n" % (zbox)))

f9.close()

print("      ")
print("******")
print("DONE!!")
print("******")
print("      ")

exit
