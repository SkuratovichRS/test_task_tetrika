import csv
from collections import defaultdict

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


class WikiParser:
    def __init__(self, base_url: str):
        self._options = ChromeOptions()
        self._options.add_argument("--headless")
        self._options.add_argument("--incognito")
        self._driver = webdriver.Chrome(options=self._options)
        self._base_url = base_url
        self._result = defaultdict(int)

    def collect_data(self) -> dict:
        self._driver.get(self._base_url)
        while True:
            if not self._count_for_page():
                break
            next_page_button = self._driver.find_element(by=By.LINK_TEXT, value="Следующая страница")
            next_page_button.click()
        return self._result

    @staticmethod
    def is_russian_letter(letter: str) -> bool:
        return ord(letter) < 65 or ord(letter) > 90

    def _count_for_page(self) -> bool:
        category_els = self._driver.find_elements(by=By.CLASS_NAME, value="mw-category-group")
        for category_el in category_els:
            letter = category_el.find_element(by=By.TAG_NAME, value="h3").text
            if not self.is_russian_letter(letter):
                return False
            animals_els = category_el.find_elements(by=By.TAG_NAME, value="li")
            self._result[letter] += len(animals_els)
        return True


def main(parser: WikiParser) -> None:
    data = parser.collect_data()
    sorted_data = sorted(data.items(), key=lambda x: x[0])
    with open("task_2/beasts.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        for letter, count in sorted_data:
            writer.writerow([letter, count])


if __name__ == "__main__":
    main(WikiParser("https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"))
