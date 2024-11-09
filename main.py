import re
import unittest

# Регулярное выражение для проверки HEX-цвета
Regular = r'^#(?:[0-9A-F]{6}|[0-9A-F]{3})$'


class Test(unittest.TestCase):

    def setUp(self):
        self.Regular = Regular

    def test_valid_colors(self):
        colors = [
            "#ECECA7", "#A0A037", "#FAFAB3", "#E3E3DE",
            "#D22898", "#C4B6DD", "#71EFFF", "#75EF71"
        ]
        for color in colors:
            self.assertTrue(re.match(self.Regular, color))

    def test_invalid_colors(self):
        inv_colors = [
            "#000G00", "#FFGGFF", "#00ABCD0", "#FFFFFFF",
            "#ABCDR", "#ABCD", "#123456789ABCDEF"
        ]
        for color in inv_colors:
            self.assertFalse(re.match(self.Regular, color))

    def test_case(self):
        edge_cases = [
            "#AB99CD", "#FFB", "#ADC", "#RFFFFF"
        ]
        for case in edge_cases:
            self.assertTrue(re.match(self.Regular, case), f"Неверный HEX-цвет: {case}")


def work_with_file(content):
    pattern = r'#\S+'

    print("Содержимое файла:")
    print(content)

    hex_colors = re.findall(pattern, content)
    print(f"\nНайдены HEX-коды: {hex_colors}\n")

    for color in hex_colors:
        if re.search(Regular, color):
            print(f"\nКорректный код: {color} +++++++++")
        else:
            print(f"\nКекорректный код: {color} ---------")

    return True


file_path = 'Test.txt'
try:
    with open(file_path, 'r') as file:
        content = file.read()

    work_with_file(content)
except FileNotFoundError:
    print(f"Ошибка: Файл '{file_path}' не найден.")
    print("Обработка файла завершена с ошибкой.")
except Exception as e:
    print(f"Произошла ошибка при чтении файла: {str(e)}")
    print("Обработка файла завершена с ошибкой.")
