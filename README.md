# Organisateur de Fichiers

Ce script Python organise les fichiers dans un dossier donné en les déplaçant vers des sous-dossiers basés sur leurs extensions. Il est particulièrement utile pour trier des fichiers multimédias, documents, fichiers CSV, et autres types de fichiers.

## Fonctionnalités

- Organise les fichiers audio, image, document, CSV et autres dans des sous-dossiers correspondants.
- Crée les sous-dossiers nécessaires s'ils n'existent pas déjà.
- Traite uniquement les fichiers et ignore les sous-dossiers existants.

## Pré-requis

- Python 3.x

## Extensions supportées

Les extensions supportées par défaut sont :

- **Audios**: `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`
- **Images**: `.jpeg`, `.jpg`, `.png`, `.gif`, `.bmp`, `.tiff`
- **Documents**: `.pdf`, `.txt`, `.doc`, `.docx`, `.odt`, `.rtf`, `.html`, `.htm`
- **CSV**: `.csv`, `.tsv`
- **Autres**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`

## Utilisation

1. Clonez ce dépôt ou téléchargez le script `organisateur_de_fichiers.py`.
2. Assurez-vous que Python 3 est installé sur votre système.
3. Mettez à jour la variable `folder` dans le script avec le chemin du dossier que vous souhaitez organiser.
4. Exécutez le script.

```python
import os

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
        print(fichier,

Remarques
Assurez-vous d'avoir les permissions nécessaires pour créer des dossiers et déplacer des fichiers dans le dossier spécifié.
Vous pouvez ajouter ou supprimer des extensions dans les listes audios_ext, images_ext, docs_ext, csv_ext, et autres_ext selon vos besoins.
Contributions
Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour toute suggestion d'amélioration ou de correction.
