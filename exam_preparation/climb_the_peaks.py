from collections import deque


def climb_the_peaks_func(food_portion, stamina):
    food_portion, stamina = deque(food_portion), deque(stamina)
    mountain_peaks_data = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100,'Polezhan': 60,'Kamenitza': 70,}
    conquered_peeks = []

    for peak, difficult in mountain_peaks_data.items():
        while True:
            daily_sum_of_elements = food_portion.pop() + stamina.popleft()

            if daily_sum_of_elements >= difficult:
                conquered_peeks.append(peak)
                break
            elif (len(food_portion) == 0 or len(stamina) == 0) and len(conquered_peeks) == 0:
                return "Alex failed! He has to organize his journey better next time -> @PIRINWINS"

    data_representation = '\n'.join(conquered_peeks)
    return f'Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK\nConquered peaks:\n{data_representation}'


food = list(map(int, input().split(', ')))
stamina = list(map(int, input().split(', ')))
print(climb_the_peaks_func(food, stamina))
