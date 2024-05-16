import requests
from abc import ABC, abstractmethod


class APIVacanciesHH(ABC):
    """
    Абстрактный класс для работы с API.
    """

    @abstractmethod
    def getting_vacancies(self, keyword):
        pass


class HeadHunterRuAPI(APIVacanciesHH):
    """
    Получает вакансии по ключевому слову
    """

    def getting_vacancies(self, keyword):

        url = 'https://api.hh.ru/vacancies'
        params = {'text': keyword}
        response = requests.get(url, params=params)
        data = response.json()
        return data
