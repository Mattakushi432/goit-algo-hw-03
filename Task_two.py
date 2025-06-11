import random

def get_numbers_ticket(max_num: int, min_num: int, quantity: int) -> list[int]:
    if not (1 <= min_num <= max_num <= 1000 and  0 < quantity <= (max_num - min_num + 1)):
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_num, max_num))

    return sorted(list(numbers))

lottery_ticket = get_numbers_ticket(50, 10, 5)
print(f"Ваші лотерейні номери (50, 10, 5 чисел): {lottery_ticket}")
