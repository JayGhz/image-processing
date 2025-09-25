import requests
from PIL import Image
from io import BytesIO
import os

os.makedirs("./week5/image_recommender/waifus", exist_ok=True)

urls_file = "./week5/image_recommender/urls.txt"

with open(urls_file, "r") as f:
    urls = [line.strip() for line in f if line.strip()]

count = 0
errors = []

for i, url in enumerate(urls, 1):
    try:
        img_data = requests.get(url).content
        img = Image.open(BytesIO(img_data))
        
        img = img.convert("RGB")
        
        img = img.resize((250, 250))
        
        count += 1
        img.save(f"./week5/image_recommender/waifus/waifu_{count}.jpg", "JPEG")
    
    except Exception as e:
        errors.append(f"Error en imagen {i}: {str(e)}")

print(f"Proceso completado: {count} imágenes descargadas")
if errors:
    print("\nErrores encontrados:")
    for error in errors:
        print(error)
