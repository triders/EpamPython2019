"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:
> print(folder1)
V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1
А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True

V
|   |text.txt
|   |test1
|   |   |tex10.txt
|   |test2
|   |   |text2.txt
|   |test3
|   |   |4
|   |   |   |5
|   |   |   |   |text5.txt
|   |   |   |   |text55.txt
|   |test4

"""
import os


def dir_name(path):
    """returns name of directory or file from given path"""
    return path[path.rfind('\\')+1:]


class PrintableFolder:

    def __init__(self, path):
        self.path = path
        self.name = dir_name(self.path)
        self.content = []
        for root, dirs, files in os.walk(self.path):
            self.content.append(dir_name(root))
            self.content.extend(files)

    def __str__(self):
        res = f'{self.name}\nV\n'  # exception for root
        n = 1
        depth = 0
        for root, dirs, files in os.walk(self.path):
            sep = '|   '
            prefix = n * sep

            if dir_name(root) == self.name:
                # exception for files in main root
                prefix = n * sep
                for file in files:
                    res += prefix + '|' + file + '\n'
                continue

            res += prefix + '|' + dir_name(root) + '\n'

            if dirs:
                n += 1
                depth += 1

            if files:
                n += 1
                prefix = n * sep
                for file in files:
                    res += prefix + '|' + file + '\n'
                n -= 1

            if not dirs:
                n -= depth

        return res

    def __contains__(self, item):
        return item.name in self.content


class PrintableFile:
    def __init__(self, path):
        self.path = path
        self.name = dir_name(path)

    def __str__(self):
        return str(self.path)


path_to_folder1 = r'C:\Тимофей\#Программирование\test'
path_to_folder2 = r'C:\Тимофей\#Программирование\test\test1'
path_to_file1 = r'C:\Тимофей\#Программирование\test\text.txt'
path_to_file2 = r'C:\Тимофей\#Программирование\test\test2\text2.txt'
path_to_file3 = r'C:\never_land'

folder1 = PrintableFolder(path_to_folder1)
folder2 = PrintableFolder(path_to_folder2)

file1 = PrintableFile(path_to_file1)
file2 = PrintableFile(path_to_file2)
file3 = PrintableFile(path_to_file3)

print(folder1)
print(folder2)

print(folder2 in folder1)
print(file1 in folder1)
print(file2 in folder1)
print(file3 in folder1)

