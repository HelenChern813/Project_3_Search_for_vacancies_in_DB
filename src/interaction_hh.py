from typing import Any

import requests


class HeadHunterAPI:
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        self._url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self._params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def hh_employers(self) -> list[dict[str, Any]]:
        """Метод для получения компаний, отсортированных по количеству открытых вакансий"""

        self._url = "https://api.hh.ru/employers"
        self._params = {
            "sort_by": "by_vacancies_open",
            "per_page": 10
        }
        response = requests.get(self._url, self._params)
        if response.status_code != 200:
            raise requests.RequestException
        return response.json()["items"]

    def hh_vacancies(self, employer_id: int) -> list[dict[str, Any]]:
        """Метод для получения списка вакансий"""

        self._url = "https://api.hh.ru/vacancies"
        self._params = {
            "employer_id": employer_id,
            "per_page": 50
        }
        response = requests.get(self._url, self._params)
        if response.status_code != 200:
            raise requests.RequestException
        return response.json()["items"]
