# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:17:53 2023

@author: fabia
"""
defined_airports = ['EHBK', 'EHEH', 'EHGG', 'EHKD', 'EHLE', 'EHLW', 'EHRD', 'EHSE', 'EHTE', 'EHVK']
with open('trafficNE.scn') as f:
    f = f.readlines()
    for idx, line in enumerate(f):
        # print(line)
        with open('regional_traffic_automated_v1.scn', 'a') as fd:
            fd.write(line)
        if 'DEST' in line:
            if 'DEST EHAM' not in line:
                print(line)
                print(line.split()[2])
                if line.split()[2] in defined_airports:
                    added_line = line.split()[0] + ' PCALL ' + line.split()[2] + '\n'
                    with open('regional_traffic_automated_v2.scn', 'a') as fd:
                        fd.write(added_line)
                        print(added_line)
                print('-------------------------------')
        
        #     plane = line.strip()[12:].split()[0]
        #     print(plane)
        #     for idx_temp, line_temp in enumerate(f):
        #         if plane in line_temp:
                    
            
print('number of planes to ams: ')