import cv2

# Загрузка изображения
image = cv2.imread('medical_image.jpg')

# Отображение изображения
cv2.imshow('Medical Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
