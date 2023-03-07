# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:32:01 2023

@author: fabia
"""

import great_circle_calculator.great_circle_calculator as gcc
import airportsdata

open("lines_for_planes.scn", "w").close()
open("automatic_flights_to_ams.scn", "w").close()

airports = airportsdata.load()

all_aproaches_dict = {} # [(lon, lat), distance from waypoint to landing , name of procedure file]
all_aproaches_dict['TR1']= [(4.769911, 53.110501), 70+55+27, 'TR1.scn']
all_aproaches_dict['TR2']= [(5.551945, 53.115694), 65+55+27, 'TR2.scn']
all_aproaches_dict['TR3']= [(5.972127, 52.972703), 67+55+27, 'TR3.scn']
all_aproaches_dict['TR4']= [(6.160208, 52.577659), 65+55+27, 'TR4.scn']

all_aproaches_dict['BR1']= [(5.982276, 51.918655), 120, 'LBR1.scn']
all_aproaches_dict['BR2']= [(5.905171, 51.807512), 120, 'LBR2.scn']
all_aproaches_dict['BR3']= [(5.313663, 51.499217), 110, 'LBR3.scn']
all_aproaches_dict['BR4']= [(4.782145, 51.511669), 115, 'LBR4.scn']

all_aproaches_dict['nor1']= [(3.659815, 51.505735), 30+22+21+50 , 'nor1.scn']
all_aproaches_dict['nor2']= [(3.246925, 51.58713), 35+22+21+50, 'nor2.scn']
all_aproaches_dict['nor3']= [(2.672966, 51.915571), 87+50, 'nor3.scn']
all_aproaches_dict['nor4']= [(3.161093, 52.395078), 57+50, 'nor4.scn']
all_aproaches_dict['nor5']= [(3.418542, 52.447196), 15+35+50, 'nor5.scn']
 
airport = 'EHAM'

lat = airports[airport]['lat']
lon = airports[airport]['lon']
location = (lon,lat)
print(location)
print (gcc.distance_between_points(all_aproaches_dict['nor5'][0], location, unit='meters')/1000)

airplanes = {}
planes_inside = [] 
with open('trafficNE.scn') as f:
    f = f.readlines()
    for idx, line in enumerate(f):
        with open('automatic_flights_to_ams.scn', 'a') as fd1:
            fd1.write(line)
        if 'DEST EHAM' in line:
            plane = line.strip()[12:].split()[0]
            for idx_temp, line_temp in enumerate(f):
                if f'CRE {plane}' in line_temp.strip()[12:]:
                    print(line_temp)
                    lon_plane = line_temp.strip()[12:].split()[4]
                    lat_plane = line_temp.strip()[12:].split()[3]
                    closest = 100000000000
                    final_point = ''
                    for entry_point in all_aproaches_dict.keys():
                        
                        if gcc.distance_between_points(all_aproaches_dict[entry_point][0], (lon_plane, lat_plane), unit='meters')/1000 + all_aproaches_dict[entry_point][1] < closest:
                            final_point = entry_point
                            print(all_aproaches_dict[entry_point][0], (lon_plane, lat_plane))
                            closest = gcc.distance_between_points(all_aproaches_dict[entry_point][0], (lon_plane, lat_plane), unit='meters')/1000 + all_aproaches_dict[entry_point][1]
                    
                    if closest > 270: 
                        airplanes[plane] = final_point 
                        with open('lines_for_planes.scn', 'a') as fd:
                            line_to_add = '00:00:00.00>'+'LINE '+ f'LINE_{plane} {lat_plane},{lon_plane} {all_aproaches_dict[final_point][0][1]},{all_aproaches_dict[final_point][0][0]}' +'\n'
                            print(line_to_add)
                            fd.write(line_to_add)
                            
                        with open('automatic_flights_to_ams.scn', 'a') as fd1:
                            pcall_line = line_temp[:12] + plane + ' PCALL ' + str(all_aproaches_dict[final_point][2]) + '\n'
                            print('PCALL: ',pcall_line)
                            fd1.write(pcall_line)
                            
                    else:
                        planes_inside.append(plane)
                    print(f'closest =  {closest} km')
                    print('------------------------')
# print(all_aproaches_dict)

wpt = (4.769911, 53.110501)
print(wpt[0])
print(airplanes)
print(len(airplanes))
print(planes_inside)