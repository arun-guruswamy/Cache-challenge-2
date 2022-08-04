import random, os
import numpy as np
from collections import Counter
import glob
import time

NUMBER_OF_SEARCHES = 10
DATABASE_DIR = '/net/dali/home/mscbio/icd3/cache_competition/enamine/enamine_split_smi/'

def select_molecules():

    n_mols_written = 0

    # create a file to write on
    fout = open('molecules_list1.smi', 'w')

    # Create smi_file_list     
    smi_list = glob.glob(DATABASE_DIR + '*.smi')

    #Create random list of file numbers to open based on number of searches
    file_num_list = np.random.randint(0, 4406, size=NUMBER_OF_SEARCHES)

    #Tally repeating file numbers
    tallied_file_list = Counter(file_num_list)

    checkpoint = time.time()

    #Open each file and select random molecules
    for f in tallied_file_list.keys():
        with open(smi_list[f], 'rt') as fin: 

            #Create random list of lines to pick for molcules
            num_lines = sum(1 for line in fin)
            mol_list = np.random.permutation(num_lines+1)[:tallied_file_list.get(f)].tolist()

            #Reset file iteration
            fin.seek(0)      

            #Select molecules based on mol_list and write onto file
            for i, line in enumerate(fin):
                if i+1 in mol_list:
                    fout.write(line)
                    n_mols_written += 1
                    print(f'{n_mols_written} written in {(time.time() - checkpoint):.1f} seconds', flush=True)
                if i+1 >= max(mol_list):
                    break
                         
    fout.close()

select_molecules()


