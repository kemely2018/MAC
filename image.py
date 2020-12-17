import numpy as np
import cv2
import matplotlib.pyplot as plt



def read_image(image_path):
    """Leer una imagen y devolver un vector de la imagen"""
    img = cv2.imread(image_path)
    reshape_value = 1

    for i in img.shape:
        reshape_value *= i

    return img.reshape((1, reshape_value)), img.shape


def show_image(image):
    """ Muestra una sola imagen"""
    img=cv2.imread(image)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()


def show_images(a, b):
    """ Mostrar dos imágenes una al lado de la otra """
    imga=cv2.imread(a)
    imgb=cv2.imread(b)
    plot_image = np.concatenate((imga, imgb), axis=1)
    plt.imshow(plot_image)
    plt.xticks([]), plt.yticks([])
    plt.show()
