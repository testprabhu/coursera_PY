import os
from PIL import Image
path = 'D:\Trainings & Certification Works\GitHub_Repo\coursera_PY\Real_World_Task\Images'
dest_path = 'D:\Trainings & Certification Works\GitHub_Repo\coursera_PY\Real_World_Task\Images\Modified'
dir_list = os.listdir(path)
print(dir_list)

for i in dir_list:
    full_Path = path+"\\"+i
    with Image.open(full_Path) as im:
        im.rotate(90).resize((128,128)).save(dest_path+"\\"+i+".gif")