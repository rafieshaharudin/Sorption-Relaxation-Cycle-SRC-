#!/bin/bash --login

# SGE options start with a '#$'
#$ -S /bin/bash

# run in current working directory
#$ -cwd

# notify when end
#$ -m bea
#$ -M mohdrafiebin.shaharudin@postgrad.manchester.ac.uk

# load latest GROMACS module
module load apps/intel-18.0/towhee/8.2.0
module load apps/intel-17.0/gromacs/2018.4/double
module load apps/binapps/anaconda3/2019.07


#from md_0 to mc_1
## hold job till previous job end

##$ -hold_jid highRH_md0

cp ../md_20/output_minim.gro .
cp ../field.top .

ipython gro2coord_accurate.py
ipython xyz_update_input.py

# MC/MD coupling N cycle

# define simulation name
#$ -N SRC_highRH_cont


# make data_analysis file to transfer MC and MD output

mkdir data_analysis

for iteration in $(seq 3);

do 

#MC--

./towhee_execute > towhee_output

mkdir mc_"$iteration"

cp towhee_output data_analysis/T"$iteration".txt
mv towhee_output mc_"$iteration"
cp box* mc_"$iteration"

# python convert MC to MD

ipython pdb2gro.py
ipython update_top.py

#MD--

# set parallel environment and number of cores
#$ -pe smp.pe 24

# Inform software how many cores to use
export OMP_NUM_THREADS=$NSLOTS

# compile .tpr file equilibration
gmx_d grompp -p field.top -c input.gro -f nvt.mdp -o input_nvt.tpr

# equilibratrion simulation
gmx_d mdrun -s input_nvt.tpr -deffnm output_nvt

# compile .tpr file equilibration
gmx_d grompp -p field.top -c output_nvt.gro -f npt.mdp -o input_npt.tpr -maxwarn 1

# equilibratrion simulation
gmx_d mdrun -s input_npt.tpr -deffnm output_npt

# compile .tpr file for energy minimisation before GCMC
gmx_d grompp -p field.top -c output_npt.gro -f minim.mdp -o input_minim.tpr

# energy minimisation simulation
gmx_d mdrun -s input_minim.tpr -deffnm output_minim


mkdir md_"$iteration"

# python convert MD to MC

ipython gro2coord_accurate.py
ipython xyz_update_input.py

# run gmx energy to get box height in Z 

echo 16 0 | gmx_d energy -f output_npt.edr -o Z"$iteration"

mv *.xvg data_analysis

mv output_* *.tpr md_"$iteration"

# housekeeping
rm box* 

done


# End of jobscript
