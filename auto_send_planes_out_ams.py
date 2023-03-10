

import great_circle_calculator.great_circle_calculator as gcc
import airportsdata

open("automatic_flights_from_ams_v2.scn", "w").close()

airports = airportsdata.load()

all_departures_dict = {} # [(lon, lat), distance from waypoint to landing , name of procedure file]
all_departures_dict['volkl9'] = [(5.37739,51.900737), 3.8+7.4+18.1+33.5, '09','volkl9.scn']
all_departures_dict['volkl36'] = [(5.37739,51.900737), 7+8.7+20+60.5, '36','volkl36.scn']
all_departures_dict['nirex9'] = [(3.816149,52.290246), 3.8+5.5+16.7+14.2+12.8+43.7,'09', 'nirex9.scn']
all_departures_dict['nirex36'] = [(3.816149,52.290246), 7+9.6+12.8+43.7, '36','nirex36.scn']
all_departures_dict['sugol9'] = [(3.967365,52.524254), 3.8+5.5+16.7+56.8,'09', 'sugol9.scn']
all_departures_dict['sugol36'] = [(3.967365,52.524254), 7+9.6+42.8, '36','sugol36.scn']
all_departures_dict['betus9'] = [(6.283798,53.830896), 3.8+5.5+41+152, '09','betus9.scn']
all_departures_dict['betus36'] = [(6.283798,53.830896), 7+8.7+33.1+152,'36', 'betus36.scn']
all_departures_dict['ehte9'] = [(6.047661,52.24474), 3.8+7.4+16.1+58.2, '09','ehte9.scn']
all_departures_dict['ehte36'] = [(6.047661,52.24474), 7+8.7+33.7+22.6+34.4,'36','ehte36.scn']
all_departures_dict['silvo9'] = [(4.904605,51.982197), 3.8+7.4+18.1+33.5,'09', 'silvo9.scn']
all_departures_dict['silvo36'] = [(4.904605,51.982197), 7+8.7+20+47.7,'36', 'silvo36.scn']

airport = 'EHAM'

lat = airports[airport]['lat']
lon = airports[airport]['lon']
location = (lon,lat)
print(location)
print (gcc.distance_between_points(all_departures_dict['sugol9'][0], location, unit='meters')/1000)
lat_rwy09 = 52.3166818750929
lat_rwy36 = 52.328458

airplanes = {}
with open('automatic_flights_to_ams_and_auto_regional.scn') as f:
    f = f.readlines()
    for idx, line in enumerate(f):
        with open("automatic_flights_from_ams_v2.scn", "a") as fd1:
            fd1.write(line)
        if 'ORIG EHAM' in line:
            plane = line.strip()[12:].split()[0]
            for idx_temp, line_temp in enumerate(f):
                if f'CRE {plane}' in line_temp.strip()[12:]:
                    print(line_temp)
                    lon_plane = float(line_temp.strip()[12:].split()[4])
                    lat_plane = float(line_temp.strip()[12:].split()[3])
                    if lat_plane-lat_rwy09<0.0001:
                        rwy = '09'
                    else:
                        rwy = '36'
                if f'{plane} DEST' in line_temp.strip()[12:]:
                    print(line_temp)
                    dest_airport = line_temp.strip()[12:].split()[2]
            lat_dest = airports[dest_airport]['lat']
            lon_dest = airports[dest_airport]['lon']
            location_dest = (lon_dest,lat_dest)
            closest = 1e10
            closest_dep_point = ''
            for dep_point in all_departures_dict.keys():
                if all_departures_dict[dep_point][2] == rwy:
                    if gcc.distance_between_points(all_departures_dict[dep_point][0], location_dest, unit='meters')/1000 + all_departures_dict[dep_point][1] < closest:
                        closest = gcc.distance_between_points(all_departures_dict[dep_point][0], location_dest, unit='meters')/1000 + all_departures_dict[dep_point][1]
                        closest_dep_point = dep_point
            airplanes[plane] = closest_dep_point
            with open("automatic_flights_from_ams_v2.scn", "a") as fd1:
                pcall_line = line[:12] + plane +' PCALL ' + str(all_departures_dict[closest_dep_point][3]) + '\n'
                print('pcall',pcall_line)
                fd1.write(pcall_line)
        elif 'ORIG EHEH' in line:
            if "DEST EHAM" not in f[idx-1]:
                with open("automatic_flights_from_ams_v2.scn", "a") as fd1:
                    plane = line.strip()[12:].split()[0]
                    pcall_line = line[:12] + plane +' PCALL ' + 'EHEHDEP' + '\n'
                    print('pcall',pcall_line)
                    fd1.write(pcall_line)
        elif 'ORIG EHVK' in line:
            if "DEST EHAM" not in f[idx-1]:
                with open("automatic_flights_from_ams_v2.scn", "a") as fd1:
                    plane = line.strip()[12:].split()[0]
                    pcall_line = line[:12] + plane +' PCALL ' + 'EHVKDEP' + '\n'
                    print('pcall',pcall_line)
                    fd1.write(pcall_line)
        elif 'ORIG EHRD' in line:
            if "DEST EHAM" not in f[idx-1]:
                with open("automatic_flights_from_ams_v2.scn", "a") as fd1:
                    plane = line.strip()[12:].split()[0]
                    pcall_line = line[:12] + plane +' PCALL ' + 'EHRDDEP' + '\n'
                    print('pcall',pcall_line)
                    fd1.write(pcall_line)
            
     elif 'ORIG EBZW' in line:
         if "DEST EHAM" not in f[idx-1]:
             with open("automatic_flights_from_ams_v2.scn", "a") as fd1:
                 plane = line.strip()[12:].split()[0]
                 pcall_line = line[:12] + plane +' PCALL ' + 'REGIONALDEP' + '\n'
                 print('pcall',pcall_line)
                 fd1.write(pcall_line)
            
