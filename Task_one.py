from datetime import datetime

def get_days_from_today(date: str, date_format: str = "%Y-%m-%d") -> int:
    input_date = datetime.strptime(date, date_format).date()
    current_date = datetime.today().date()
    delta_days = abs((current_date - input_date).days)
    return delta_days
print(get_days_from_today("2026-06-11"))