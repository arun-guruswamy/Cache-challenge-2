import random, os
import numpy as np
from collections import Counter
import glob
import time
from rdkit import Chem
import pickle
from rdkit.Chem.rdFingerprintGenerator import GetRDKitFPGenerator

DATABASE_DIR = '/net/dali/home/mscbio/icd3/cache_competition/enamine/enamine_split_smi/'

def generate_fingerprints():
    file_count = 0
    smi_count = 0
    n_fingerprints_generated = 0

    # # create a file to write on
    # fout = open('enamine_fingerprints/fingerprints0.pkl', 'wb')

    # Create smi_file_list     
    smi_file_list = glob.glob(DATABASE_DIR + '*.smi')

    checkpoint = time.time()



    #Open each file and generate fingerprints
    for smi_file in smi_file_list:
        num_lines = sum(1 for line in open(smi_file))
        fpSize = 2048
        fingerprints = np.zeros((num_lines, fpSize), dtype=bool)
        gen = GetRDKitFPGenerator(minPath=1, maxPath=7, fpSize=fpSize)
        with open(smi_file, 'rt') as fin: 
            for i, line in enumerate(fin):
                mol = Chem.MolFromSmiles(line.split()[0])
                fingerprints[i, :] = gen.GetFingerprintAsNumPy(mol)
                # fingerprint = Chem.RDKFingerprint(mol)
                # pickle.dump(fingerprint, fout)
                smi_count += 1
                n_fingerprints_generated += 1     
                print(f'{n_fingerprints_generated} written in {(time.time() - checkpoint):.1f} seconds', flush=True)

            np.save('enamine_fingerprints1/fingerprints{file_count}.npy', fingerprints)

                # if smi_count == 1000000:
                #     file_count += 1
                #     fout.close()
                #     fout = open(f'enamine_fingerprints/fingerprints{file_count}.pkl', 'wb')
                #     smi_count = 0
                         
    # fout.close()

generate_fingerprints()