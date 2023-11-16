import read
import save
data_name = input(f'Введите имя файла, который вы хотите отсортировать и сохранить ')
data = read.read_file(data_name)
save_name = input(f'Введите имя файла, в который вы хотите сохранить данные ')
print(f'{save.save_file(save_name, data)}')