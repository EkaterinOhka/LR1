users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

stat_logs = {
    "Общее количество": 0,
    "Униальные посещения": 0
}
stat_logs["Общее количество"] = len(users)
stat_logs["Униальные посещения"] = len(set(users))

print(stat_logs)
