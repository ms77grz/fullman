import os

os.chdir(r'c:\Users\Rizvan\Desktop')  # Меняем текущий каталог
print(os.getcwd())  # Проверяем

# tree = os.walk('stories')
# for i in tree:
#     print(i)


def read_dir(folder):
    for root, _, files in os.walk(folder):
        # считаем количество разделителей между папками (\ или /)
        lvl = root.count(os.sep)
        tab1 = ' ' * 4 * lvl
        tab2 = ' ' * 4 * (lvl + 1)
        print(f'{tab1}[{os.path.basename(root)}]')
        for file in files:
            print(f'{tab2}{file}')


read_dir('stories')
