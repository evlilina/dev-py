users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
amount_of_visits = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
amount_of_visits["Общее количество"] = len(users)
amount_of_visits["Уникальные посещения"] = len(set(users))
print(amount_of_visits)





