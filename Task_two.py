import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if not (1 <= min <= max <= 1000 and 0 < quantity <= (max - min + 1)):
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(list(numbers))


lottery_ticket = get_numbers_ticket(10, 50, 5)
print(f"Ваші лотерейні номери (10, 50, 5 чисел): {lottery_ticket}")

lottery_ticket_test = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні номери (1, 49, 6 чисел): {lottery_ticket_test}")