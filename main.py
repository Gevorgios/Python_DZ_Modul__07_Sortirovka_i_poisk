# def display_menu():
#     print("Меню:")
#     print("1. Отсортировать по идентификационным кодам")
#     print("2. Отсортировать по номерам телефона")
#     print("3. Вывести список пользователей с кодами и телефонами")
#     print("4. Выход")
#
# def sort_by_id_codes(id_codes, phone_numbers):
#     sorted_data = sorted(zip(id_codes, phone_numbers), key=lambda x: x[0])
#     return [list(t) for t in zip(*sorted_data)]
#
# def sort_by_phone_numbers(id_codes, phone_numbers):
#     sorted_data = sorted(zip(id_codes, phone_numbers), key=lambda x: x[1])
#     return [list(t) for t in zip(*sorted_data)]
#
# def display_users(id_codes, phone_numbers):
#     for i in range(len(id_codes)):
#         print(f"Идентификационный код: {id_codes}, Номер телефона: {phone_numbers[i]}")
#
# id_codes = [723, 456, 889]
# phone_numbers = [9585335, 985454, 9854854]
#
# while True:
#     display_menu()
#     choice = int(input("Выберите действие: "))
#
#     if choice == 1:
#         sorted_data = sort_by_id_codes(id_codes, phone_numbers)
#         print("Отсортировано по идентификационным кодам:")
#         display_users(sorted_data[0], sorted_data[1])
#     elif choice == 2:
#         sorted_data = sort_by_id_codes(id_codes, phone_numbers)
#         print("Отсортировано по номерам телефона:")
#         display_users(sorted_data[0], sorted_data[1])
#     elif choice == 3:
#         print("Список пользователей с кодами и телефонами:")
#         display_users(id_codes, phone_numbers)
#     elif choice == 4:
#         print("Выход")
#         break
#     else:
#         print("Некорректный выбор. Пожалуйста, выберите снова")


# 2


# def display_menu():
#     print("Меню:")
#     print("1. Отсортировать по названию книг")
#     print("2. Отсортировать по годам выпуска")
#     print("3. Вывести список книг с названиями и годами выпуска")
#     print("4. Выход")
#
# def sort_by_book_title(book_titles, release_years):
#     sorted_data = sorted(zip(book_titles, release_years), key=lambda x: x[0])
#     return [list(t) for t in zip(*sorted_data)]
#
# def sort_by_release_years(book_titles, release_years):
#     sorted_data = sorted(zip(book_titles, release_years), key=lambda x: x[1])
#     return [list(t) for t in zip(*sorted_data)]
#
# def display_books(book_titles, release_years):
#     for i in range(len(book_titles)):
#         print(f"Название книги: {book_titles[i]}, Год выпуска: {release_years[i]}")
#
# # Пример использования
# book_titles = ["Book A", "Book B", "Book C"]
# release_years = [2000, 2010, 2020]
#
# while True:
#     display_menu()
#     choice = int(input("Выберите действие: "))
#
#     if choice == 1:
#         sorted_data = sort_by_book_title(book_titles, release_years)
#         print("Отсортировано по названию книг:")
#         display_books(sorted_data[0], sorted_data[1])
#     elif choice == 2:
#         sorted_data = sort_by_release_years(book_titles, release_years)
#         print("Отсортировано по годам выпуска:")
#         display_books(sorted_data[0], sorted_data[1])
#     elif choice == 3:
#         print("Список книг с названиями и годами выпуска:")
#         display_books(book_titles, release_years)
#     elif choice == 4:
#         print("Выход.")
#         break
#     else:
#         print("Некорректный выбор. Пожалуйста, выберите снова.")