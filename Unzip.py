import pyzipper
import itertools

# Name of existing ZIP file
fichier_zip = 'archive.zip'  

# Possible characters (lowercase letters of the alphabet)
caracteres = 'abcdefghijklmnopqrstuvwxyz'

# Password length
longueur_mot_de_passe = 3

mot_de_passe_trouve = None

try:
    # Opening password protected ZIP file
    with pyzipper.AESZipFile(fichier_zip, 'r', compression=pyzipper.ZIP_STORED,
                            encryption=pyzipper.WZ_AES) as fichier_zip:
        
        # Cycle through all possible combinations of passwords
        for combinaison in itertools.product(caracteres, repeat=longueur_mot_de_passe):
            mot_de_passe = ''.join(combinaison)
            
            try:
                # Unzipping the file with the current password
                fichier_zip.extractall(pwd=mot_de_passe.encode('utf-8'))
                
                mot_de_passe_trouve = mot_de_passe
                break  
            
            except Exception as e:
                continue
    
    if mot_de_passe_trouve:
        print(f"File unzipped successfully, with password: '{mot_de_passe_trouve}'")
    else:
        print(f"The correct password was not found for the file '{fichier_zip}'.")
    
    print(f"End of file unzip combination.")

except FileNotFoundError:
    print(f"ZIP file '{fichier_zip}' was not found.")
except Exception as e:
    print(f"An error has occurred : {e}")
