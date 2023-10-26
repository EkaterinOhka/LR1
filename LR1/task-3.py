# TODO Найдите количество книг, которое можно разместить на дискете

information_volum = 1.44 * 1024 * 1024
number_of_pages = 100
number_of_strings = 50
number_of_symbols = 25
volume_of_symbol = 4

volume_of_book = number_of_symbols * number_of_strings * number_of_pages * volume_of_symbol
number_of_books = round(information_volum / volume_of_book)

print("Количество книг, помещающихся на дискету:", number_of_books)
