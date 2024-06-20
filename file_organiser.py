import os
import shutil

# Extensions pour les fichiers audio
audios_ext = ['.mp3', '.wav', '.flac', '.aac', '.ogg']

# Extensions pour les images
images_ext = ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff']

# Extensions pour les documents
docs_ext = ['.pdf', '.txt', '.doc', '.docx', '.odt', '.rtf', '.html', '.htm']

# Extensions pour les fichiers CSV
csv_ext = ['.csv', '.tsv']

# Extensions pour les autres fichiers
autres_ext = ['.zip', '.rar', '.7z', '.tar', '.gz']



# Prendre l’extension du fichier pour séparer par type d’extension
def prendre_extension(nom):
    index = nom.rfind('.')
    return nom[index:] if index != -1 else ''


# Créer une fonction pour organiser les fichiers
def organiser(folder):
    audios_dir = os.path.join(folder, 'audios')
    images_dir = os.path.join(folder, 'images')
    docs_dir = os.path.join(folder, 'documents')
    csv_dir = os.path.join(folder, 'csv')
    autres_dir = os.path.join(folder, 'autres')

    # Créer les répertoires si ils n'existent pas
    for dir in [audios_dir, images_dir, docs_dir, csv_dir, autres_dir]:
        if not os.path.isdir(dir):
            os.mkdir(dir)

    noms_fichiers = os.listdir(folder)
    
    for fichier in noms_fichiers:
        # Ignorer les répertoires
        if os.path.isdir(os.path.join(folder, fichier)):
            continue

        # Prendre l'extension du fichier en lettres minuscules
        extension = str.lower(prendre_extension(fichier))
        print(fichier, extension)
        
        # Déterminer le nouveau dossier basé sur l'extension
        if extension in audios_ext:
            nouveau_folder = audios_dir
        elif extension in images_ext:
            nouveau_folder = images_dir
        elif extension in docs_ext:
            nouveau_folder = docs_dir
        elif extension in csv_ext:
            nouveau_folder = csv_dir
        else:
            nouveau_folder = autres_dir

        # Déplacer le fichier vers son dossier correspondant
        vieux = os.path.join(folder, fichier)
        nouveau = os.path.join(nouveau_folder, fichier)
        os.rename(vieux, nouveau)
        print('Moveu', vieux, '--->', nouveau)



# Spécifier le dossier à organiser
folder = 'C:\\Users\\lisia\\OneDrive\Documents'

# Appeler la fonction pour organiser les fichiers
organiser(folder)




