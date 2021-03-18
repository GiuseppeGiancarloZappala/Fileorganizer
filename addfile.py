import shutil
import mimetypes
import csv
import argparse
import os.path
#Ho reimplementato con argparse.

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()


lista_files=[]
my_path=("files")
dirs = os.listdir( my_path )

f_path = os.path.join("files", args.filename)

if not os.path.isfile(f_path):
    print("QUESTO FILE NON ESISTE, CONTROLLA SE HAI DIGITATO CORRETTAMENTE")
else:

    #f_path = os.path.join("files", args.filename) #punto la posizione del file in questione
    f_size = os.path.getsize(f_path)#estraggo la size
    type_file=mimetypes.guess_type(f_path) #estraggo il tipo di file
    print(f"{os.path.basename(f_path)},{type_file}, {f_size} Kbyte") # stampo le informazioni estratte
    name = os.path.basename(f_path)
    size = f_size
    type_info = type_file
    lista_files.extend((name, size, type_info))# aggiungo le informazioni alla mia lista

    info_files = tuple(lista_files[n:n + 3] for n, i in enumerate(lista_files) if n % 3 == 0) #separo le informazioni per file


    if os.path.isfile("files/recap.csv"):
        with open("files/recap.csv","a") as out:
            csv_out=csv.writer(out)#per scrivere in un file csv usiamo la funzione csv.writer
            for row in info_files:
                csv_out.writerow(row)
    else:
        with open("files/recap.csv","a") as out:
            csv_out=csv.writer(out)#per scrivere in un file csv usiamo la funzione csv.writer
            csv_out.writerow(['name','byteSize','Type_info'])#scrivo la prima riga
            for row in info_files:
                csv_out.writerow(row)

    for file in dirs:
        if os.path.isdir("files/audio/")==False: # verifico l'esistenza delle cartelle
            os.mkdir("files/audio")
        if os.path.isdir("files/docs/")==False:
            os.mkdir("files/docs")
        if os.path.isdir("files/images/")==False:
            os.mkdir("files/images")
        if file.endswith(".mp3") or file.endswith(".wav"): #verifico l'estensione dei file
            shutil.move(os.path.join("files",file),os.path.join("files/audio/",file))#sposto i files nella sottocartella corretta
        if file.endswith(".txt") or file.endswith(".odt"):
            shutil.move(os.path.join("files/",file),os.path.join("files/docs/",file))
        if file.endswith(".png") or file.endswith(".jpg")or file.endswith(".jpeg"):
            shutil.move(os.path.join("files/",file),os.path.join("files/images/",file))


