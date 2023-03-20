#clearup program


newname = 'finalscenario_shortened_v2.scn'

open(newname, "w").close()


with open('finalscenario.scn') as f:
    f = f.readlines()
    for idx in range(50):
        with open(newname, "a") as fd1:
            fd1.write(f[idx])
    for idx in range(50, len(f)):
        
        with open(newname, "a") as fd1:
            
            if len(f[idx]) < 9:
                print('too short')
                
            elif 'rtf'in f[idx]:
                print(f[idx])
                
            elif f[idx-1] == f[idx]:
                print(f[idx-1])
                print(f[idx])
                
            elif f[idx-2] == f[idx] and "LNAV" not in f[idx] and "VNAV" not in f[idx]:
                print(f[idx-2])
                print(f[idx])   
                
            elif f[idx-3] == f[idx] and "LNAV" not in f[idx] and "VNAV" not in f[idx]:
                print(f[idx-2])
                print(f[idx])
            
            elif f[idx-4] == f[idx] and "LNAV" not in f[idx] and "VNAV" not in f[idx]:
                print(f[idx-2])
                print(f[idx])  
                
                
            elif f[idx-1][12:].strip().split()[0:] == f[idx][12:].strip().split()[0:]:
                if float(f[idx-1].strip().split()[0][6:8]) - float(f[idx].strip().split()[0][6:8]) < 1:
                    print(f[idx-1])
                    print(f[idx])
                else:
                    fd1.write(f[idx])
            
            elif f[idx-2][12:].strip().split()[0:] == f[idx][12:].strip().split()[0:]:
                if float(f[idx-2].strip().split()[0][6:8]) - float(f[idx].strip().split()[0][6:8]) < 1:
                    print(f[idx-2])
                    print(f[idx])
                else:
                    fd1.write(f[idx])
                    
            elif f[idx-3][12:].strip().split()[0:] == f[idx][12:].strip().split()[0:]:
                if float(f[idx-3].strip().split()[0][6:8]) - float(f[idx].strip().split()[0][6:8]) < 1:
                    print(f[idx-3])
                    print(f[idx])
                else:
                    fd1.write(f[idx])
           
            elif f[idx-4][12:].strip().split()[0:] == f[idx][12:].strip().split()[0:]:
                if float(f[idx-4].strip().split()[0][6:8]) - float(f[idx].strip().split()[0][6:8]) < 1:
                    print(f[idx-3])
                    print(f[idx])
                else:
                    fd1.write(f[idx])
                
     
                    
            else:
                fd1.write(f[idx])
       
# 
# float(f[-10].strip().split()[0][6:8]) - float(f[-9].strip().split()[0][6:8])