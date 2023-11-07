def taxi_sort(N, distances, tariffs):
    sorted_taxis = sorted(range(N), key=lambda x: tariffs[x])
    total_cost = 0
    for i in range(N):
        total_cost += distances[i] * tariffs[sorted_taxis[i]]
    return sorted_taxis, total_cost

N = int(input("Введите количество сотрудников компании: "))
distances = list(map(int, input("Введите расстояния от работы до домов: ").split()))
tariffs = list(map(int, input("Введите тарифы за проезд одного километра в такси: ").split()))

sorted_taxis, total_cost = taxi_sort(N, distances, tariffs)

print("Номера такси для сотрудников:", sorted_taxis)
print("Сумма в рублях:", total_cost)

# Функция для преобразования числа в слово
def num2word(n, words):
    if n % 100 in (11, 12, 13, 14):
        return words[2]
    if n % 10 == 1:
        return words[0]
    if n % 10 in (2, 3, 4):
        return words[1]
    return words[2]

# Вывод суммы прописью
rubles_words = ["рубль", "рубля", "рублей"]
print("Сумма словами:", total_cost, num2word(total_cost, rubles_words))
