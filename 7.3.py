course_rooms = {
    1: 'Кабинет 201',
    2: 'Кабинет 302',
    3: 'Кабинет 403',
    4: 'Кабинет 504',
}

course_times = {
    1: '9:00 - 10:30',
    2: '10:30 - 12:00',
    3: '13:00 - 14:30',
    4: '14:30 - 16:00',
}

course_number = int(input("Введите номер курса: "))

if course_number in course_rooms and course_number in course_times:
    print("Аудитория:", course_rooms[course_number])
    print("Время:", course_times[course_number])
else:
    print("Курс с таким номером не существует.")
