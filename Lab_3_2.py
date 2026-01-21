def find_common_participants(participants_1, participants_2, separator=','):
    participants_list1 = participants_1.split(separator)
    participants_list2 = participants_2.split(separator)

    common_participants = list(set(participants_list1).intersection(participants_list2))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)