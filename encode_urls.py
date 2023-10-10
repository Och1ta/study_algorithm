import string
import random
# Реализуйте класс MarsURLEncoder.
# В конструкторе класса __init__(...) создайте атрибут — хранилище ссылок.
# В классе должно быть два метода:
# метод encode() должен получать на вход длинные ссылки и возвращать короткие;
# метод decode() должен принимать короткую ссылку и возвращать исходную, длинную.


class MarsURLEncoder:

    def __init__(self):
        self.storage_url = {}

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        letters = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters, 6))
        short_url = 'https://ma.rs/' + rand_string
        self.storage_url[short_url] = long_url
        return short_url

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        if short_url in self.storage_url:
            return self.storage_url[short_url]
        else:
            return "Короткая ссылка уже находится в базе"
