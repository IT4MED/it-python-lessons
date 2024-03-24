import cv2

# Загрузка изображения с МРТ мозга
изображение = cv2.imread('mri_brain.jpg')

# Преобразование изображения в оттенки серого
серое_изображение = cv2.cvtColor(изображение, cv2.COLOR_BGR2GRAY)

# Создание окна для отображения изображения
cv2.namedWindow('МРТ мозга')

# Функция для применения выбранной цветовой схемы к выделенной области
def применить_цветовую_схему(цветовая_схема):
    if цветовая_схема == 'viridis':
        return cv2.applyColorMap(серое_изображение, cv2.COLORMAP_VIRIDIS)
    elif цветовая_схема == 'plasma':
        return cv2.applyColorMap(серое_изображение, cv2.COLORMAP_PLASMA)
    elif цветовая_схема == 'inferno':
        return cv2.applyColorMap(серое_изображение, cv2.COLORMAP_INFERNO)
    elif цветовая_схема == 'magma':
        return cv2.applyColorMap(серое_изображение, cv2.COLORMAP_MAGMA)
    else:
        return изображение

# Функция для обработки щелчков кнопок 
def обработать_кнопки(event, x, y, flags, param):
    global цветовая_схема
    if event == cv2.EVENT_LBUTTONDOWN:
        if 10 <= y <= 60:
            if 10 <= x <= 160:
                цветовая_схема = 'viridis'
            elif 170 <= x <= 320:
                цветовая_схема = 'plasma'
            elif 330 <= x <= 480:
                цветовая_схема = 'inferno'
            elif 490 <= x <= 640:
                цветовая_схема = 'magma'

# Установка функции обработки щелчков для окна с изображением
cv2.setMouseCallback('МРТ мозга', обработать_кнопки)

# Начальная цветовая схема - нет (исходное изображение в оттенках серого)
цветовая_схема = None

while True:
    # Применение выбранной цветовой схемы к изображению
    if цветовая_схема is not None:
        цветное_изображение = применить_цветовую_схему(цветовая_схема)
    else:
        цветное_изображение = изображение

    # Отображение изображения с кнопками
    cv2.imshow('МРТ мозга', цветное_изображение)

    # Рисование кнопок в боковой части окна
    кнопки = цветное_изображение.copy()
    cv2.rectangle(кнопки, (10, 10), (160, 60), (255, 255, 255), -1)
    cv2.putText(кнопки, 'Viridis', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.rectangle(кнопки, (170, 10), (320, 60), (255, 255, 255), -1)
    cv2.putText(кнопки, 'Plasma', (180, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.rectangle(кнопки, (330, 10), (480, 60), (255, 255, 255), -1)
    cv2.putText(кнопки, 'Inferno', (340, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.rectangle(кнопки, (490, 10), (640, 60), (255, 255, 255), -1)
    cv2.putText(кнопки, 'Magma', (500, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow('МРТ мозга', кнопки)

    # Ожидание нажатия клавиши
    key = cv2.waitKey(1) & 0xFF

    # Нажмите 'q' для выхода из цикла
    if key == ord('q'):
        break

# Закрытие окна OpenCV
cv2.destroyAllWindows()
