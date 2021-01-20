# Aim : To plot the evolution of number of water molecules adsorbed and box height in Z from SRCs

set title 'Number of water molecules adsorbed'
set ylabel 'N'
set xlabel 'Number of MC steps'
set key bottom right
plot 'SRC_MC' u 1:4 w lp lw 2.0 lc 'black' title 'N water adsorbed'

pause -1 'ENTER TO PLOT MD'

set title 'Z box evolution'
set ylabel 'Box height (nm)'
set xlabel 'Time (ps)'
set key bottom right
plot 'SRC_MD' w lp lw 2.0 lc 'black' title 'Z box'

pause -1 'ENTER TO EXIT'
