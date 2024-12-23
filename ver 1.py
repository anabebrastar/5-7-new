import random
import string

def generate_random_text(length=100):
    words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 7))) for _ in range(length)]
    return ' '.join(words)

def reverse_words(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return reversed_words

def main():
    text = None
    result = None

    while True:
        print("\nМеню:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            print("Выберите способ ввода данных:")
            print("1. Ввести данные вручную")
            print("2. Сгенерировать данные случайным образом")
            input_choice = input("Выберите способ ввода: ")
            if input_choice == '1':
                text = input("Введите текст: ")
            elif input_choice == '2':
                text = generate_random_text()
                print("Сгенерированный текст:", text)
            else:
                print("Неверный выбор. Попробуйте снова.")

            result = None  # Сбрасываем результат при вводе новых данных

        elif choice == '2':
            if text is None:
                print("Сначала введите исходные данные.")
            else:
                result = reverse_words(text)
                print("Алгоритм выполнен.")

        elif choice == '3':
            print("Вывод результата (пока не реализовано)")

        elif choice == '4':
            print("Завершение работы программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()


