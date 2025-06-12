import re


def normalize_phone(phone_number: str) -> str:
    sanitized_number = re.sub(r'[^\d+]', '', phone_number)
    if sanitized_number.startswith('380') and not sanitized_number.startswith('+'):
        sanitized_number = '380' + sanitized_number

    return sanitized_number

raw_numbers = [
        "067\t123 4567",
    ]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)