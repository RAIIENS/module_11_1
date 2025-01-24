# Сначала устанавливаем и обновляем PIP до последней версии.
# [notice] A new release of pip is available: 23.2.1 -> 24.3.1
# [notice] To update, run: python.exe -m pip install --upgrade pip
# (.venv) PS C:\Users\asus\PycharmProjects\module_11_1> python.exe -m pip install --upgrade pip
# Requirement already satisfied: pip in c:\users\asus\pycharmprojects\module_11_1\.venv\lib\site-packages (23.2.1)
# Collecting pip
#   Obtaining dependency information for pip from https://files.pythonhosted.org/packages/ef/7d/500c9ad20238fcfcb4cb9243eede163594d7020ce87bd9610c9e02771876/pip-24.3.1-py3-none-any.whl.metadata
#   Downloading pip-24.3.1-py3-none-any.whl.metadata (3.7 kB)
# Downloading pip-24.3.1-py3-none-any.whl (1.8 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 6.1 MB/s eta 0:00:00
# Installing collected packages: pip
#   Attempting uninstall: pip
#     Found existing installation: pip 23.2.1
#     Uninstalling pip-23.2.1:
#       Successfully uninstalled pip-23.2.1
# Successfully installed pip-24.3.1
# (.venv) PS C:\Users\asus\PycharmProjects\module_11_1>

# Библиотека изображений Python PIL (Pillow) — это дружественная к пользователю версия
# обработки изображений Python. Будем применять её для обработки наших изображений.

from PIL.DdsImagePlugin import module
from PIL.ImageMath import imagemath_int

# Теперь устанавливаем нужные мне библиотеки для работы с изображениями.
# Я буду менять размеры изображений,применять фильтр для размытия изображения
# и конвертировать изображения в другой формат.

# Берём любое изображение, которое поддерживает наш редактор изображений и переносим и
# сохраняем его в папке проекта.

from PIL import Image, ImageFilter

# Выбираем изображение
image = Image.open('image1.jpeg')

# 1. Изменяем размера изображения и сохраняем с новыми параметрами
resized_image = image.resize((800, 600))
resized_image.save('resized_image.jpg')

# 2. Применяем фильтр размытия изображения и тоже сохраняем
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('blurred_image.jpg')

# 3. Конвертируем изображение в другой формат (PNG) и сохраняем в новом формате.
image.save('converted_image.png', format='PNG')

# Возможности библиотеки:
# Библиотека Pillow предоставляет много функций для работы с изображениями.
# Она включает в себя:
# Обработку изображений с возможностью изменение размера, обрезки, поворот и т.д.
# Применение фильтров: встроенные фильтры используют для размытия, резкости и других эффектов.
# Конвертация форматов: поддержка различных форматов изображений, таких как JPEG, PNG, BMP
# и другие.
# Создание новых изображений: возможность создания изображений с нуля и добавления текста
# или простых фигур.
# Таким образом библиотека Pillow значительно расширяет возможности Python в области
# обработки изображений. С ее помощью можно легко и быстро выполнять различные операции
# с изображениями, что делает ее незаменимым инструментом для разработчиков и дизайнеров.