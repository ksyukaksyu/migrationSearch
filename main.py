import os

current_dir = os.path.dirname(os.path.abspath(__file__))
migrations_dir = 'files'
migrations_path = os.path.join(current_dir, migrations_dir)
files_list = []


def search_in_files(search, files):
    result_list = []
    for file in files:
        with open(file) as file_data:
            if search in file_data.read():
                result_list.append(file)
    return result_list


if __name__ == '__main__':
    while True:
        input_str = input('Введите подстроку для поиска: ').lower()
        if len(files_list) == 0:
            for file in os.listdir(migrations_path):
                if file.endswith('.sql'):
                    files_list.append(os.path.join(migrations_path, file))

        files_list = search_in_files(input_str, files_list)
        for file in files_list:
            print(file)
        print('Всего: {}'.format(len(files_list)))
