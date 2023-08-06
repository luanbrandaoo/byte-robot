import wikipedia
from random import choice
import requests
from bs4 import BeautifulSoup
import cv2
import base64
import numpy as np
import re

def remove_specific_words(query, words_to_remove):
    words = re.findall(r'\b\w+\b', query)
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    return ' '.join(filtered_words)

def crop_face(input_image_path, target_size=(160, 128)):
    try:
        response = requests.get(input_image_path)
        arr = np.asarray(bytearray(response.content), dtype=np.uint8)
        image = cv2.imdecode(arr, -1)  # 'Load it as it is'

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

        if len(faces) > 0:
            x, y, w, h = faces[0]

            center_x = x + w // 2
            center_y = y + h // 2

            half_width = target_size[0] // 2
            half_height = target_size[1] // 2

            left = max(0, center_x - half_width)
            top = max(0, center_y - half_height)
            right = min(image.shape[1], center_x + half_width)
            bottom = min(image.shape[0], center_y + half_height)

        else:
            center_x = image.shape[1] // 2
            center_y = image.shape[0] // 2 - 50
            half_width = target_size[0] // 2
            half_height = target_size[1] // 2

            top = max(0, center_y - half_height)
            bottom = min(image.shape[0], center_y + half_height)

            left = center_x - half_width
            right = center_x + half_width

        cropped_image = image[top:bottom, left:right]

        resized_image = cv2.resize(cropped_image, target_size, interpolation=cv2.INTER_AREA)

        a , b = cv2.imencode('.png', resized_image)
        jpg_as_text = base64.b64encode(b)
        return str(jpg_as_text)[2:-1]

    except Exception as e:
        print(f"Erro ao cortar a imagem: {str(e)}")

wikipedia.set_lang("pt")

search_init_list = ['o que e','o que foi','quem foi','quem e','quando foi','quando e','como e','pesquise','como foi','como aconteceu','onde']
error_responses = ["Desculpe, não consegui encontrar"]

def detect_search(input):
    for init in search_init_list:
        if init in input:
            return True
    return False

def extract_main_image(page_title):
    page_url = wikipedia.page(page_title).url
    response = requests.get(page_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    infobox = soup.find('table', class_='infobox')

    main_image = None
    if infobox:
        images = infobox.find_all('img')
        for image in images:
            src = image.get('src')
            if src and not (src.startswith('data:') or 'icon' in src.lower() or 'small' in src.lower()):
                main_image = src
                break

    if main_image and not main_image.startswith('http'):
        main_image = f'https:{main_image}'

    return main_image

def wikipedia_search(query):
    words_to_remove = ['o que e','que foi','quem','quando','como','pesquise','sobre','onde','foi','aconteceu','diga','fale','explique','me','quem']

    query = remove_specific_words(query, words_to_remove)
    
    print('wikipedia_search: '+query)
    try:
        main_image = extract_main_image(query)
        wp_page = wikipedia.page(query)

        summary_short = ". ".join(wp_page.summary.split(". ")[:1]) + "."

        if main_image:
            return [summary_short, crop_face(main_image)]
        else:
            return choice(error_responses)
    except:
        return choice(error_responses)

if __name__ == "__main__":
    print(wikipedia_search(input('search: ')))
