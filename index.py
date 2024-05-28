import requests
from deepface import DeepFace
import os

url_one = 'https://gas-kvas.com/grafic/uploads/posts/2023-09/1695805189_gas-kvas-com-p-kartinki-garri-potter-18.jpg'
url_two = 'https://frazy.su/wp-content/uploads/2016/07/regnum_picture_1464862366254511_normal.jpg'


response_one = requests.get(url_one)
response_two = requests.get(url_two)

current_path = os.path.dirname(os.path.abspath(__file__))
photos_path = os.path.join(current_path, 'photos')
if not os.path.exists(photos_path):
    os.makedirs(photos_path, exist_ok=True)


photo1 = os.path.join(photos_path, 'photo_one.jpg')
photo2 = os.path.join(photos_path, 'photo_two.jpg')

with open(photo1, 'wb') as file:
    file.write(response_one.content)
   
 
with open(photo2, 'wb') as file:
    file.write(response_two.content)
    
result = DeepFace.verify(photo1, photo2)
print(result)