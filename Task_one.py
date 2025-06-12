from datetime import datetime, date
from typing import Optional

"""
1. def get_days_from_today(date: str) -> int:
    он не взвращает инт он возвращает инт или нон
2. имя переменной date очень плохое. оно совпадает с популярной либой. И очень непонятно что ті хочешь сюда положить
3. Пиши докстринги (если хочешь правильное оформление)
4. Если есть желание написать комент лучше вынеси в отдельную функцию
5. if __name__ == "__main__": крутая штука но для тестов лучше использовать тесты :)
        например либа Pytest пример скинул
        
6. Не используй print для вывода ошибок. Лучше использовать создать и рейзить ексепшн( нот это для больших проектов)
    здесь можно просто подписать тот который вылетает. 
    Хотя завист от таски
"""
def get_days_from_today(date_str: str) -> Optional[int]:
    """Отримує кількість днів від вказаної дати до поточної дати.
    Args:
        date_str (str): Дата у форматі 'PPPP-MM-ДД'.
    Returns:
        Optional[int]: Кількість днів від вказаної дати до поточної дати, або None у випадку помилки.

    """
    try:
        format_date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError as e:
        # raise ValueError(f"Помилка: Неправильний формат дати '{date_str}'. Очікується 'PPPP-MM-ДД'") from e
        print(f"Помилка: Неправильний формат дати '{date_str}'. Очікується 'PPPP-MM-ДД'")
        return

    # Отримання поточної дати без врахування часу!
    current_date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) # Круто. Но есть более короткий способ
    # используй date вместо datetime
    today = date.today()
    input_date = format_date.date()  # Преобразование datetime в date
    # time_difference = current_date - format_date
    return (today - input_date).days


if __name__ == "__main__":
    """Перевірка з поточною датою"""
    print(f"Поточна дата: {datetime.today().strftime('%Y-%m-%d')}")

    date1 = "2021-10-09"
    days1 = get_days_from_today(date1)
    if days1 is not None:
        print(f"Кількість днів від {date1} до сьогодны: {days1}")

    date2 = "2025-06-15"
    days2 = get_days_from_today(date2)
    if days2 is not None:
        print(f"Кількість днів від {date2} до сьогодны: {days2}")

    date3 = "2025-06-10"
    days3 = get_days_from_today(date3)
    if days3 is not None:
        print(f"Кількість днів від {date3} до сьогодны: {days3}")

    date4 = "2025-06-12"
    days4 = get_days_from_today(date4)
    if days4 is not None:
        print(f"Кількість днів від {date4} до сьогодны: {days4}")

    date5 = "2024-01-01"
    days5 = get_days_from_today(date5)
    if days5 is not None:
        print(f"Кількість днів від {date5} до сьогодны: {days5}")

    """Перевірка та обробка винятків!"""
    date_invalid = "2023/12/31"
    get_days_from_today(date_invalid)

    date_another_invalid = "abc-def-ghi"
    get_days_from_today(date_another_invalid)
