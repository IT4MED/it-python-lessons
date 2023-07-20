import cv2

# Загрузка изображения
image = cv2.imread('medical_image.jpg')

# Применение фильтра Гаусса для сглаживания изображения
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Отображение исходного и обработанного изображения
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
