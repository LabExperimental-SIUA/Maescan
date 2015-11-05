import logging
import shutil
import pyexiv2
import os
import Image

#Funcion reutilizada de autorotate.py de spreads para rotar las imagenes una vez tomadas con chdkptp.
def autorotate_image(name, in_path, out_path):
    num  = int(os.path.splitext(name)[0])
    img = Image(filename=in_path)

    if(num%2 != 0):
    	img.rotate(270)
    else:
    	img.rotate(90)
    img.save(filename=out_path)


#Rota todas las imagenes del directorio actual y las coloca en una carpeta creada llamada rotated.
def rotateImages(folder):
    path = os.getcwd()+"/"+folder+"/"+"renamed"
    print("Rotating images...")
    arr = os.listdir(path)
    percentage = 100/len(arr)
    progress = 0
    for fn in arr:
        autorotate_image(fn,path+"/"+fn,os.getcwd()+"/"+folder+"/"+"rotated/"+os.path.splitext(fn)[0]+"_rotated.jpg")
        progress+=percentage
        print(str(progress)+"%")
    print("100% \nRotation successful!")


