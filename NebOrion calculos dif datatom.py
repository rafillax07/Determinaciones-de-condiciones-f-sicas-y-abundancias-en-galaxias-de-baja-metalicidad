# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:23:19 2023

@author: LENOVOPC
"""

import pyneb as pn
import numpy as np


DataFileDict = {
'O2': {'atom': 'o_ii_atom_FFT04.dat', 'coll': 'o_ii_coll_Kal09.dat'},
'O3': {'atom': 'o_iii_atom_FFT04-SZ00.dat', 'coll': 'o_iii_coll_SSB14.dat'},
'Ne3': {'atom': 'ne_iii_atom_GMZ97.dat', 'coll': 'ne_iii_coll_McLB00.dat'},
'N2': {'atom': 'n_ii_atom_FFT04.dat', 'coll': 'n_ii_coll_T11.dat'},  
'S2': {'atom': 's_ii_atom_FFTI06.dat', 'coll': 's_ii_coll_TZ10.dat'},
'S3': {'atom': 's_iii_atom_FFTI06.dat', 'coll': 's_iii_coll_GRHK14.dat'},  
'Ar3':{'atom': 'ar_iii_atom_MB09.dat', 'coll': 'ar_iii_coll_MB09.dat'}, 
'Ar4':{'atom': 'ar_iv_atom_MZ82.dat', 'coll': 'ar_iv_coll_RB97.dat'},
'Cl3':{'atom': 'cl_iii_atom_Fal99.dat', 'coll': 'cl_iii_coll_BZ89.dat'},

'Fe3':{'atom': 'fe_iii_atom_Q96_J00.dat', 'coll': 'fe_iii_coll_Z96.dat'},
#'Fe3':{'atom': 'fe_iii_atom_Q96_J00.dat', 'coll': 'fe_iii_coll_BB14_144.dat'},
#'Fe3':{'atom': 'fe_iii_atom_Q96_J00.dat', 'coll': 'fe_iii_coll_BBQ10_34.dat'},
#'Fe3':{'atom': 'fe_iii_atom_BB14_144.dat', 'coll': 'fe_iii_coll_Z96.dat'},
#'Fe3':{'atom': 'fe_iii_atom_BB14_144.dat', 'coll': 'fe_iii_coll_BB14_144.dat'},
#'Fe3':{'atom': 'fe_iii_atom_BB14_144.dat', 'coll': 'fe_iii_coll_BBQ10_34.dat'},
#'Fe3':{'atom': 'fe_iii_atom_BBQ10.dat', 'coll': 'fe_iii_coll_Z96.dat'},
#'Fe3':{'atom': 'fe_iii_atom_BBQ10.dat', 'coll': 'fe_iii_coll_BB14_144.dat'},
#'Fe3':{'atom': 'fe_iii_atom_BBQ10.dat', 'coll': 'fe_iii_coll_BBQ10_34.dat'},
#'Fe3':{'atom': 'fe_iii_atom_DH09_34.dat', 'coll': 'fe_iii_coll_Z96.dat'},
#'Fe3':{'atom': 'fe_iii_atom_DH09_34.dat', 'coll': 'fe_iii_coll_BB14_144.dat'},
#'Fe3':{'atom': 'fe_iii_atom_DH09_34.dat', 'coll': 'fe_iii_coll_BBQ10_34.dat'},
#'Fe3':{'atom': 'fe_iii_atom_NP96.dat', 'coll': 'fe_iii_coll_Z96.dat'},
#'Fe3':{'atom': 'fe_iii_atom_NP96.dat', 'coll': 'fe_iii_coll_BB14_144.dat'},
#'Fe3':{'atom': 'fe_iii_atom_NP96.dat', 'coll': 'fe_iii_coll_BBQ10_34.dat'},
}

pn.atomicData.setDataFileDict(DataFileDict)

O3 = pn.Atom('O',3)
N2 = pn.Atom('N',2)
O2 = pn.Atom('O',2)
S2 = pn.Atom('S',2)
Cl3 = pn.Atom('Cl',3)
Ar4 = pn.Atom('Ar',4)
S3 = pn.Atom('S',3)
Ar3 = pn.Atom('Ar',3)
Fe3 = pn.Atom('Fe',3,NLevels=34)

#Para Nebulosa Orion
# i3323feiii =  0.069
i3726 = 55.776
i3729 = 26.898
i3868 =  22.870
i3967 = 6.849
i4009feiii = 0.022
i4026 =  2.181
i4131feiii = 0.016
i4363 = 1.301
i4388 =  0.542
i4471 = 4.523
#i4607feiii = 0
i4659feiii = 0.549
i4668feiii = 0.031
i4701feiii = 0.172
i4711 = 0.100
i4734feiii = 0.069
i4740 =  0.121
i4755feiii = 0.103
i4770feiii = 0.061
i4778feiii = 0.033
i4881feiii = 0.254
i4922 = 1.222
i4925feiii = 0.049
i4931feiii = 0.021
i4959 = 128.202
i4986feiii = 0.012
i4987feiii = 0.046
i5007 = 383.804
i5011feiii = 0.067
i5085feiii = 0.011
i5270feiii = 0.274
i5412feiii = 0.026
i5518 =  0.383
i5538 = 0.590
i5755 = 0.680
i5876 = 14.418 
i6312 = 1.853
i6548 = 12.201
i6584 =  37.769
i6678 =  3.848
i6716 = 1.938
i6731 = 3.518
i7135 = 16.197 
i7320 = 5.432
i7330 = 4.154

den = 100

#Temperatura
temO3 = O3.getTemDen(i4363/(i5007), den=den, to_eval = 'L(4363)/L(5007)')
temO2 = 0.7*temO3 + 3000.0   
temN2 = N2.getTemDen(i5755/(i6548+i6584), den=den, to_eval = 'L(5755)/(L(6548)+L(6584))')

print(temO3)
print(temO2)
print(temN2)

#Densidades Nebulosa Orion
ne_s2 = S2.getTemDen(i6716/i6731, tem=temN2, to_eval = 'L(6716)/L(6731)')
ne_o2 = O2.getTemDen(i3726/i3729, tem=temN2, to_eval = 'L(3726)/L(3729)')
ne_cl3 = Cl3.getTemDen(i5518/i5538, tem=temN2, to_eval = 'L(5518)/L(5538)')
ne_ar4 = Ar4.getTemDen(i4711/i4740, tem=temO3, to_eval = 'L(4711)/L(4740)')

ane = np.array([ne_s2, ne_o2, ne_cl3, ne_ar4])
lne = np.log10(ane)
mne = np.nanmean(lne)
den = 10**mne

print(ne_o2)
print(ne_s2)
print(ne_cl3)
print(ne_ar4)
print(den)

#Abundancias O, O+, O++, O total
abO2 = O2.getIonAbundance(int_ratio=(i3726+i3729), tem=temN2, den=den, to_eval='L(3726)+L(3729)')
labO2 = 12.0 + np.log10(abO2)
abO2b = O2.getIonAbundance(int_ratio=(i7320+i7330), tem=temN2, den=den, to_eval='L(7319)+L(7320)+L(7330)+L(7331)')
labO2b = 12.0 + np.log10(abO2b)
abO3 = O3.getIonAbundance(int_ratio=(i5007), tem=temO3, den=den, to_eval='L(5007)')
labO3 = 12.0 + np.log10(abO3)
abO3b = O3.getIonAbundance(int_ratio=(i4363), tem=temO3, den=den, to_eval='L(4363)')
labO3b = 12.0 + np.log10(abO3b)
abO = abO2 + abO3
labO = 12.0 + np.log10(abO)

#print(labO2)
#print(labO2b)
#print(labO3)
#print(labO3b)
#print(labO)

# Abundancias Fe++/H+, Fe/H y Fe/O con densidad media

# abFe3i3323feiii = Fe3.getIonAbundance((i3323feiii), tem=temN2, den=den, to_eval='L(3323)')											
# labFe3i3323feiii = 12.0 + np.log10(abFe3i3323feiii)

abFe3i4009feiii = Fe3.getIonAbundance((i4009feiii), tem=temN2, den=den, to_eval='L(4009)')											
labFe3i4009feiii = 12.0 + np.log10(abFe3i4009feiii)

abFe3i4131feiii = Fe3.getIonAbundance((i4131feiii), tem=temN2, den=den, to_eval='L(4131)')											
labFe3i4131feiii = 12.0 + np.log10(abFe3i4131feiii)

# abFe3i4607feiii = Fe3.getIonAbundance((i4607feiii), tem=temN2, den=den, to_eval='L(4607)')											
# labFe3i4607feiii = 12.0 + np.log10(abFe3i4607feiii)

abFe3i4659feiii = Fe3.getIonAbundance((i4659feiii), tem=temN2, den=den, to_eval='L(4659)')											
labFe3i4659feiii = 12.0 + np.log10(abFe3i4659feiii)

abFe3i4668feiii = Fe3.getIonAbundance((i4668feiii), tem=temN2, den=den, to_eval='L(4668)')											
labFe3i4668feiii = 12.0 + np.log10(abFe3i4668feiii)

abFe3i4701feiii = Fe3.getIonAbundance((i4701feiii), tem=temN2, den=den, to_eval='L(4701)')											
labFe3i4701feiii = 12.0 + np.log10(abFe3i4701feiii)

abFe3i4734feiii = Fe3.getIonAbundance((i4734feiii), tem=temN2, den=den, to_eval='L(4734)')											
labFe3i4734feiii = 12.0 + np.log10(abFe3i4734feiii)

abFe3i4755feiii = Fe3.getIonAbundance((i4755feiii), tem=temN2, den=den, to_eval='L(4755)')											
labFe3i4755feiii = 12.0 + np.log10(abFe3i4755feiii)

abFe3i4770feiii = Fe3.getIonAbundance((i4770feiii), tem=temN2, den=den, to_eval='L(4770)')											
labFe3i4770feiii = 12.0 + np.log10(abFe3i4770feiii)

abFe3i4778feiii = Fe3.getIonAbundance((i4778feiii), tem=temN2, den=den, to_eval='L(4778)')											
labFe3i4778feiii = 12.0 + np.log10(abFe3i4778feiii)

abFe3i4881feiii = Fe3.getIonAbundance((i4881feiii), tem=temN2, den=den, to_eval='L(4881)')											
labFe3i4881feiii = 12.0 + np.log10(abFe3i4881feiii)

abFe3i4925feiii = Fe3.getIonAbundance((i4925feiii), tem=temN2, den=den, to_eval='L(4925)')											
labFe3i4925feiii = 12.0 + np.log10(abFe3i4925feiii)

abFe3i4931feiii = Fe3.getIonAbundance((i4931feiii), tem=temN2, den=den, to_eval='L(4931)')											
labFe3i4931feiii = 12.0 + np.log10(abFe3i4931feiii)

abFe3i4986feiii = Fe3.getIonAbundance((i4986feiii), tem=temN2, den=den, to_eval='L(4986)')											
labFe3i4986feiii = 12.0 + np.log10(abFe3i4986feiii)

abFe3i4987feiii = Fe3.getIonAbundance((i4987feiii), tem=temN2, den=den, to_eval='L(4987)')											
labFe3i4987feiii = 12.0 + np.log10(abFe3i4987feiii)

abFe3i5011feiii = Fe3.getIonAbundance((i5011feiii), tem=temN2, den=den, to_eval='L(5011)')											
labFe3i5011feiii = 12.0 + np.log10(abFe3i5011feiii)

abFe3i5085feiii = Fe3.getIonAbundance((i5085feiii), tem=temN2, den=den, to_eval='L(5085)')											
labFe3i5085feiii = 12.0 + np.log10(abFe3i5085feiii)

abFe3i5270feiii = Fe3.getIonAbundance((i5270feiii), tem=temN2, den=den, to_eval='L(5270)')											
labFe3i5270feiii = 12.0 + np.log10(abFe3i5270feiii)

abFe3i5412feiii = Fe3.getIonAbundance((i5412feiii), tem=temN2, den=den, to_eval='L(5412)')											
labFe3i5412feiii = 12.0 + np.log10(abFe3i5412feiii)

#abFeOb = (abFe3/abO2)*((abO2/abO3)**0.08)*0.9
#abFeOc = (abFe3/abO2)*((abO2/abO3)**0.58)*1.1
#labFeOb = np.log10(abFeOb)
#labFeOc = np.log10(abFeOc)

#print(labFe3i3323feiii)
print(labFe3i4009feiii)
print(labFe3i4131feiii)
#print(labFe3i4607feiii)
print(labFe3i4659feiii)
print(labFe3i4668feiii)
print(labFe3i4701feiii)
print(labFe3i4734feiii)
print(labFe3i4755feiii)
print(labFe3i4770feiii)
print(labFe3i4778feiii)
print(labFe3i4881feiii)
print(labFe3i4925feiii)
print(labFe3i4931feiii)
print(labFe3i4986feiii)
print(labFe3i4987feiii)
print(labFe3i5011feiii)
print(labFe3i5085feiii)
print(labFe3i5270feiii)
print(labFe3i5412feiii)
#print(labFeOb)
#print(labFeOc)

a=(1111111111111)

print(a)

# Abundancias Fe++/H+, Fe/H y Fe/O con densidad Cl3

# abFe3i3323feiiid1 = Fe3.getIonAbundance((i3323feiii), tem=temN2, den=ne_cl3, to_eval='L(3323)')											
# labFe3i3323feiiid1 = 12.0 + np.log10(abFe3i3323feiiid1)

abFe3i4009feiiid1 = Fe3.getIonAbundance((i4009feiii), tem=temN2, den=ne_cl3, to_eval='L(4009)')											
labFe3i4009feiiid1 = 12.0 + np.log10(abFe3i4009feiiid1)

abFe3i4131feiiid1 = Fe3.getIonAbundance((i4131feiii), tem=temN2, den=ne_cl3, to_eval='L(4131)')											
labFe3i4131feiiid1 = 12.0 + np.log10(abFe3i4131feiiid1)

# abFe3i4607feiiid1 = Fe3.getIonAbundance((i4607feiii), tem=temN2, den=ne_cl3, to_eval='L(4607)')											
# labFe3i4607feiiid1 = 12.0 + np.log10(abFe3i4607feiiid1)

abFe3i4659feiiid1 = Fe3.getIonAbundance((i4659feiii), tem=temN2, den=ne_cl3, to_eval='L(4659)')											
labFe3i4659feiiid1 = 12.0 + np.log10(abFe3i4659feiiid1)

abFe3i4668feiiid1 = Fe3.getIonAbundance((i4668feiii), tem=temN2, den=ne_cl3, to_eval='L(4668)')											
labFe3i4668feiiid1 = 12.0 + np.log10(abFe3i4668feiiid1)

abFe3i4701feiiid1 = Fe3.getIonAbundance((i4701feiii), tem=temN2, den=ne_cl3, to_eval='L(4701)')											
labFe3i4701feiiid1 = 12.0 + np.log10(abFe3i4701feiiid1)

abFe3i4734feiiid1 = Fe3.getIonAbundance((i4734feiii), tem=temN2, den=ne_cl3, to_eval='L(4734)')											
labFe3i4734feiiid1 = 12.0 + np.log10(abFe3i4734feiiid1)

abFe3i4755feiiid1 = Fe3.getIonAbundance((i4755feiii), tem=temN2, den=ne_cl3, to_eval='L(4755)')											
labFe3i4755feiiid1 = 12.0 + np.log10(abFe3i4755feiiid1)

abFe3i4770feiiid1 = Fe3.getIonAbundance((i4770feiii), tem=temN2, den=ne_cl3, to_eval='L(4770)')											
labFe3i4770feiiid1 = 12.0 + np.log10(abFe3i4770feiiid1)

abFe3i4778feiiid1 = Fe3.getIonAbundance((i4778feiii), tem=temN2, den=ne_cl3, to_eval='L(4778)')											
labFe3i4778feiiid1 = 12.0 + np.log10(abFe3i4778feiiid1)

abFe3i4881feiiid1 = Fe3.getIonAbundance((i4881feiii), tem=temN2, den=ne_cl3, to_eval='L(4881)')											
labFe3i4881feiiid1 = 12.0 + np.log10(abFe3i4881feiiid1)

abFe3i4925feiiid1 = Fe3.getIonAbundance((i4925feiii), tem=temN2, den=ne_cl3, to_eval='L(4925)')											
labFe3i4925feiiid1 = 12.0 + np.log10(abFe3i4925feiiid1)

abFe3i4931feiiid1 = Fe3.getIonAbundance((i4931feiii), tem=temN2, den=ne_cl3, to_eval='L(4931)')											
labFe3i4931feiiid1 = 12.0 + np.log10(abFe3i4931feiiid1)

abFe3i4986feiiid1 = Fe3.getIonAbundance((i4986feiii), tem=temN2, den=ne_cl3, to_eval='L(4986)')											
labFe3i4986feiiid1 = 12.0 + np.log10(abFe3i4986feiiid1)

abFe3i4987feiiid1 = Fe3.getIonAbundance((i4987feiii), tem=temN2, den=ne_cl3, to_eval='L(4987)')											
labFe3i4987feiiid1 = 12.0 + np.log10(abFe3i4987feiiid1)

abFe3i5011feiiid1 = Fe3.getIonAbundance((i5011feiii), tem=temN2, den=ne_cl3, to_eval='L(5011)')											
labFe3i5011feiiid1 = 12.0 + np.log10(abFe3i5011feiiid1)

abFe3i5085feiiid1 = Fe3.getIonAbundance((i5085feiii), tem=temN2, den=ne_cl3, to_eval='L(5085)')											
labFe3i5085feiiid1 = 12.0 + np.log10(abFe3i5085feiiid1)

abFe3i5270feiiid1 = Fe3.getIonAbundance((i5270feiii), tem=temN2, den=ne_cl3, to_eval='L(5270)')											
labFe3i5270feiiid1 = 12.0 + np.log10(abFe3i5270feiiid1)

abFe3i5412feiiid1 = Fe3.getIonAbundance((i5412feiii), tem=temN2, den=ne_cl3, to_eval='L(5412)')											
labFe3i5412feiiid1 = 12.0 + np.log10(abFe3i5412feiiid1)

#print(labFe3i3323feiiid1)
print(labFe3i4009feiiid1)
print(labFe3i4131feiiid1)
#print(labFe3i4607feiiid1)
print(labFe3i4659feiiid1)
print(labFe3i4668feiiid1)
print(labFe3i4701feiiid1)
print(labFe3i4734feiiid1)
print(labFe3i4755feiiid1)
print(labFe3i4770feiiid1)
print(labFe3i4778feiiid1)
print(labFe3i4881feiiid1)
print(labFe3i4925feiiid1)
print(labFe3i4931feiiid1)
print(labFe3i4986feiiid1)
print(labFe3i4987feiiid1)
print(labFe3i5011feiiid1)
print(labFe3i5085feiiid1)
print(labFe3i5270feiiid1)
print(labFe3i5412feiiid1)

print(a)

#Abundancias Fe++/H+, Fe/H y Fe/O con densidad Ar4

# abFe3i3323feiiid2 = Fe3.getIonAbundance((i3323feiii), tem=temN2, den=ne_ar4, to_eval='L(3323)')											
# labFe3i3323feiiid2 = 12.0 + np.log10(abFe3i3323feiiid2)

abFe3i4009feiiid2 = Fe3.getIonAbundance((i4009feiii), tem=temN2, den=ne_ar4, to_eval='L(4009)')											
labFe3i4009feiiid2 = 12.0 + np.log10(abFe3i4009feiiid2)

abFe3i4131feiiid2 = Fe3.getIonAbundance((i4131feiii), tem=temN2, den=ne_ar4, to_eval='L(4131)')											
labFe3i4131feiiid2 = 12.0 + np.log10(abFe3i4131feiiid2)

# abFe3i4607feiiid2 = Fe3.getIonAbundance((i4607feiii), tem=temN2, den=ne_ar4, to_eval='L(4607)')											
# labFe3i4607feiiid2 = 12.0 + np.log10(abFe3i4607feiiid2)

abFe3i4659feiiid2 = Fe3.getIonAbundance((i4659feiii), tem=temN2, den=ne_ar4, to_eval='L(4659)')											
labFe3i4659feiiid2 = 12.0 + np.log10(abFe3i4659feiiid2)

abFe3i4668feiiid2 = Fe3.getIonAbundance((i4668feiii), tem=temN2, den=ne_ar4, to_eval='L(4668)')											
labFe3i4668feiiid2 = 12.0 + np.log10(abFe3i4668feiiid2)

abFe3i4701feiiid2 = Fe3.getIonAbundance((i4701feiii), tem=temN2, den=ne_ar4, to_eval='L(4701)')											
labFe3i4701feiiid2 = 12.0 + np.log10(abFe3i4701feiiid2)

abFe3i4734feiiid2 = Fe3.getIonAbundance((i4734feiii), tem=temN2, den=ne_ar4, to_eval='L(4734)')											
labFe3i4734feiiid2 = 12.0 + np.log10(abFe3i4734feiiid2)

abFe3i4755feiiid2 = Fe3.getIonAbundance((i4755feiii), tem=temN2, den=ne_ar4, to_eval='L(4755)')											
labFe3i4755feiiid2 = 12.0 + np.log10(abFe3i4755feiiid2)

abFe3i4770feiiid2 = Fe3.getIonAbundance((i4770feiii), tem=temN2, den=ne_ar4, to_eval='L(4770)')											
labFe3i4770feiiid2 = 12.0 + np.log10(abFe3i4770feiiid2)

abFe3i4778feiiid2 = Fe3.getIonAbundance((i4778feiii), tem=temN2, den=ne_ar4, to_eval='L(4778)')											
labFe3i4778feiiid2 = 12.0 + np.log10(abFe3i4778feiiid2)

abFe3i4881feiiid2 = Fe3.getIonAbundance((i4881feiii), tem=temN2, den=ne_ar4, to_eval='L(4881)')											
labFe3i4881feiiid2 = 12.0 + np.log10(abFe3i4881feiiid2)

abFe3i4925feiiid2 = Fe3.getIonAbundance((i4925feiii), tem=temN2, den=ne_ar4, to_eval='L(4925)')											
labFe3i4925feiiid2 = 12.0 + np.log10(abFe3i4925feiiid2)

abFe3i4931feiiid2 = Fe3.getIonAbundance((i4931feiii), tem=temN2, den=ne_ar4, to_eval='L(4931)')											
labFe3i4931feiiid2 = 12.0 + np.log10(abFe3i4931feiiid2)

abFe3i4986feiiid2 = Fe3.getIonAbundance((i4986feiii), tem=temN2, den=ne_ar4, to_eval='L(4986)')											
labFe3i4986feiiid2 = 12.0 + np.log10(abFe3i4986feiiid2)

abFe3i4987feiiid2 = Fe3.getIonAbundance((i4987feiii), tem=temN2, den=ne_ar4, to_eval='L(4987)')											
labFe3i4987feiiid2 = 12.0 + np.log10(abFe3i4987feiiid2)

abFe3i5011feiiid2 = Fe3.getIonAbundance((i5011feiii), tem=temN2, den=ne_ar4, to_eval='L(5011)')											
labFe3i5011feiiid2 = 12.0 + np.log10(abFe3i5011feiiid2)

abFe3i5085feiiid2 = Fe3.getIonAbundance((i5085feiii), tem=temN2, den=ne_ar4, to_eval='L(5085)')											
labFe3i5085feiiid2 = 12.0 + np.log10(abFe3i5085feiiid2)

abFe3i5270feiiid2 = Fe3.getIonAbundance((i5270feiii), tem=temN2, den=ne_ar4, to_eval='L(5270)')											
labFe3i5270feiiid2 = 12.0 + np.log10(abFe3i5270feiiid2)

abFe3i5412feiiid2 = Fe3.getIonAbundance((i5412feiii), tem=temN2, den=ne_ar4, to_eval='L(5412)')											
labFe3i5412feiiid2 = 12.0 + np.log10(abFe3i5412feiiid2)

#print(labFe3i3323feiiid2)
print(labFe3i4009feiiid2)
print(labFe3i4131feiiid2)
#print(labFe3i4607feiiid2)
print(labFe3i4659feiiid2)
print(labFe3i4668feiiid2)
print(labFe3i4701feiiid2)
print(labFe3i4734feiiid2)
print(labFe3i4755feiiid2)
print(labFe3i4770feiiid2)
print(labFe3i4778feiiid2)
print(labFe3i4881feiiid2)
print(labFe3i4925feiiid2)
print(labFe3i4931feiiid2)
print(labFe3i4986feiiid2)
print(labFe3i4987feiiid2)
print(labFe3i5011feiiid2)
print(labFe3i5085feiiid2)
print(labFe3i5270feiiid2)
print(labFe3i5412feiiid2)

print(a)

# Abundancias Fe++/H+, Fe/H y Fe/O con densidad O2

# abFe3i3323feiiid3 = Fe3.getIonAbundance((i3323feiii), tem=temN2, den=ne_o2, to_eval='L(3323)')											
# labFe3i3323feiiid3 = 12.0 + np.log10(abFe3i3323feiiid3)

abFe3i4009feiiid3 = Fe3.getIonAbundance((i4009feiii), tem=temN2, den=ne_o2, to_eval='L(4009)')											
labFe3i4009feiiid3 = 12.0 + np.log10(abFe3i4009feiiid3)

abFe3i4131feiiid3 = Fe3.getIonAbundance((i4131feiii), tem=temN2, den=ne_o2, to_eval='L(4131)')											
labFe3i4131feiiid3 = 12.0 + np.log10(abFe3i4131feiiid3)

# abFe3i4607feiiid3 = Fe3.getIonAbundance((i4607feiii), tem=temN2, den=ne_o2, to_eval='L(4607)')											
# labFe3i4607feiiid3 = 12.0 + np.log10(abFe3i4607feiiid3)

abFe3i4659feiiid3 = Fe3.getIonAbundance((i4659feiii), tem=temN2, den=ne_o2, to_eval='L(4659)')											
labFe3i4659feiiid3 = 12.0 + np.log10(abFe3i4659feiiid3)

abFe3i4668feiiid3 = Fe3.getIonAbundance((i4668feiii), tem=temN2, den=ne_o2, to_eval='L(4668)')											
labFe3i4668feiiid3 = 12.0 + np.log10(abFe3i4668feiiid3)

abFe3i4701feiiid3 = Fe3.getIonAbundance((i4701feiii), tem=temN2, den=ne_o2, to_eval='L(4701)')											
labFe3i4701feiiid3 = 12.0 + np.log10(abFe3i4701feiiid3)

abFe3i4734feiiid3 = Fe3.getIonAbundance((i4734feiii), tem=temN2, den=ne_o2, to_eval='L(4734)')											
labFe3i4734feiiid3 = 12.0 + np.log10(abFe3i4734feiiid3)

abFe3i4755feiiid3 = Fe3.getIonAbundance((i4755feiii), tem=temN2, den=ne_o2, to_eval='L(4755)')											
labFe3i4755feiiid3 = 12.0 + np.log10(abFe3i4755feiiid3)

abFe3i4770feiiid3 = Fe3.getIonAbundance((i4770feiii), tem=temN2, den=ne_o2, to_eval='L(4770)')											
labFe3i4770feiiid3 = 12.0 + np.log10(abFe3i4770feiiid3)

abFe3i4778feiiid3 = Fe3.getIonAbundance((i4778feiii), tem=temN2, den=ne_o2, to_eval='L(4778)')											
labFe3i4778feiiid3 = 12.0 + np.log10(abFe3i4778feiiid3)

abFe3i4881feiiid3 = Fe3.getIonAbundance((i4881feiii), tem=temN2, den=ne_o2, to_eval='L(4881)')											
labFe3i4881feiiid3 = 12.0 + np.log10(abFe3i4881feiiid3)

abFe3i4925feiiid3 = Fe3.getIonAbundance((i4925feiii), tem=temN2, den=ne_o2, to_eval='L(4925)')											
labFe3i4925feiiid3 = 12.0 + np.log10(abFe3i4925feiiid3)

abFe3i4931feiiid3 = Fe3.getIonAbundance((i4931feiii), tem=temN2, den=ne_o2, to_eval='L(4931)')											
labFe3i4931feiiid3 = 12.0 + np.log10(abFe3i4931feiiid3)

abFe3i4986feiiid3 = Fe3.getIonAbundance((i4986feiii), tem=temN2, den=ne_o2, to_eval='L(4986)')											
labFe3i4986feiiid3 = 12.0 + np.log10(abFe3i4986feiiid3)

abFe3i4987feiiid3 = Fe3.getIonAbundance((i4987feiii), tem=temN2, den=ne_o2, to_eval='L(4987)')											
labFe3i4987feiiid3 = 12.0 + np.log10(abFe3i4987feiiid3)

abFe3i5011feiiid3 = Fe3.getIonAbundance((i5011feiii), tem=temN2, den=ne_o2, to_eval='L(5011)')											
labFe3i5011feiiid3 = 12.0 + np.log10(abFe3i5011feiiid3)

abFe3i5085feiiid3 = Fe3.getIonAbundance((i5085feiii), tem=temN2, den=ne_o2, to_eval='L(5085)')											
labFe3i5085feiiid3 = 12.0 + np.log10(abFe3i5085feiiid3)

abFe3i5270feiiid3 = Fe3.getIonAbundance((i5270feiii), tem=temN2, den=ne_o2, to_eval='L(5270)')											
labFe3i5270feiiid3 = 12.0 + np.log10(abFe3i5270feiiid3)

abFe3i5412feiiid3 = Fe3.getIonAbundance((i5412feiii), tem=temN2, den=ne_o2, to_eval='L(5412)')											
labFe3i5412feiiid3 = 12.0 + np.log10(abFe3i5412feiiid3)

#print(labFe3i3323feiiid3)
print(labFe3i4009feiiid3)
print(labFe3i4131feiiid3)
#print(labFe3i4607feiiid3)
print(labFe3i4659feiiid3)
print(labFe3i4668feiiid3)
print(labFe3i4701feiiid3)
print(labFe3i4734feiiid3)
print(labFe3i4755feiiid3)
print(labFe3i4770feiiid3)
print(labFe3i4778feiiid3)
print(labFe3i4881feiiid3)
print(labFe3i4925feiiid3)
print(labFe3i4931feiiid3)
print(labFe3i4986feiiid3)
print(labFe3i4987feiiid3)
print(labFe3i5011feiiid3)
print(labFe3i5085feiiid3)
print(labFe3i5270feiiid3)
print(labFe3i5412feiiid3)

print(a)

# Abundancias Fe++/H+, Fe/H y Fe/O con densidad s2

# abFe3i3323feiiid4 = Fe3.getIonAbundance((i3323feiii), tem=temN2, den=ne_s2, to_eval='L(3323)')											
# labFe3i3323feiiid4 = 12.0 + np.log10(abFe3i3323feiiid4)

abFe3i4009feiiid4 = Fe3.getIonAbundance((i4009feiii), tem=temN2, den=ne_s2, to_eval='L(4009)')											
labFe3i4009feiiid4 = 12.0 + np.log10(abFe3i4009feiiid4)

abFe3i4131feiiid4 = Fe3.getIonAbundance((i4131feiii), tem=temN2, den=ne_s2, to_eval='L(4131)')											
labFe3i4131feiiid4 = 12.0 + np.log10(abFe3i4131feiiid4)

# abFe3i4607feiiid4 = Fe3.getIonAbundance((i4607feiii), tem=temN2, den=ne_s2, to_eval='L(4607)')											
# labFe3i4607feiiid4 = 12.0 + np.log10(abFe3i4607feiiid4)

abFe3i4659feiiid4 = Fe3.getIonAbundance((i4659feiii), tem=temN2, den=ne_s2, to_eval='L(4659)')											
labFe3i4659feiiid4 = 12.0 + np.log10(abFe3i4659feiiid4)

abFe3i4668feiiid4 = Fe3.getIonAbundance((i4668feiii), tem=temN2, den=ne_s2, to_eval='L(4668)')											
labFe3i4668feiiid4 = 12.0 + np.log10(abFe3i4668feiiid4)

abFe3i4701feiiid4 = Fe3.getIonAbundance((i4701feiii), tem=temN2, den=ne_s2, to_eval='L(4701)')											
labFe3i4701feiiid4 = 12.0 + np.log10(abFe3i4701feiiid4)

abFe3i4734feiiid4 = Fe3.getIonAbundance((i4734feiii), tem=temN2, den=ne_s2, to_eval='L(4734)')											
labFe3i4734feiiid4 = 12.0 + np.log10(abFe3i4734feiiid4)

abFe3i4755feiiid4 = Fe3.getIonAbundance((i4755feiii), tem=temN2, den=ne_s2, to_eval='L(4755)')											
labFe3i4755feiiid4 = 12.0 + np.log10(abFe3i4755feiiid4)

abFe3i4770feiiid4 = Fe3.getIonAbundance((i4770feiii), tem=temN2, den=ne_s2, to_eval='L(4770)')											
labFe3i4770feiiid4 = 12.0 + np.log10(abFe3i4770feiiid4)

abFe3i4778feiiid4 = Fe3.getIonAbundance((i4778feiii), tem=temN2, den=ne_s2, to_eval='L(4778)')											
labFe3i4778feiiid4 = 12.0 + np.log10(abFe3i4778feiiid4)

abFe3i4881feiiid4 = Fe3.getIonAbundance((i4881feiii), tem=temN2, den=ne_s2, to_eval='L(4881)')											
labFe3i4881feiiid4 = 12.0 + np.log10(abFe3i4881feiiid4)

abFe3i4925feiiid4 = Fe3.getIonAbundance((i4925feiii), tem=temN2, den=ne_s2, to_eval='L(4925)')											
labFe3i4925feiiid4 = 12.0 + np.log10(abFe3i4925feiiid4)

abFe3i4931feiiid4 = Fe3.getIonAbundance((i4931feiii), tem=temN2, den=ne_s2, to_eval='L(4931)')											
labFe3i4931feiiid4 = 12.0 + np.log10(abFe3i4931feiiid4)

abFe3i4986feiiid4 = Fe3.getIonAbundance((i4986feiii), tem=temN2, den=ne_s2, to_eval='L(4986)')											
labFe3i4986feiiid4 = 12.0 + np.log10(abFe3i4986feiiid4)

abFe3i4987feiiid4 = Fe3.getIonAbundance((i4987feiii), tem=temN2, den=ne_s2, to_eval='L(4987)')											
labFe3i4987feiiid4 = 12.0 + np.log10(abFe3i4987feiiid4)

abFe3i5011feiiid4 = Fe3.getIonAbundance((i5011feiii), tem=temN2, den=ne_s2, to_eval='L(5011)')											
labFe3i5011feiiid4 = 12.0 + np.log10(abFe3i5011feiiid4)

abFe3i5085feiiid4 = Fe3.getIonAbundance((i5085feiii), tem=temN2, den=ne_s2, to_eval='L(5085)')											
labFe3i5085feiiid4 = 12.0 + np.log10(abFe3i5085feiiid4)

abFe3i5270feiiid4 = Fe3.getIonAbundance((i5270feiii), tem=temN2, den=ne_s2, to_eval='L(5270)')											
labFe3i5270feiiid4 = 12.0 + np.log10(abFe3i5270feiiid4)

abFe3i5412feiiid4 = Fe3.getIonAbundance((i5412feiii), tem=temN2, den=ne_s2, to_eval='L(5412)')											
labFe3i5412feiiid4 = 12.0 + np.log10(abFe3i5412feiiid4)

#print(labFe3i3323feiiid4)
print(labFe3i4009feiiid4)
print(labFe3i4131feiiid4)
#print(labFe3i4607feiiid4)
print(labFe3i4659feiiid4)
print(labFe3i4668feiiid4)
print(labFe3i4701feiiid4)
print(labFe3i4734feiiid4)
print(labFe3i4755feiiid4)
print(labFe3i4770feiiid4)
print(labFe3i4778feiiid4)
print(labFe3i4881feiiid4)
print(labFe3i4925feiiid4)
print(labFe3i4931feiiid4)
print(labFe3i4986feiiid4)
print(labFe3i4987feiiid4)
print(labFe3i5011feiiid4)
print(labFe3i5085feiiid4)
print(labFe3i5270feiiid4)
print(labFe3i5412feiiid4)