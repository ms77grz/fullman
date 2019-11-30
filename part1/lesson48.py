import zipfile
import os

dir = 'c:\\webapps\\fullman\\folder'

# my_zip = zipfile.ZipFile('test.zip', 'w')

my_zip = zipfile.ZipFile(os.path.join(dir, 'test.zip'), 'w')

for folder, subfolder, files in os.walk(dir):
    # print(folder, subfolder, files)
    # print(folder)
    # print(subfolder)
    # print(files)
    # print(folder,files)
    for file in files:
        print(file)
        print(os.path.join(folder, file))
        print(os.path.relpath(os.path.join(folder, file), dir))
        if file == 'test.zip':
            continue
        # my_zip.write(os.path.join(folder, file), file, compress_type=zipfile.ZIP_DEFLATED)
        my_zip.write(os.path.join(folder, file), os.path.relpath(
            os.path.join(folder, file), dir), compress_type=zipfile.ZIP_DEFLATED)

my_zip.close()
