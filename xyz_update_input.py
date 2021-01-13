# note: Edited to update the dimension of box in X and Y every new MC cycle
# note: Last edited on 8/1/2020 17:55

import os

f1 = open('towhee_input').readlines()[31]
f21 = open('towhee_input').readlines()[35]
f22 = open('towhee_input').readlines()[36]
f23 = open('towhee_input').readlines()[37]
f3 = open('output_npt.gro').readlines()[-1]
f4 = open('field.top').readlines()[-1]
f99 = open('dummy_input', 'w')

first_part = open('towhee_input').readlines()[:31]
second_part = open('towhee_input').readlines()[32:35]
third_part = open('towhee_input').readlines()[38:]

# New number of water molecules from MD
sol_new = f4.split()[1]

# New coordinate of box XYZ from MD
xx_new 	= float(f3.split()[0])*10
yy_new  = float(f3.split()[1])*10
zz_new	= float(f3.split()[2])*10

# Box dimension that remain constant always (0.00)
yx_old = f21.split()[1]
zx_old = f21.split()[2]
xy_old = f22.split()[0]
zy_old = f22.split()[2]
xz_old = f23.split()[0]
yz_old = f23.split()[1]

# Number of GO remain constant (depends on layer of GO used)
old_GO = f1.split()[1]

for line in first_part:
 f99.write(line)

# Update new number of SOL in towhee_input
f99.write(str('%3s' % sol_new) + ('%2s\n' % old_GO))

for line in second_part:
 f99.write(line)

# Update new box dimension in towhee_input 
f99.write(str('%8.4f' % float(xx_new)) + str('%6.2f' % float(yx_old)) + str('%6.2f\n' % float(zx_old)))
f99.write(str('%4.2f' % float(xy_old)) + str('%8.4f' % float(yy_new)) + str('%6.2f\n' % float(zy_old)))
f99.write(str('%4.2f' % float(xz_old)) + str('%6.2f' % float(yz_old)) + str('%10.4f\n' % float(zz_new)))

for line in third_part:
 f99.write(line)

f99.close()


os.rename(r'dummy_input',r'towhee_input')  ### RENAME DUMMY TO ORIGINAL FILE NAME ###

print("      ")
print("******")
print("DONE!!")
print("******")
print("      ")

exit

