def taxi_sort(N, distances, tariffs):
    sorted_taxis = sorted(range(N), key=lambda x: tariffs[x])
    total_cost = 0
    for i in range(N):
        total_cost += distances[i] * tariffs[sorted_taxis[i]]
    return sorted_taxis, total_cost

def num2word(n, words):
    if n % 100 in (11, 12, 13, 14):
        return words[2]
    if n % 10 == 1:
        return words[0]
    if n % 10 in (2, 3, 4):
        return words[1]
    return words[2]

def main():
    try:
        N = int(input("Введите количество сотрудников компании: "))
        if N <= 0:
            print("Количество сотрудников должно быть больше нуля")
            return

        distances = list(map(int, input("Введите расстояния от работы до домов: ").split()))
        if len(distances) != N:
            print("Количество расстояний должно соответствовать количеству сотрудников")
            return

        tariffs = list(map(int, input("Введите тарифы за проезд одного километра в такси: ").split()))
        if len(tariffs) != N:
            print("Количество тарифов должно соответствовать количеству сотрудников")
            return

        sorted_taxis, total_cost = taxi_sort(N, distances, tariffs)

        print("Номера такси для сотрудников:", sorted_taxis)
        print("Сумма в рублях:", total_cost)

        rubles_words = ["рубль", "рубля", "рублей"]
        print("Сумма словами:", total_cost, num2word(total_cost, rubles_words))
    except ValueError:
        print("Ошибка ввода. Введите целые числа.")

if __name__ == "__main__":
    main()
