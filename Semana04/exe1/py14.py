import os

os.chdir('/home/wander/SistemasEmbarcados/SEII-Wander_Victor_Vercosa_Mares/Semana04/exe1/')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    f_title = file_name.split('py')

    new_name = '{}'.format(f_title)

    os.rename(f, new_name)

    print(new_name)
