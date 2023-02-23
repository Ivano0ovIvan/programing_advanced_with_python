from collections import deque

textiles = deque([int(x) for x in input().split(' ')])
medicaments = deque([int(x) for x in input().split(' ')])

healing_items = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100,
}
created_items = {}

while textiles and medicaments:

    current_difference = 0
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    sum_of_current_elements = current_textile + current_medicament
    for k, v in healing_items.items():
        if sum_of_current_elements == v:
            if k not in created_items.keys():
                created_items[k] = 0
            created_items[k] += 1
            break
    else:
        if sum_of_current_elements > healing_items['MedKit']:
            if 'MedKit' not in created_items.keys():
                created_items['MedKit'] = 0
            created_items['MedKit'] += 1
            current_difference = sum_of_current_elements - healing_items['MedKit']
            current_medicament = medicaments.pop()
            current_medicament += current_difference
            medicaments.append(current_medicament)
        else:
            current_medicament += 10
            medicaments.append(current_medicament)


if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

if created_items:
    sorted_created_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))

    for item in sorted_created_items:
        print(f"{item[0]} - {item[1]}")

if medicaments:
    medicaments.reverse()
    sorted_medicaments = [str(x) for x in medicaments]
    print(f"Medicaments left: {', '.join(sorted_medicaments)}")

elif textiles:
    sorted_textiles = [str(x) for x in textiles]
    print(f"Textiles left: {', '.join(sorted_textiles)}")