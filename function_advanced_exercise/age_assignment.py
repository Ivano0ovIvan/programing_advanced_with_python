def age_assignment(*names, **ages):
    result = []

    for letter, age in ages.items():
        person_name = ''

        for name in names:
            if name.startswith(letter):
                person_name = name
                break
        result.append(f"{person_name} is {age} years old.")
    return '\n'.join(sorted(result))


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))