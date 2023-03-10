


import airportsdata

open("dep_apr_reg_v2.scn", "w").close()

airports = airportsdata.load()
defined_airports_without_eham = ['EBZW','EHBK', 'EHEH', 'EHGG', 'EHKD', 'EHLE', 'EHLW', 'EHRD', 'EHSE', 'EHTE', 'EHVK']
defined_airports = defined_airports_without_eham + ['EHAM']

airplanes = {}
with open('dep_apr_reg.scn') as f:
    f = f.readlines()
    for idx, line in enumerate(f):
        with open("dep_apr_reg_v2.scn", "a") as fd1:
            fd1.write(line)

        if 'ORIG EHEH' in line:
            if 'DEST' in f[idx-1] and f[idx-1].split()[2] not in defined_airports:
                with open("dep_apr_reg_v2.scn", "a") as fd1:
                    plane = line.strip()[12:].split()[0]
                    pcall_line = line[:12] + plane +' PCALL ' + 'EHEHDEP' + '\n'
                    print('pcall',pcall_line)
                    fd1.write(pcall_line)
        elif 'ORIG EHVK' in line:
            if 'DEST' in f[idx-1] and f[idx-1].split()[2] not in defined_airports:
                with open("dep_apr_reg_v2.scn", "a") as fd1:
                    plane = line.strip()[12:].split()[0]
                    pcall_line = line[:12] + plane +' PCALL ' + 'EHVKDEP' + '\n'
                    print('pcall',pcall_line)
                    fd1.write(pcall_line)
        elif 'ORIG EHRD' in line:
            if 'DEST' in f[idx-1] and f[idx-1].split()[2] not in defined_airports:
                with open("dep_apr_reg_v2.scn", "a") as fd1:
                    plane = line.strip()[12:].split()[0]
                    pcall_line = line[:12] + plane +' PCALL ' + 'EHRDDEP' + '\n'
                    print('pcall',pcall_line)
                    fd1.write(pcall_line)
            
        elif 'ORIG EBZW' in line:
            if 'DEST' in f[idx-1] and f[idx-1].split()[2] not in defined_airports:
                with open("dep_apr_reg_v2.scn", "a") as fd1:
                     plane = line.strip()[12:].split()[0]
                     pcall_line = line[:12] + plane +' PCALL ' + 'REGIONALDEP' + '\n'
                     print('pcall',pcall_line)
                     fd1.write(pcall_line)
    
        
        elif 'ORIG' in f[idx-1] and f[idx-1].split()[2] in defined_airports_without_eham:
            if 'DEST' in f[idx-1] and f[idx-1].split()[2] not in defined_airports:
                with open("dep_apr_reg_v2.scn", "a") as fd1:
                     plane = line.strip()[12:].split()[0]
                     pcall_line = line[:12] + plane +' PCALL ' + 'REGIONALDEP' + '\n'
                     print('pcall',pcall_line)
                     fd1.write(pcall_line)
        elif 'ORIG' in f[idx-1] and f[idx-1].split()[2] in defined_airports_without_eham:
            if 'DEST' in f[idx-1] and f[idx-1].split()[2] in defined_airports:
                with open("dep_apr_reg_v2.scn", "a") as fd1:
                     plane = line.strip()[12:].split()[0]
                     pcall_line = line[:12] + plane +' PCALL ' + 'REGIONAL' + '\n'
                     print('pcall',pcall_line)
                     fd1.write(pcall_line)
