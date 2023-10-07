def calculate_bmi(weight, height_cm):
    try:
        weight = float(weight)
        height = float(height_cm) / 100

        if height == 0:
            raise ZeroDivisionError

        bmi = weight / (height ** 2)
        return bmi
    except ValueError:
        return None
    except ZeroDivisionError:
        return None


def main():
    try:
        weight = float(input("Введите вес (кг): "))
        height_cm = float(input("Введите рост (см): "))

        if weight <= 0 or height_cm <= 0:
            raise ValueError

        bmi = calculate_bmi(weight, height_cm)

        if bmi is not None:
            print(f"Индекс массы тела (BMI): {bmi:.2f}")
        else:
            print("Ошибка: введены некорректные данные!")
    except ValueError:
        print("Ошибка: введены некорректные данные!")


if __name__ == "__main__":
    main()
