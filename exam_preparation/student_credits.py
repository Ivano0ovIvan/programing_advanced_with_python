def students_credits(*data):
    courses_dict = {}
    total_student_points = 0
    points_for_diploma = 240
    for current_data in data:
        course_name, *points = current_data.split('-')
        courses_dict[course_name] = points

    for course, points in courses_dict.items():
        credits = int(courses_dict[course][0])
        max_test_points = int(courses_dict[course][1])
        current_student_points = int(courses_dict[course][2])
        current_credits = credits * (current_student_points / max_test_points)
        total_student_points += float(f'{current_credits:.1f}')
        courses_dict[course].clear()
        courses_dict[course] = float(f'{current_credits:.1f}')

    output = []
    if total_student_points >= points_for_diploma:
        output.append(f"Diyan gets a diploma with {total_student_points} credits.")
    else:
        output.append(f"Diyan needs {points_for_diploma - total_student_points} credits more for a diploma.")
    for course, points in sorted(courses_dict.items(), key=lambda k: -k[1]):

        output.append(f'{course} - {points:.1f}')

    return '\n'.join(output)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)




