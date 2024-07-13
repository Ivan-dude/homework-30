import os, time
# directory = os.getcwd()
for root, dirs, files in os.walk('.'):
  for file in files:
    if 'module_7_5.py' in files:
      file = os.path.join('module_7_5.py')
      filepath = os.path.join(root, file)
      filetime = os.path.getmtime(file)
      formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
      filesize = os.path.getsize(file)
      parent_dir = os.path.dirname(os.path.abspath(file))
      print(f'Обнаружен файл: {file}, Путь:{filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
            f'\nРодительская директория: {parent_dir}')
      break