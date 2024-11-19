# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 01:34:27 2023

@author: PC
"""

# Galaxia-4 HSC J1631+4426
import pyneb as pn
import numpy as np

# Datos Atomicos --------------------------------------------------------------
DataFileDict = {
'O2': {'atom': 'o_ii_atom_FFT04.dat', 'coll': 'o_ii_coll_Kal09.dat'},
'O3': {'atom': 'o_iii_atom_FFT04-SZ00.dat', 'coll': 'o_iii_coll_SSB14.dat'},
'Ne3': {'atom': 'ne_iii_atom_GMZ97.dat', 'coll': 'ne_iii_coll_McLB00.dat'},
'N2': {'atom': 'n_ii_atom_FFT04.dat', 'coll': 'n_ii_coll_T11.dat'},  
'S2': {'atom': 's_ii_atom_FFTI06.dat', 'coll': 's_ii_coll_TZ10.dat'},
'S3': {'atom': 's_iii_atom_FFTI06.dat', 'coll': 's_iii_coll_GRHK14.dat'},  
'Ar3':{'atom': 'ar_iii_atom_MB09.dat', 'coll': 'ar_iii_coll_MB09.dat'}, 
'Ar4':{'atom': 'ar_iv_atom_MZ82.dat', 'coll': 'ar_iv_coll_RB97.dat'},
'Fe3':{'atom': 'fe_iii_atom_Q96_J00.dat', 'coll': 'fe_iii_coll_Z96.dat'}
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
O2 = pn.Atom('O',2)
O3 = pn.Atom('O',3)
Ne3 = pn.Atom('Ne',3)
N2 = pn.Atom('N',2)
S2 = pn.Atom('S',2)
S3 = pn.Atom('S',3)
Ar3 = pn.Atom('Ar',3)
Ar4 = pn.Atom('Ar',4)
Fe3 = pn.Atom('Fe',3,NLevels=34)

# Intensidades ----------------------------------------------------------------
i3726 = 0	
i3729 = 0	
Otot = 50.12		
i3869 = 21.73	
i3968 = 0	
i4363 = 8.18	
i4659 = 0.92		
i4711 = 1*0.35*0
i4740 = 1*0.36*0	
i4959 = 55.76	
i5007 = 170.92		
i6312 = 1*0.55*0	
i6548 = 1*0.50*0	
i6584 = 1*0.48*0		
i6716 = 0
i6731 = 0
i7136 = 0
i7320 = 1*0.48*0	
i7330 = 1*0.54*0

# Densidad Inicial ------------------------------------------------------------
den = 100.0

# Temperaturas ----------------------------------------------------------------
if i4363 !=0.0:
  if i5007 !=0.0 and i4959 !=0.0:
   temO3 = O3.getTemDen(0.034, den=den, to_eval = 'L(4363)/(L(4959)+L(5007))') 
  if i5007 !=0.0 and i4959 ==0.0:
   temO3 = O3.getTemDen(i4363/i5007, den=den, to_eval = 'L(4363)/L(5007)') 
  if i5007 ==0.0 and i4959 !=0.0:
   temO3= O3.getTemDen(i4363/i4959, den=den, to_eval = 'L(4363)/L(4959)') 

if i7320 !=0.0 and i7330 !=0.0:
 temO2= O2.getTemDen((Otot)/(i7320+i7330), den=den, to_eval = '(L(3726)+L(3729))/(L(7319)+L(7320)+L(7330)+L(7331))')  
else:
 temO2 = 0.7*temO3 + 3000.0

print(temO3)
print(temO2)

# Densidades ------------------------------------------------------------------
if i6716 !=0.0 and i6731 !=0.0:
  ne_s2 = S2.getTemDen(i6716/i6731, tem=temO3, to_eval = 'L(6716)/L(6731)')
else:
  ne_s2 = -1
if i3726 !=0.0 and i3729 !=0.0:
  ne_o2 = O2.getTemDen(i3726/i3729, tem=temO3, to_eval = 'L(3726)/L(3729)')
else:
  ne_o2 = -1

if ne_s2 ==-1 and ne_o2 ==-1:
  den = 100.0
else:
 ane = np.array([ne_s2, ne_o2])
 lne = np.log10(ane)
 mne = np.nanmean(lne)
 den = 10**mne

print(ne_s2)
print(ne_o2)
print(den)

# Abundancias O+/H+, O++/H+, O/H ----------------------------------------------
if i3726 !=0.0 and i3729 !=0.0:
 abO2 = O2.getIonAbundance(int_ratio=(i3726+i3729), tem=temO3, den=den, to_eval='L(3726)+L(3729)')
if i3726 ==0.0 and i3729 !=0.0:
 abO2 = O2.getIonAbundance(int_ratio=(Otot), tem=temO3, den=den, to_eval='L(3726)+L(3729)')
if i3726 !=0.0 and i3729 ==0.0:
 abO2 = O2.getIonAbundance(int_ratio=(Otot), tem=temO3, den=den, to_eval='L(3726)+L(3729)')
if i3726 ==0.0 and i3729 ==0.0:
 abO2 = O2.getIonAbundance(int_ratio=(Otot), tem=temO3, den=den, to_eval='L(3726)+L(3729)')

if i4959 !=0.0 and i5007 !=0.0:
    abO3 = O3.getIonAbundance(int_ratio=(i4959+i5007), tem=temO3, den=den, to_eval='L(4959)+L(5007)')
if i4959 !=0.0 and i5007 ==0.0:
    abO3 = O3.getIonAbundance(int_ratio=(i4959), tem=temO3, den=den, to_eval='L(4959)')
if i4959 ==0.0 and i5007 !=0.0:
    abO3 = O3.getIonAbundance(int_ratio=(i5007), tem=temO3, den=den, to_eval='L(5007)')

labO2 = 12.0 + np.log10(abO2)
labO3 = 12.0 + np.log10(abO3)
abO = abO2 + abO3
labO = 12.0 + np.log10(abO)

print(abO2)
print(abO3)
print(abO)
print(labO2)
print(labO3)
print(labO)

# Parametros v, w y log(O+/O++) -----------------------------------------------
v = abO2/(abO2+abO3)
w = abO3/(abO2+abO3)
PIO = np.log10(abO2/abO3)

print(v)
print(w)
print(PIO)

# Abundancias Fe++/H+, Fe/H y Fe/O y ICFs -------------------------------------
abFe3 = Fe3.getIonAbundance((i4659), tem=temO3, den=den, to_eval='L(4659)')											

labFe3 = 12.0 + np.log10(abFe3)
abFe = abFe3 * (0.036*v - 0.146 + 1.386/v)
labFe = 12.0 + np.log10(abFe)
abFeOa = abFe/abO
abFeOb = (abFe3/abO2)*((abO2/abO3)**0.08)*0.9
abFeOc = (abFe3/abO2)*((abO2/abO3)**0.58)*1.1
labFeOa = np.log10(abFeOa)
labFeOb = np.log10(abFeOb)
labFeOc = np.log10(abFeOc)
abFeb = (10**labFeOb)*abO
labFeb = 12.0 + np.log10(abFeb)
abFec = (10**labFeOc)*abO
labFec = 12.0 + np.log10(abFec)

print(abFe3)
print(labFe3)
print(abFe)
print(labFe)
print(abFeOa)
print(abFeOb)
print(abFeOc)
print(labFeOa)
print(labFeOb)
print(labFeOc)
print(abFeb)
print(labFeb)
print(abFec)
print(labFec)

# Abundancias N+/H+, N/H, N/O -------------------------------------------------
if i6548 !=0.0 and i6584 !=0.0:
 abN2 = N2.getIonAbundance(int_ratio=(i6548+i6584), tem=temO3, den=den, to_eval='L(6548)+L(6584)')
if i6548 !=0.0 and i6584 ==0.0:
 abN2 = N2.getIonAbundance(int_ratio=(i6548), tem=temO3, den=den, to_eval='L(6548)')
if i6548 ==0.0 and i6584 !=0.0:
 abN2 = N2.getIonAbundance(int_ratio=(i6584), tem=temO3, den=den, to_eval='L(6584)')
if i6548 ==0.0 and i6584 ==0.0:
 abN2 = 0

if abN2 !=0.0:
 labN2 = 12.0 + np.log10(abN2)
if abN2 ==0.0:
 labN2 = 0.0
abN = abN2 * (-0.825*v + 0.718 + 0.853/v)
if abN !=0.0:
 labN = 12.0 + np.log10(abN)
if abN ==0.0:
 labN = 0
abNO = abN/abO
if abNO !=0.0:
 labNO = np.log10(abNO)
if abNO ==0.0:
 labNO = 0

if abN2 !=0.0:
 labN2O2 = np.log10(abN2/abO2)
if abN2 ==0.0:
 labN2O2 = 0
if labN2O2 !=0.0:
 labNOb = labN2O2 + ((0.013) + (-0.793*w) + (8.177*(w**2)) + (-23.194*(w**3)) + (26.364*(w**4)) + (-10.536*(w**5)))
if labN2O2 ==0.0:
 labNOb = 0
if labNOb !=0.0:
 abNOb = 10**(labNOb)
if labNOb ==0.0:
 abNOb = 0
abNb = abNOb * abO
if abNb !=0.0:
 labNb = 12.0 + np.log10(abNb)
if abNb ==0.0:
 labNb = 0

print(abN2)
print(labN2)
print(abN)
print(labN)
print(abNO)
print(labNO)
print(labN2O2)
print(labNOb)
print(abNOb)
print(abNb)
print(labNb)

# Abundancia iónica de S+/H+, S++/H+, S/H -------------------------------------
if i6716 !=0.0 and i6731 !=0.0:
 abS2 = S2.getIonAbundance((i6716+i6731), tem=temO3, den=den, to_eval='L(6717)+L(6731)')
if i6716 !=0.0 and i6731 ==0.0:
 abS2 = S2.getIonAbundance(i6716, tem=temO3, den=den, to_eval='L(6717)')																								
if i6716 ==0.0 and i6731 !=0.0:
 abS2 = S2.getIonAbundance(i6731, tem=temO3, den=den, to_eval='L(6731)')
if i6716 ==0.0 and i6731 ==0.0:
 abS2 = 0

if i6312 !=0.0: 
 abS3 = S3.getIonAbundance(i6312, tem=temO3, den=den, to_eval='L(6312)')
if i6312 ==0.0:
 abS3 = 0

if abS2 !=0.0:
 labS2 = 12.0 + np.log10(abS2)
if abS2 ==0.0:
 labS2 = 0
if abS3 !=0.0:
 labS3 = 12.0 + np.log10(abS3)
if abS3 ==0.0:
 labS3 = 0
if abS2 !=0.0 and abS3 !=0.0:
 abS = abS2 + abS3
else:
 abS = 0
if abS !=0.0:
 labS = 12.0 + np.log10(abS)
if abS ==0.0:
 labS = 0
abSO = abS/abO
if abSO !=0.0:
 labSO = np.log10(abSO)
if abSO ==0.0:
 labSO = 0

if abS2 !=0.0:
 labS2O2 = np.log10(abS2/abO2)
if abS2 ==0.0:
 labS2O2 =0
if labS2O2 !=0.0:
 labSOb = labS2O2 + ((0.078) + (1.084*w) + (5.808*(w**2)) + (-26.537*(w**3)) + (35.967*(w**4)) + (-16.298*(w**5)))
if labS2O2 ==0.0:
 labSOb = 0
if labSOb !=0.0:
 abSOb = 10**(labSOb)
if labSOb ==0.0:
 abSOb = 0
abSb = abSOb * abO
if abSb !=0.0:
 labSb = 12 + np.log10(abSb)
if abSb ==0.0:
 labSb = 0

print(abS2)
print(labS2)
print(abS3)
print(labS3)
print(abS)
print(labS)
print(abSO)
print(labSO)
print(labS2O2)
print(labSOb)
print(abSOb)
print(abSb)
print(labSb)

# Abundancia iónica de Ne++/H+, Ne/H, Ne/O ------------------------------------
if i3869 !=0.0 and i3968 !=0.0:
 abNe3 = Ne3.getIonAbundance((i3869+i3968), tem=temO3, den=den, to_eval='L(3869)+L(3968)')
if i3869 !=0.0 and i3968 ==0.0:
 abNe3 = Ne3.getIonAbundance(i3869, tem=temO3, den=den, to_eval='L(3869)')
if i3869 ==0.0 and i3968 !=0.0:
 abNe3 = Ne3.getIonAbundance((i3968), tem=temO3, den=den, to_eval='L(3968)')
 
labNe3 = 12.0 + np.log10(abNe3)
abNe = abNe3 * (-0.385*w + 1.365 + 0.022/w)
labNe = 12.0 + np.log10(abNe)
abNeO = abNe/abO
labNeO = np.log10(abNeO)

labNe3O3 = np.log10(abNe3/abO3)
labNeOb = labNe3O3 + ((-0.557) + (4.237*w) + (-8.564*(w**2)) + (4.834*(w**3)) + (2.284*(w**4)) + (-2.239*(w**5)))
abNeOb = 10**(labNeOb)
abNeb = abNeOb * abO
labNeb = 12 + np.log10(abNeb)

print(abNe3)
print(labNe3)
print(abNe)
print(labNe)
print(abNeO)
print(labNeO)
print(labNe3O3)
print(labNeOb)
print(abNeOb)
print(abNeb)
print(labNeb)

# Abundancia iónica de Ar++/H+, Ar+++/H+, Ar/H, Ar/O --------------------------
if i7136 !=0.0:
 abAr3 = Ar3.getIonAbundance(i7136, tem=temO3, den=den, to_eval='L(7136)')
if i7136 ==0.0:
 abAr3 = 0

if i4711 !=0.0 and i4740 !=0.0:
 abAr4 = Ar4.getIonAbundance((i4711+i4740), tem=temO3, den=den, to_eval='L(4711)+L(4740)')
if i4711 ==0.0 and i4740 !=0.0:
 abAr4 = Ar4.getIonAbundance((i4740), tem=temO3, den=den, to_eval='L(4740)')
if i4711 !=0.0 and i4740 ==0.0:
 abAr4 = Ar4.getIonAbundance((i4711), tem=temO3, den=den, to_eval='L(4711)')
if i4711 ==0.0 and i4740 ==0.0:
 abAr4 = 0

if abAr3 !=0.0:
 labAr3 = 12.0 + np.log10(abAr3)
if abAr3 ==0.0:
 labAr3 = 0
if abAr4 !=0.0:
 labAr4 = 12.0 + np.log10(abAr4)
if abAr4 ==0.0:
 labAr4 = 0
abAr = abAr3 * (0.278*v + 0.836 + 0.051/v)
if abAr !=0.0:
 labAr = 12.0 + np.log10(abAr)
if abAr ==0.0:
 labAr = 0
abArO = abAr/abO
if abArO !=0.0: 
 labArO = np.log10(abArO)
if abArO ==0.0:
 labArO = 0

if abAr3 !=0.0:
 labAr3O3 = np.log10(abAr3/abO3)
if abAr3 ==0.0:
 labAr3O3 = 0
if labAr3O3 !=0.0:
 labArOb = labAr3O3 + ((-1.463) + (6.993*w) + (-19.728*(w**2)) + (33.233*(w**3)) + (-29.535*(w**4)) + (10.745*(w**5)))
if labAr3O3 ==0.0:
 labArOb = 0
if labArOb !=0.0:
 abArOb = 10**(labArOb)
if labArOb ==0.0:
 abArOb = 0
abArb = abArOb * abO
if abArb !=0.0:
 labArb = 12 + np.log10(abArb)
if abArb ==0.0:
 labArb = 0

print(abAr3)
print(labAr3)
print(abAr4)
print(labAr4)
print(abAr)
print(labAr)
print(abArO)
print(labArO)
print(labAr3O3)
print(labArOb)
print(abArOb)
print(abArb)
print(labArb)