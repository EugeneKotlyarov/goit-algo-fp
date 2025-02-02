def greedy_algo(items, budget):
    # Змінні для зберігання обраних страв, вартості та калорій
    selected_items = []
    total_cost = 0
    total_calories = 0

    # Сортуємо страви за співвідношенням калорій до вартості у спадаючому порядку
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    # Обираємо страви, поки не вичерпаємо бюджет
    for item_name, item_specifics in sorted_items:
        if total_cost + item_specifics["cost"] <= budget:
            selected_items.append(item_name)
            total_cost += item_specifics["cost"]
            total_calories += item_specifics["calories"]

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def dynp_algo(items, budget):
    # Ініціалізація масивів для динамічного програмування
    num_items = len(items)
    dp_table = [[0] * (budget + 1) for _ in range(num_items + 1)]

    # Заповнення масиву варіантів
    for i in range(1, num_items + 1):
        for j in range(budget + 1):
            current_item = items[list(items.keys())[i - 1]]

            if current_item["cost"] > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = max(
                    dp_table[i - 1][j],
                    dp_table[i - 1][j - current_item["cost"]]
                    + current_item["calories"],
                )

    selected_items = []
    i, j = num_items, budget

    # Відновлення обраних страв
    while i > 0 and j > 0:
        if dp_table[i][j] != dp_table[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]
        i -= 1

    selected_items.reverse()
    total_cost = sum(items[item]["cost"] for item in selected_items)
    total_calories = sum(items[item]["calories"] for item in selected_items)

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 100

    greedy_result = greedy_algo(items, budget)
    dynamic_result = dynp_algo(items, budget)

    print("Жадібний алгоритм:")
    print(f"Порядок обирання страв: {greedy_result["selected_items"]}")
    print(f"Витратили бюджет: {greedy_result["total_cost"]} зі 100")
    print(f"Отримали калорій: {greedy_result["total_calories"]}")
    print()
    print("Динамічное програмування:")
    print(f"Порядок обирання страв: {dynamic_result["selected_items"]}")
    print(f"Витратили бюджет: {dynamic_result["total_cost"]} зі 100")
    print(f"Отримали калорій: {dynamic_result["total_calories"]}")


if __name__ == "__main__":
    main()
