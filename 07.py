import random


def simulate_dice_rolls(times):
    results = {}
    probabilities = {}

    for _ in range(times):
        sum = random.randint(1, 6) + random.randint(1, 6)

        if sum not in results:
            results[sum] = 1
        else:
            results[sum] += 1

    for k, v in results.items():
        probabilities[k] = v / times

    return probabilities


def main():
    # Кількість симуляцій
    times = 10000

    # Робимо симуляцію і одразу сортуємо
    probabilities = sorted(simulate_dice_rolls(times).items())

    # Реальна вирогідність
    p_real = {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78,
    }

    print(f"Сума\tP (M-C)\tP (реальна)")
    for sum, probability in probabilities:
        print(f"{sum}\t{probability * 100:.2f}\t{p_real[sum]:.2f}")


if __name__ == "__main__":
    main()
