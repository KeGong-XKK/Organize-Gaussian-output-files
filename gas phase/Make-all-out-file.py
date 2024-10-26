import os
import numpy as np
import re

#-----------define your path, default suffix is '.out'
file = os.listdir('./')
suffix = '.out'
#-------------------------
log = []
#### atomic number to symbol
peri = {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 
 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca', 21: 'Sc', 
 22: 'Ti', 23: 'V', 24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn', 31: 'Ga', 
 32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr', 37: 'Rb', 38: 'Sr', 39: 'Y', 40: 'Zr', 41: 'Nb', 
 42: 'Mo', 43: 'Tc', 44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag', 48: 'Cd', 49: 'In', 50: 'Sn', 
 51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe', 55: 'Cs', 56: 'Ba', 57: 'La', 58: 'Ce', 59: 'Pr', 60: 'Nd', 
 61: 'Pm', 62: 'Sm', 63: 'Eu', 64: 'Gd', 65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70: 'Yb',
 71: 'Lu', 72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir', 78: 'Pt', 79: 'Au', 80: 'Hg', 
 81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At', 86: 'Rn', 87: 'Fr', 88: 'Ra', 89: 'Ac', 90: 'Th', 
 91: 'Pa', 92: 'U', 93: 'Np', 94: 'Pu', 95: 'Am', 96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es', 100: 'Fm', 
 101: 'Md', 102: 'No', 103: 'Lr', 104: 'Rf', 105: 'Db', 106: 'Sg', 107: 'Bh', 108: 'Hs', 109: 'Mt', 
 110: 'Ds', 111: 'Rg', 112: 'Cn', 113: 'Nh', 114: 'Fl', 115: 'Mc', 116: 'Lv', 117: 'Ts', 118: 'Og' 
 }
####

for i in range(len(file)):
    if file[i].find(suffix) > -1:
        log.append(file[i])
for i in range(len(log)):
    f1 = open(log[i], 'r')
    while True:
        line = f1.readline()
        if not line:
            break
        if line.find('Deg. of freedom') > -1:
            temp = line.split()
            natom = int(int(temp[3])/3 + 2) #3N-6 Degrees
            pos=np.zeros([natom,4])
            break
    f1.close()
    
    f1 = open(log[i], 'r')
    while True:
        line = f1.readline()
        if not line:
            break
        if line.find('Center     Atomic      Atomic')>-1:
            line=f1.readline()
            line=f1.readline()
            for j in range(natom):
                line = f1.readline()
                line = line.split()
                pos[j,0]=round(int(line[1]))
                for s in range(3):
                    pos[j,s+1] = float(line[s+3])
    f1.close()
    
    out1 = log[i].replace(suffix, '')
    out = 'gas phase.xyz'
    f2 = open(out, 'a')
    print('convert ' + str(log[i]))
    f2.write(str(natom) + '\n')
    f2.write(str(out1) + '(gas)' + '\n')
    #f2.write('\n')
    for i in range(natom):
        f2.write(peri[int(pos[i, 0])] + '      ')
        for j in range(3):
            #f2.write(str(pos[i, j+1]) + '      ')
            temp= np.format_float_positional(pos[i, j+1], precision=9, unique=False, trim='k')
            f2.write(f"{temp:<20}")
        f2.write('\n')
    f2.close()