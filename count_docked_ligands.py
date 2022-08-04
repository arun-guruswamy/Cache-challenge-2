import gzip
from pathlib import Path

total = 0

def count_mols(sdf_file_path: Path):
    sdf_file = gzip.open(sdf_file_path)

    n_mols = 0
    for line in sdf_file:
        if line.startswith(b'$$$$'):
            n_mols += 1

    return n_mols

for i in range(500):
    total += count_mols(f"docking_results/docked{i}.sdf.gz")

print(total)

# def count_mols(x):
#     sdf_file = open(x, 'rt')

#     n_mols = 0
#     for i, line in enumerate(sdf_file):
#         if line.startswith('$$$$'):
#             n_mols += 1
            
#     sdf_file.close()
#     return n_mols

# for i in range(500):
#     total += count_mols(f"split_conformed_molecules/conformed_molecules{i}.sdf")

# print(total)