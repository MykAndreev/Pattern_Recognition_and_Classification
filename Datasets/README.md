# Набори даних для задач класифікації та розпізнавання образів і модуль на Python для їх завантаження

Для тестування та аналізу програмної реалізації методів розпізнавання образів пропонується використовувати класичні набори даних для розпізнавання з `Neural Network Datasets`, які призначені для розгляду задачі розпізнання образів та класифікації у середовищі MATLAB:

- `simpleclass_dataset`	-	Simple pattern recognition dataset.
- `cancer_dataset`		-	Breast cancer dataset.
- `crab_dataset`		-	Crab gender dataset.
- `iris_dataset`		-	Iris flower dataset.
- `wine_dataset`		-	Italian wines dataset.

Ці набори даних входять до колекції баз даних [UCI Machine Learning Repository](http://archive.ics.uci.edu), де є їх докладний опис. Отримати дані із одного з наборів даних можна викликавши функцію з ім'ям, що збігається з назвою набору даних. Щоб це можна було зробити в Python, до цих наборів даних доданий модуль `datasets.py`, що забезпечує це.

# Набір даних `iris_dataset`

Цей набір даних містить інформацію про різні види ірисів. Кожен зразок представлений чотирма характеристиками:

*   Довжина чашолистків (sepal length) в см
*   Ширина чашолистків (sepal width) в см
*   Довжина пелюсток (petal length) в см
*   Ширина пелюсток (petal width) в см

Набір даних містить 150 зразків, кожен з яких належить до одного з трьох видів ірисів:

## Види ірисів

*   Setosa
*   Versicolor
*   Virginica

## Формат даних

Набір даних складається з двох матриць:

*   `irisInputs`: Матриця розміром 4x150, де кожен стовпець відповідає одному зразку ірису, а кожен рядок - одній з чотирьох характеристик.
*   `irisTargets`: Матриця розміром 3x150, де кожен стовпець відповідає одному зразку ірису.  Кожен стовпець містить вектор, де 1 знаходиться в тому рядку, який відповідає виду ірису, а інші елементи дорівнюють 0.  Це так зване "one-hot encoding" представлення міток класів.

## Використання

Цей набір даних часто використовується для задач класифікації в машинному навчанні. Мета полягає в тому, щоб навчити модель, яка здатна класифікувати іриси на основі їх характеристик.  Також, можливе використання для задач кластеризації.

## Джерела

Цей набір даних доступний у репозиторії машинного навчання UCI:

[http://mlearn.ics.uci.edu/MLRepository.html](http://mlearn.ics.uci.edu/MLRepository.html)

Джерело: Murphy, P.M., Aha, D.W. (1994). UCI Repository of machine learning databases. Irvine, CA: University of California, Department of Information and Computer Science.  На основі даних, наданих R.A. Fisher.

## Завантаження `iris_dataset` та обробка за допомогою модуля `datasets.py`

Для завантаження та обробки набору даних `iris_dataset` за допомогою модуля `datasets.py`, виконайте наступні кроки:

1.  Імпортуйте модуль `datasets` та бібліотеку `numpy` у свій Python скрипт:

    ```python
    import sys
    import numpy as np
    from datasets import iris_dataset
    ```

2.  Додайте шлях до каталогу, де знаходиться модуль `datasets.py`, якщо необхідно:

    ```python
    sys.path.append("d:\\My work\\Python\\My Python\\Pattern Recognition and Classification\\Datasets")
    ```

3.  Викличте функцію `iris_dataset()` для завантаження даних:

    ```python
    inputs, targets = iris_dataset()
    ```

    Функція `iris_dataset()` повертає кортеж, що містить:

    *   `inputs`: Матриця 4x150 з характеристиками ірисів.
    *   `targets`: Матриця 3x150 з мітками класів у форматі one-hot encoding.

4.  Застосуйте завантажені дані:

    ```python
    print(f"Shape of inputs: {inputs.shape}. Shape of targets: {targets.shape}.")
    print('Перші 5 стовпців inputs:')
    print(inputs[:, 0:5])
    print('Перші 20 стовпців targets:')
    print(targets[:, 0:20])
    targets = np.argmax(targets, axis=0)
    print('Перші елементи переробленого масиву targets:')
    print(targets[0:31])
    ```

**Важливо:** Для подальшої роботи з даними, найчастіше зручніше мати мітки класів у вигляді вектора (0, 1, 2). Тому, ми використовуємо `np.argmax(targets, axis=0)` для конвертації one-hot representation в вектор міток. Саме цей вектор `targets` і потрібно використовувати в більшості алгоритмів машинного навчання.


# Набір даних `wine_dataset`

Цей набір даних містить результати хімічного аналізу вин з трьох виноробень в Італії. Кожен зразок вина представлений тринадцятьма характеристиками:

*   Alcohol
*   Malic acid
*   Ash
*   Alcalinity of ash
*   Magnesium
*   Total phenols
*   Flavanoids
*   Nonflavanoid phenols
*   Proanthocyanins
*   Color intensity
*   Hue
*   OD280/OD315 of diluted wines
*   Proline

Набір даних містить 178 зразків вина.

## Виноробні

*   Виноробня #1
*   Виноробня #2
*   Виноробня #3

## Формат даних

Набір даних складається з двох матриць:

*   `wineInputs`: Матриця розміром 13x178, де кожен стовпець відповідає одному зразку вина, а кожен рядок - одній з тринадцяти характеристик.
*   `wineTargets`: Матриця розміром 3x178, де кожен стовпець відповідає одному зразку вина. Кожен стовпець містить вектор, де 1 знаходиться в тому рядку, який відповідає виду виноробні, а інші елементи дорівнюють 0. Це так зване "one-hot encoding" представлення міток класів.

## Використання

Цей набір даних часто використовується для задач класифікації в машинному навчанні. Мета полягає в тому, щоб навчити модель, яка здатна класифікувати вина за виноробнею на основі їх хімічних характеристик.

## Джерела

Цей набір даних доступний у репозиторії машинного навчання UCI:

[http://mlearn.ics.uci.edu/MLRepository.html](http://mlearn.ics.uci.edu/MLRepository.html)

Джерело: Murphy, P.M., Aha, D.W. (1994). UCI Repository of machine learning databases. Irvine, CA: University of California, Department of Information and Computer Science.  На основі даних, наданих Stefan Aeberhard.

## Завантаження `wine_dataset` та обробка за допомогою модуля `datasets.py`

Для завантаження та обробки набору даних `wine_dataset` за допомогою модуля `datasets.py`, виконайте наступні кроки:

1.  Імпортуйте модуль `datasets` та бібліотеку `numpy` у свій Python скрипт:

    ```python
    import sys
    import numpy as np
    from datasets import wine_dataset
    ```

2.  Додайте шлях до каталогу, де знаходиться модуль `datasets.py`, якщо необхідно:

    ```python
    sys.path.append("d:\\My work\\Python\\My Python\\Pattern Recognition and Classification\\Datasets")
    ```

3.  Викличте функцію `wine_dataset()` для завантаження даних:

    ```python
    inputs, targets = wine_dataset()
    ```

    Функція `wine_dataset()` повертає кортеж, що містить:

    *   `inputs`: Матриця 13x178 з характеристиками вин.
    *   `targets`: Матриця 3x178 з мітками класів у форматі one-hot encoding.

4.  Застосуйте завантажені дані:

    ```python
    print(f"Shape of inputs: {inputs.shape}. Shape of targets: {targets.shape}.")
    print('Перші 5 стовпців inputs:')
    print(inputs[:, 0:5])
    print('Перші 20 стовпців targets:')
    print(targets[:, 0:20])
    targets = np.argmax(targets, axis=0)
    print('Перші елементи переробленого масиву targets:')
    print(targets[0:31])
    ```

**Важливо:** Для подальшої роботи з даними, найчастіше зручніше мати мітки класів у вигляді вектора (0, 1, 2). Тому, ми використовуємо `np.argmax(targets, axis=0)` для конвертації one-hot representation в вектор міток. Саме цей вектор `targets` і потрібно використовувати в більшості алгоритмів машинного навчання.


# Набір даних `cancer_dataset` (*Breast Cancer*)

Цей набір даних містить інформацію про біопсії зразків тканин молочної залози. Кожен зразок представлений дев'ятьма характеристиками:

*   Clump thickness
*   Uniformity of cell size
*   Uniformity of cell shape
*   Marginal Adhesion
*   Single epithelial cell size
*   Bare nuclei
*   Bland chromatin
*   Normal nucleoli
*   Mitoses

Набір даних містить 699 зразків біопсій.

## Класи

*   Benign (Доброякісні)
*   Malignant (Злоякісні)

## Формат даних

Набір даних складається з двох матриць:

*   `cancerInputs`: Матриця розміром 9x699, де кожен стовпець відповідає одному зразку біопсії, а кожен рядок - одній з дев'яти характеристик.
*   `cancerTargets`: Матриця розміром 2x699, де кожен стовпець відповідає одному зразку біопсії. Кожен стовпець містить вектор, де 1 знаходиться в тому рядку, який відповідає класу (доброякісний або злоякісний), а інший елемент дорівнює 0. Це так зване "one-hot encoding" представлення міток класів.

## Використання

Цей набір даних часто використовується для задач класифікації в машинному навчанні. Мета полягає в тому, щоб навчити модель, яка здатна класифікувати біопсії як доброякісні або злоякісні на основі їх характеристик.

## Джерела

Цей набір даних доступний у репозиторії машинного навчання UCI:

[http://mlearn.ics.uci.edu/MLRepository.html](http://mlearn.ics.uci.edu/MLRepository.html)

Джерело: Murphy, P.M., Aha, D.W. (1994). UCI Repository of machine learning databases. Irvine, CA: University of California, Department of Information and Computer Science.  На основі даних, наданих Olvi Mangasarian.

## Завантаження та обробка `cancer_dataset` за допомогою модуля `datasets.py`

Для завантаження та обробки набору даних `cancer_dataset` за допомогою модуля `datasets.py`, виконайте наступні кроки:

1.  Імпортуйте модуль `datasets` та бібліотеку `numpy` у свій Python скрипт:

    ```python
    import sys
    import numpy as np
    from datasets import cancer_dataset
    ```

2.  Додайте шлях до каталогу, де знаходиться модуль `datasets.py`, якщо необхідно:

    ```python
    sys.path.append("d:\\My work\\Python\\My Python\\Pattern Recognition and Classification\\Datasets")
    ```

3.  Викличте функцію `cancer_dataset()` для завантаження даних:

    ```python
    inputs, targets = cancer_dataset()
    print(f"Shape of inputs: {inputs.shape}. Shape of targets: {targets.shape}.")
    print('Перші 5 стовпців inputs:')
    print(inputs[:, 0:5])
    print('Перші 20 стовпців targets:')
    print(targets[:, 0:20])
    targets = np.argmax(targets, axis=0)
    print('Перші елементи переробленого масиву targets:')
    print(targets[0:31])
    ```

    Функція `cancer_dataset()` повертає кортеж, що містить:

    *   `inputs`: Матриця 9x699 з характеристиками біопсій.
    *   `targets`: Матриця 2x699 з мітками класів у форматі one-hot encoding.

    **Важливо:** Для подальшої роботи з даними, найчастіше зручніше мати мітки класів у вигляді вектора (0, 1). Тому, ми використовуємо `np.argmax(targets, axis=0)` для конвертації one-hot representation в вектор міток. Саме цей вектор `targets` і потрібно використовувати в більшості алгоритмів машинного навчання.


# Набір даних `crab_dataset` (*Crab Sex*)

Цей набір даних містить інформацію про крабів. Кожен зразок представлений шістьма фізичними атрибутами:

*   Species
*   Frontal lip
*   Rearwidth
*   Length
*   Width
*   Depth

Набір даних містить 200 зразків крабів.

## Стать крабів

*   Female (Самки)
*   Male (Самці)

## Формат даних

Набір даних складається з двох матриць:

*   `crabInputs`: Матриця розміром 6x200, де кожен стовпець відповідає одному крабу, а кожен рядок - одному з шести фізичних атрибутів.
*   `crabTargets`: Матриця розміром 2x200, де кожен стовпець відповідає одному крабу. Кожен стовпець містить вектор, де 1 знаходиться в тому рядку, який відповідає статі краба (самка або самець), а інший елемент дорівнює 0. Це так зване "one-hot encoding" представлення міток класів.

## Використання

Цей набір даних часто використовується для задач класифікації в машинному навчанні. Мета полягає в тому, щоб навчити модель, яка здатна класифікувати крабів за статтю на основі їх фізичних атрибутів.

## Джерела

Цей набір даних доступний у репозиторії машинного навчання UCI:

[http://mlearn.ics.uci.edu/MLRepository.html](http://mlearn.ics.uci.edu/MLRepository.html)

Джерело: Murphy, P.M., Aha, D.W. (1994). UCI Repository of machine learning databases. Irvine, CA: University of California, Department of Information and Computer Science.  На основі даних, наданих Olvi Mangasarian.

## Завантаження та обробка `crab_dataset` за допомогою модуля `datasets.py`

Для завантаження та обробки набору даних `crab_dataset` за допомогою розробленого модуля `datasets.py`, виконайте наступні кроки:

1.  Імпортуйте модуль `datasets` та бібліотеку `numpy` у свій Python скрипт:

    ```python
    import sys
    import numpy as np
    from datasets import cancer_dataset
    ```

2.  Додайте шлях до каталогу, де знаходиться модуль `datasets.py`, якщо необхідно:

    ```python
    sys.path.append("d:\\My work\\Python\\My Python\\Pattern Recognition and Classification\\Datasets")
    ```

3.  Викличте функцію `crab_dataset()` для завантаження даних:

    ```python
    inputs, targets = crab_dataset()
    print(f"Shape of inputs: {inputs.shape}. Shape of targets: {targets.shape}.")
    print('Перші 5 стовпців inputs:')
    print(inputs[:, 0:5])
    print('Перші 20 стовпців targets:')
    print(targets[:, 0:20])
    targets = np.argmax(targets, axis=0)
    print('Перші елементи переробленого масиву targets:')
    print(targets[0:31])
    ```

    Функція `crab_dataset()` повертає кортеж, що містить:

    *   `inputs`: Матриця 6x200 з фізичними атрибутами крабів.
    *   `targets`: Матриця 2x200 з мітками класів у форматі one-hot encoding.

    **Важливо:** Для подальшої роботи з даними, найчастіше зручніше мати мітки класів у вигляді вектора (0, 1). Тому, ми використовуємо `np.argmax(targets, axis=0)` для конвертації one-hot representation в вектор міток. Саме цей вектор `targets` і потрібно використовувати в більшості алгоритмів машинного навчання.


# Набір даних `simpleclass_dataset` (*Simple Classification*)

Цей набір даних містить 1000 двовимірних векторів, які належать до чотирьох різних категорій.

## Характеристики

Кожен вектор представлений двома елементами (x, y).

## Категорії

Набір даних містить чотири категорії.

## Формат даних

Набір даних складається з двох матриць:

*   `simpleclassInputs`: Матриця розміром 2x1000, де кожен стовпець відповідає одному двовимірному вектору, а кожен рядок - одній координаті (x або y).
*   `simpleclassTargets`: Матриця розміром 4x1000, де кожен стовпець відповідає одному вектору. Кожен стовпець містить вектор, де 1 знаходиться в тому рядку, який відповідає категорії вектору, а інші елементи дорівнюють 0. Це так зване "one-hot encoding" представлення міток класів.

## Використання

Цей набір даних часто використовується для демонстрації навчання нейронної мережі класифікації. Мета полягає в тому, щоб навчити модель, яка здатна класифікувати двовимірні вектори за категоріями на основі їх координат.

## Джерела

Цей набір даних був створений за допомогою функції `simpleclass_create`.

## Завантаження та обробка `simpleclass_dataset` за допомогою модуля `datasets.py`

Для завантаження та обробки набору даних Simple Classification за допомогою розробленого модуля `datasets.py`, виконайте наступні кроки:

1.  Імпортуйте модуль `datasets` та бібліотеку `numpy` у свій Python скрипт:

    ```python
    import sys
    import numpy as np
    from datasets import simpleclass_dataset
    ```

2.  Додайте шлях до каталогу, де знаходиться модуль `datasets.py`, якщо необхідно:

    ```python
    sys.path.append("d:\\My work\\Python\\My Python\\Pattern Recognition and Classification\\Datasets")
    ```

3.  Викличте функцію `simpleclass_dataset()` для завантаження даних:

    ```python
    inputs, targets = simpleclass_dataset()
    print(f"Shape of inputs: {inputs.shape}. Shape of targets: {targets.shape}.")
    print('Перші 5 стовпців inputs:')
    print(inputs[:, 0:5])
    print('Перші 20 стовпців targets:')
    print(targets[:, 0:20])
    targets = np.argmax(targets, axis=0)
    print('Перші елементи переробленого масиву targets:')
    print(targets[0:31])
    ```

    Функція `simpleclass_dataset()` повертає кортеж, що містить:

    *   `inputs`: Матриця 2x1000 з координатами векторів.
    *   `targets`: Матриця 4x1000 з мітками класів у форматі one-hot encoding.

    **Важливо:** Для подальшої роботи з даними, найчастіше зручніше мати мітки класів у вигляді вектора (0, 1, 2, 3). Тому, ми використовуємо `np.argmax(targets, axis=0)` для конвертації one-hot representation в вектор міток. Саме цей вектор `targets` і потрібно використовувати в більшості алгоритмів машинного навчання.
