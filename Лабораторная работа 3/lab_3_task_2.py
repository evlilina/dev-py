# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, separator=","):
    participants_first_group = first_group.split(separator)
    participants_second_group = second_group.split(separator)

    common_participants = list(set(participants_first_group).intersection(participants_second_group))
    return sorted(common_participants)



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)
