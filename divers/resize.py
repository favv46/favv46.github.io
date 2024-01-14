from PIL import Image
import os

def crop_and_resize_images(input_folder, output_folder, target_size=1000):
    # Assurez-vous que le dossier de sortie existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Parcourir toutes les images dans le dossier d'entrée
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        # Vérifier si le chemin est un fichier et si c'est une image
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Ouvrir l'image
            with Image.open(input_path) as img:
                # Calculer les dimensions du carré de recadrage
                min_dimension = min(img.width, img.height)
                left = (img.width - min_dimension) // 2
                top = (img.height - min_dimension) // 2
                right = (img.width + min_dimension) // 2
                bottom = (img.height + min_dimension) // 2

                # Recadrer l'image en un carré
                cropped_img = img.crop((left, top, right, bottom))

                # Redimensionner l'image à la taille cible
                resized_img = cropped_img.resize((target_size, target_size))

                # Construire le chemin de sortie
                output_path = os.path.join(output_folder, filename)

                # Sauvegarder l'image redimensionnée
                resized_img.save(output_path)

if __name__ == "__main__":
    # Spécifier le dossier d'entrée contenant les images
    input_folder = "favv46.github.io\divers\img no resize"

    # Spécifier le dossier de sortie pour les images recadrées et redimensionnées
    output_folder = "favv46.github.io\divers\img resize"

    # Appeler la fonction pour recadrer et redimensionner toutes les images dans le dossier d'entrée
    crop_and_resize_images(input_folder, output_folder)

    print("Toutes les images ont été recadrées et redimensionnées avec succès.")
