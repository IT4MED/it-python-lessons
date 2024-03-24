import os
import cv2

def detect_faces(input_image_path, output_image_path):
    # Загрузка файла классификатора Haar Cascade для обнаружения лиц
    face_cascade_path = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    # Чтение входного изображения
    image = cv2.imread(input_image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц на изображении
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Рисование прямоугольников вокруг обнаруженных лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Сохранение изображения с обнаруженными лицами
    cv2.imwrite(output_image_path, image)

if __name__ == "__main__":
    input_dir = 'input_img'
    output_dir = 'found_faces'

    # Создание выходной директории, если она не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Обработка всех изображений в директории с входными изображениями
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.jpg'):
            input_image_path = os.path.join(input_dir, filename)
            output_image_path = os.path.join(output_dir, filename)
            detect_faces(input_image_path, output_image_path)
            print(f"Обнаруженные лица сохранены в {output_image_path}")
