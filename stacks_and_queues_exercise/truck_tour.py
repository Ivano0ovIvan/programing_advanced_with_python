from _collections import deque
petrol_pumps = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
petrol_pumps_data_copy = petrol_pumps.copy()
index = 0
gas_left = 0

while petrol_pumps_data_copy:
    petrol, distance = petrol_pumps_data_copy.popleft()
    gas_left += petrol
    if gas_left - distance < 0:
        petrol_pumps.rotate(-1)
        petrol_pumps_data_copy = petrol_pumps.copy()
        index += 1
        gas_left = 0
    else:
        gas_left -= distance
print(index)
