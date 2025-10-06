from src.configuration import config
from src.dbmanager import DBManager
from src.create_db import create_database, create_tables, filling_tables


def main() -> None:
    """Функция для взаимодействия с пользователем"""

    db_name = "hh_vacancies"
    params = config()

    while True:
        print("\nВыберите действие:")
        print("1. Создать базу данных и таблицы")
        print("2. Заполнить таблицы данными")
        print("3. Получить список всех компаний и количество вакансий у каждой компании")
        print("4. Получить среднюю зарплату по вакансиям")
        print("5. Получить список всех вакансий, в названии которых содержатся переданные в метод слова")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            create_database(db_name, params)
            create_tables(db_name, params)
            print("База данных и таблицы созданы.")

        elif choice == "2":
            filling_tables(db_name, params)
            print("Данные добавлены в таблицы.")

        elif choice == "3":
            db_manager = DBManager(db_name, params)
            companies_and_vacancies = db_manager.get_companies_and_vacancies_count()
            for company in companies_and_vacancies:
                print(f"Компания: {company['employer_name']}, Количество вакансий: {company['vacancies_count']}")

        elif choice == "4":
            db_manager = DBManager(db_name, params)
            avg_salary = db_manager.get_avg_salary()
            print(f"Средняя зарплата по вакансиям: {avg_salary}")

        elif choice == "5":
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            db_manager = DBManager(db_name, params)
            keyword_vacancies = db_manager.get_vacancies_with_keyword(keyword)
            for vacancy in keyword_vacancies:
                print(f"Компания: {vacancy['employer_name']}, Вакансия: {vacancy['vacancy_name']}, Зарплата от: {vacancy['salary_from']}, Зарплата до: {vacancy['salary_to']}, Ссылка: {vacancy['vacancy_url']}")

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 6.")


if __name__ == "__main__":
    main()
