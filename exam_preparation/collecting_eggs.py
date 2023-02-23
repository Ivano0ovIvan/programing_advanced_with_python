from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
papers = deque([int(x) for x in input().split(', ')])
BOX_SIZE = 50
count_of_filled_boxes = 0
fill_box_condition = False

while eggs:

    if not papers:
        break

    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue

    elif current_egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue
    current_paper = papers.pop()

    if current_egg + current_paper <= BOX_SIZE:
        count_of_filled_boxes += 1
        fill_box_condition = True

if fill_box_condition:
    print(f"Great! You filled {count_of_filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join(map(str, eggs))}')
if papers:
    print(f"Pieces of paper left: {', '.join(map(str, papers))}")