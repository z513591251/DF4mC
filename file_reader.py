import re
import numpy as np


def openFile(input_file): 
    with open(input_file) as f:
         contents = f.readlines()
    return contents


def readFasta(inpFile,maxlen):
    _hash = {}
    _seq = []
    _id = []

    for line in open(inpFile):
        if line.startswith('>'):
           name = line.replace('>','').split()[0]
           _id.append(name)
           _hash[name] = ''
        else:
           _hash[name] += line.replace('\n','')

    for i in _hash.keys():
        if len(_hash[i]) <= maxlen:
           Subseq = _hash[i] + "X" * (maxlen - len(_hash[i]))
        else:
           Subseq = _hash[i][0:maxlen]
        _seq.append(Subseq)

    return _seq, _id


def readRNAfoldFile(input_file):
# MFE: Minimum Free Energy
#EFE: Ensemble Free Energy
#Freq: Frequency of the MFE structure
# Usage: (RNAseq,RNAstructure,MFE,EFE,Freq)=readRNAfoldFile(inputfile)

    contents = openFile(input_file)
    _RNAseq = []
    _RNAstructure = []
    _MFE = []
    _EFE = []
    _Freq = []
 
    i = 0
    for line in contents:
        i += 1
        if i % 4 == 2:
           _RNAstructure.append(re.split(r'\s+',line)[0])
           _MFE.append(re.split(r'\s+',line)[2].replace(')',''))
        if i % 4 == 3:
           _EFE.append(re.split(r'\s+',line)[6])
        if i % 4 == 0:
           _Freq.append(re.split(r'\s+',line)[7].replace(';',''))
        if i % 4 == 1:
           _RNAseq.append(line.replace('\n',''))
    _MFE = np.array(list(map(float,_MFE)))
    _EFE = np.array(list(map(float,_EFE)))
    _Freq = np.array(list(map(float,_Freq)))
    return _RNAseq, _RNAstructure, _MFE, _EFE, _Freq

