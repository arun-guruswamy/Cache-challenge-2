molecule_id = ""
molecule_count = 0
file_count = 1
missing_values = []
nums = []
conformed = 1

fout = open('split_conformed_molecules/conformed_molecules0.sdf', 'w')

molecule_id_list = []
smi_id_list = []

missing_ids = ['PV-003879516828', 'PV-006746454243', 'PV-004824488175', 'PV-005784530337', 'PV-006220056173', 'PV-005535913760', 'PV-005718928454', 'PV-004328867115', 'Z3618811017', 'PV-005700881127', 'PV-007069508573', 'Z4125845732', 'PV-004137072887', 'Z3312453089', 'PV-003882664003', 'PV-005686507109', 'PV-004364861466', 'Z3057998745', 'PV-006196934361', 'PV-005971865992', 'PV-005719927361', 'PV-005131728745', 'Z5033311274', 'PV-006300878360', 'PV-007072616673', 'PV-005770688601', 'PV-005169800128', 'PV-006556068523', 'PV-006707350478', 'PV-004111686252', 'PV-006803202038', 'PV-005340709368', 'PV-004391505206', 'PV-005098003550', 'PV-004708703554', 'PV-003365020227', 'PV-005937958594', 'PV-004384606254', 'PV-004203664569', 'PV-006050101559', 'PV-004476874232', 'PV-004263977459', 'PV-004800385868', 'PV-005200610595', 'PV-004516302439', 'Z5034647051', 'PV-006585348516', 'PV-006009437951', 'PV-006876677131', 'PV-006692371165', 'Z4100017421', 'PV-006185842267', 'PV-006978260339', 'Z4993339932', 'PV-004411200032', 'PV-006864968604', 'PV-004509468476', 'PV-003717385113', 'PV-004788643640', 'PV-006727428049', 'PV-005145881899', 'PV-004883763927', 'PV-006626431321', 'Z1672011682', 'PV-007120766910', 'PV-004769901882', 'PV-006384777414', 'Z3578988563', 'PV-005490679908', 'PV-006867178370', 'PV-005219267841', 'Z4140819894', 'PV-006463718519']

for i in range(100):
    with open(f'conformed_molecules/conformed_molecules{i}.sdf', 'rt') as fin:
        for j, line in enumerate(fin):
            if "PV" in line or "Z" in line:
                l = line.split()
                if "|" in line:
                    cur_molecule_id = l[1]
                else:
                    cur_molecule_id = l[0]
   
                if molecule_id != cur_molecule_id:
                    conformed = 1
                    molecule_count += 1             
                    molecule_id = cur_molecule_id

                    if molecule_count > 200:       
                        fout.close()                       
                        fout = open(f'split_conformed_molecules/conformed_molecules{file_count}.sdf', 'w')
                        fout.write(line)
                        file_count += 1
                        molecule_count = 1
                    else:
                        fout.write(line)
                elif molecule_id == cur_molecule_id:
                    conformed = 0
                    continue
            elif conformed == 0:
                continue
            else:
                fout.write(line)    

fout.close()   


    # with open(f'molecules/molecule_group{i}.smi', 'rt') as fin:
    #     for j, line in enumerate(fin):
    #         l = line.split()
    #         if "|" in line:
    #             cur_molecule_id = l[2]

    #         else:
    #             cur_molecule_id = l[1]
    #         smi_id_list.append(cur_molecule_id)
            


