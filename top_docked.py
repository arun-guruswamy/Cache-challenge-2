def get_sdf_lines(sdf_file, idx):
    output_lines = []
    f = gzip.open(sdf_file, mode='rt')
    mol_idx = 0
    mol = []
    for line in f:
        mol.append(line)
        if line.startswith('$$$$'):
            
            # save this molecule if it is the one we are looking for
            if mol_idx == idx:
                return output_lines
            
            mol = []
            mol_idx += 1
            
    f.close()
    return output_lines


dfo = df_docked.sort_values(by='CNN_VS', ascending=False)
output_file = 'top_docked.sdf'

sdf_lines = []
for idx, row in dfo.iloc[:10].iterrows():
    sdf_file = row['docking_sample']
    pose_idx = row['pose_idx']
    sdf_lines += get_sdf_lines(sdf_file, pose_idx)
    
with gzip.open(output_file, mode='wt') as f:
    f.write(''.join(sdf_lines))