morning = {
    "Java", "C", "Ruby", "Lisp", "C#"
}

evening = {
    "Python", "C#", "Java", "C", "Ruby"
}

possible_courses = morning ^ evening
print(possible_courses)

possible_courses = morning.symmetric_difference(evening)
print(possible_courses)

possible_courses = evening.symmetric_difference(morning)
print(possible_courses)
