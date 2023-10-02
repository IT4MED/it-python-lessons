def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        bmi = weight / (height ** 2)
        if (bmi<1):
            return None
        return bmi
        print('sas')
    except ValueError:
        return None
    except ZeroDivisionError:
        return None

def main():
    weight = input("Введите вес (кг): ")
    height = input("Введите рост (м): ")

    bmi = calculate_bmi(weight, height)

    if bmi is not None:
        print(f"Индекс массы тела (BMI): {bmi:.2f}")
    else:
        print("Ошибка: введены некорректные данные!")

if __name__ == "__main__":
    main()
