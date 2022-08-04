molecule = {}
mol_id = ""

with open('docking_sample.txt', 'rt') as fin:
    for i, line in enumerate(fin):
        if "PV" in line or "Z" in line:
            l = line.split()
            if "&" in line:
                mol_id = l[1]
            else:
                mol_id = l[0]
        if "1" in line and line.split()[0] == "1":
            molecule[mol_id] = line.split()[2]

print(molecule)