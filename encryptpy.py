#Author Francesco Margiotta

import os
import sys
import base64
from cryptography.fernet import Fernet
banner = '''  ______                                   _
 |  ____|                                 | |
 | |__    _ __    ___  _ __  _   _  _ __  | |_  _ __   _   _
 |  __|  | '_ \  / __|| '__|| | | || '_ \ | __|| '_ \ | | | |
 | |____ | | | || (__ | |   | |_| || |_) || |_ | |_) || |_| |
 |______||_| |_| \___||_|    \__, || .__/  \__|| .__/  \__, |
                              __/ || |         | |      __/ |
                             |___/ |_|         |_|     |___/
'''
print(banner)
print("****************************************************************************")
print("Encrypt your files using for each of them a symmetric unique encryption key")
print("Based on cryptography built in library")
print("****************************************************************************")
if (len(sys.argv)<4):
    print("Encryptpy v 1.0\n")
    print("Usage: ./encrypty.py 1|0 <input file> <output file>")
    print("1=Encrypt input file")
    print("0=Decrypt input file")
    print("****************************************************************************")
    print("Encrypt your files using for each of them a symmetric unique encryption key")
    print("Based on cryptography built in library")
    print("Example: ./encryptpy 1 fileinput.txt fileoutput.txt")
    print("****************************************************************************")
    exit(1)
mode= sys.argv[1]
ifile = sys.argv[2]
ofile = sys.argv[3]
if (int(mode)==1):
    tok = open("./token.txt", "a")   #da inserire controllo se il file richiesto è stato già cifrato. Altrimenti avrei stesso file con 2 chiavi!!!
                                            # <file input> <chiave simmetrica> <file output>
    fo = open(ofile,"a")
    try:
        with open(ifile,"r") as fi:
            key = Fernet.generate_key()
            print("Generating Fernet key...\n[IT]Genero le chiavi di Fernet...")
            ifile1 = base64.b64encode(ifile.encode())
            ifile1 = ifile1.decode()
            ofile1 = base64.b64encode(ofile.encode())
            ofile1 = ofile1.decode()
            print("Encoding informations...\n[IT]Codifico le informazioni")
            tok.write(str(ifile1) + "\t" + key.decode() + "\t" + str(ofile1))
            tok.write("\n")
            print("token.txt generated. Keep it in a safe place! it will allow you to decrypt your files.\n[IT]File token.txt generato. Tienilo in un posto sicuro! Ti permetterà di decifrare i tuoi file")
            for line in fi:
                    f = Fernet(key)
                    token = f.encrypt(line.encode())
                    enc = token.decode()
                    fo.write(enc)
                    fo.write("\n")
        c=input("File encrypted. Would you like to remove original file?[Y/N]\n[IT]File criptato. Vuoi cancellare il file originale??[Y/N]: ")
        if (c == 'Y' or c == 'y' or c == 'yes' or c == 'Yes'):
            os.remove(ifile)
            print("Original file removed.\n[IT]File originale rimosso")
    except:
        print("Errore apertura file")
        exit(1)
else:    #UNA VOLTA DECODIFICATO IL FILE, DEVO CANCELLARE QUELLO CIFRATO E CANCELLARE ANCHE L'ENTRY NEL FILE TOKEN.TXT (ALTRIMENTI NON POSSO CIFRARLO UNA SECONDA VOLTA)
    try:
        print("Reading token.txt\n[IT]Sto leggendo il file token.txt")
        with open("./token.txt", "r") as tok:
            for line in tok:
                list =line.split()
                filenc= base64.b64decode(list[2].encode()) #nome file output
                file = filenc.decode()
                if(file == ifile):
                    print(file + " " + ifile)
                    key = list[1]
                    break
                else:
                    continue
        print("Decoding data...\n[IT]Decodifico i dati")
        print(key)
        f = Fernet(key)
        with open(ifile,"rb") as fi:
            for line in fi:
                with open(ofile, "a") as fo:
                    line2 = f.decrypt(line)
                    msg = line2.decode()
                    fo.write(msg)
        print("Removing encrypted file.\n[IT]Rimuovo il file criptato")
        os.remove(ifile)
        f = open("./token.txt","r+")
        print("Updating token.txt...")
        d = f.readlines()
        f.seek(0)
        for i in d:
            x = i.split()
            y = base64.b64decode(x[2].encode())
            z= y.decode()
            if z != file:
                f.write(i)
        f.truncate()
        f.close()
        del x,y,z
    except:
        print("Errore apertura file")
        exit(1)
