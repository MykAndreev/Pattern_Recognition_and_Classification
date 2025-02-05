import scipy.io
import os

_DATASET_DIR = os.path.join(os.path.dirname(__file__))

def simpleclass_dataset():
    mat_data = scipy.io.loadmat(os.path.join(_DATASET_DIR, "simpleclass_dataset.mat"))
    inputs = mat_data.get("simpleclassInputs")
    targets = mat_data.get("simpleclassTargets")
    return inputs, targets

def iris_dataset():
    mat_data = scipy.io.loadmat(os.path.join(_DATASET_DIR, "iris_dataset.mat"))
    inputs = mat_data.get("irisInputs")
    targets = mat_data.get("irisTargets")
    return inputs, targets

def cancer_dataset():
    mat_data = scipy.io.loadmat(os.path.join(_DATASET_DIR, "cancer_dataset.mat"))
    inputs = mat_data.get("cancerInputs")
    targets = mat_data.get("cancerTargets")
    return inputs, targets

def crab_dataset():
    mat_data = scipy.io.loadmat(os.path.join(_DATASET_DIR, "crab_dataset.mat"))
    inputs = mat_data.get("crabInputs")
    targets = mat_data.get("crabTargets")
    return inputs, targets

def wine_dataset():
    mat_data = scipy.io.loadmat(os.path.join(_DATASET_DIR, "wine_dataset.mat"))
    inputs = mat_data.get("wineInputs")
    targets = mat_data.get("wineTargets")
    return inputs, targets


import numpy as np
from numpy.random import randint

def simpleclass_create():
    """
    Створює набір вхідних даних X та міток T для простої задачі розпізнавання образів.
    Ця функція генерує дані, які використовуються в simpleclass_dataset.
    Повертає:
        x: Матриця розміром 2x1000, що містить координати x та y для 1000 точок.
        t: Матриця розміром 4x1000, що містить мітки класів у форматі one-hot encoding.
    """

    centerx = [0, 0, 1, 1]
    centery = [0, 1, 0, 1]
    radius = [0.4, 0.4, 0.4, 0.4]

    num_samples = 1000
    x = np.zeros((2, num_samples))
    t = np.zeros((4, num_samples))

    for i in range(num_samples):
        j = randint(0, 4)  # Випадковий вибір класу (0-3)
        t[j, i] = 1  # One-hot encoding

        angle = np.random.rand() * 2 * np.pi
        r = (np.random.rand()**0.8) * radius[j]
        x[0, i] = centerx[j] + np.cos(angle) * r
        x[1, i] = centery[j] + np.sin(angle) * r

    return x, t
