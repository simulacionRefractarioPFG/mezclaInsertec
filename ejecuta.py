import os
import glob

# Crea carpeta para albergar los arhivos con las configuraciones del sistema
os.system('sudo mkdir ./post')
# Permisos a la carpeta
os.system('sudo chmod -R 777 post')

# Aproxima
os.system('mpirun -np * liggghts < in.plantilla1')
# Comprime
os.system('mpirun -np * liggghts < in.plantilla2')
# Relaja
os.system('mpirun -np * liggghts < in.plantilla3')

# Recupera el ultimo archivo con la configuracion del sistema
newest = max(glob.iglob('./post/dump*.pruebas'), key=os.path.getctime)
os.system('mv %s ./dump1' % (newest))

# Libera
os.system('mpirun -np * liggghts < in.plantilla4')

# Recupera el ultimo archivo con la configuracion del sistema
newest = max(glob.iglob('./post/dump*.pruebas'), key=os.path.getctime)
os.system('mv %s ./dump2' % (newest))