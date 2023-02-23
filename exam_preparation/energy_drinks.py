from collections import deque

milligrams_of_caffeine = deque([int(x) for x in input().split(', ')])
energy_drinks = deque([int(x) for x in input().split(', ')])

MAX_CAFFEINE = 300
total_caffeine = 0

while energy_drinks:

    if not milligrams_of_caffeine:
        print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
        break

    current_caffeine = milligrams_of_caffeine.pop()
    current_drink = energy_drinks.popleft()
    caffeine = current_caffeine * current_drink

    if total_caffeine + caffeine <= MAX_CAFFEINE:
        total_caffeine += caffeine

    else:
        energy_drinks.append(current_drink)
        if total_caffeine >= 30:
            total_caffeine -= 30
        else:
            total_caffeine = 0

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
