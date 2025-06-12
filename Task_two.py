import random


def get_numbers_ticket(max: int, min: int, quantity: int) -> list[int]:
    if not (1 <= min <= max <= 1000 and 0 < quantity <= (max - min + 1)):
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(list(numbers))


lottery_ticket = get_numbers_ticket(50, 10, 5)
print(f"Ваші лотерейні номери (50, 10, 5 чисел): {lottery_ticket}")
