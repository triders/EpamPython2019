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
|\outer_1
|   |\inner_1_0
|   |   |*file_1_0.txt
|   |\inner_1_1
|   |   |*file_1_1.txt
|   |\inner_1_2
|   |   |*file_1_2.txt
|   |\inner_1_3
|   |   |*file_1_3.txt
|   |\inner_1_4
|   |   |*file_1_4.txt
"""
import os

def make_dirs(path, outer_num_of_dirs, inner_num_of_dirs):
    """makes dirs and files at given path""" 
    for i in range(outer_num_of_dirs):
        os.chdir(path)
        os.mkdir(f'outer_{str(i)}')
        ipath = path + "\\" + f'outer_{str(i)}'

        for j in range(inner_num_of_dirs):
            os.chdir(ipath)
            os.mkdir(f"inner_{str(i) + '_' + str(j)}")
            os.chdir(ipath + '\\' + f"inner_{str(i) + '_' + str(j)}")
            with open(f"file_{str(i) + '_' + str(j)}.txt", 'w') as file:
                pass


class PrintableFolder:

    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(self.path)
        self.content = []
        for root, _, files in os.walk(self.path):
            for file in files:
                self.content.append(PrintableFile(root+'\\'+file))

    def __str__(self):
        res = f'V\n'
        n = 0
        depth = -1
        for root, dirs, files in os.walk(self.path):
            sep = '|   '
            prefix = n * sep
            res += prefix + '|\\' + os.path.basename(root) + '\n'

            if dirs:
                n += 1
                depth += 1

            if files:
                n += 1
                prefix = n * sep
                for file in files:
                    res += prefix + '|*' + file + '\n'
                n -= 1

            if not dirs:
                n -= depth

        return res

    def __contains__(self, item):
        for i in self.content:
            if item == i:
                return True
        return False


class PrintableFile:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)

    def __eq__(self, other):
        return self.path == other.path and self.name == other.name

    def __str__(self):
        return f'name of file: "{self.name}", path: {self.path}'


# Make dirs and files to test


path = r"D:\Тимофей\Программирование\EpamPython2019-triders 06.01.2020\06-advanced-python\hw"

make_dirs(path, 4, 5)


# test


path_to_folder_0 = path + '\\outer_0'
path_to_folder_1 = path + '\\outer_1'
path_to_folder_1_1 = path + '\\outer_1\\inner_1_1'
path_to_file_1_1 = path + '\\outer_1\\inner_1_1\\file_1_1.txt'
path_to_file_no_file = r'C:\never_land'

folder_0 = PrintableFolder(path_to_folder_0)
folder_1 = PrintableFolder(path_to_folder_1)
folder_1_1 = PrintableFolder(path_to_folder_1)

file_1_1 = PrintableFile(path_to_file_1_1)

print(folder_0)
print(folder_1)

print(file_1_1)

print(file_1_1 in folder_1_1)
print(file_1_1 in folder_1)
print(file_1_1 in folder_0)
