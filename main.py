import requests


from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        url = self.get_link(file_path).get('href', '')
        response = requests.put(url, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('201! Success!')


    def get_link(self, file_path: str):
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = {'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'file.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)