from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
        format_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print(f"Помилка: Неправильний формат дати '{date}'. Очікується 'PPPP-MM-ДД'")
        return None

    # Отримання поточної дати без врахування часу!
    current_date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    time_difference = current_date - format_date
    return time_difference.days


if __name__ == "__main__":
    """Перевірка з поточною датою"""
    print(f"Поточна дата: {datetime.today().strftime('%Y-%m-%d')}")

    date1 = "2021-10-09"
    days1 = get_days_from_today(date1)
    if days1 is not None:
        print(f"Кількість днів від {date1} до сьогодні: {days1}")

    date2 = "2025-06-15"
    days2 = get_days_from_today(date2)
    if days2 is not None:
        print(f"Кількість днів від {date2} до сьогодні: {days2}")

    date3 = "2025-06-10"
    days3 = get_days_from_today(date3)
    if days3 is not None:
        print(f"Кількість днів від {date3} до сьогодні: {days3}")

    date4 = "2025-06-12"
    days4 = get_days_from_today(date4)
    if days4 is not None:
        print(f"Кількість днів від {date4} до сьогодні: {days4}")

    date5 = "2024-01-01"
    days5 = get_days_from_today(date5)
    if days5 is not None:
        print(f"Кількість днів від {date5} до сьогодні: {days5}")

"""Перевірка та обробка винятків!"""
date_invalid = "2023/12/31"
get_days_from_today(date_invalid)

date_another_invalid = "abc-def-ghi"
get_days_from_today(date_another_invalid)
