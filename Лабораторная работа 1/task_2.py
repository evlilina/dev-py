# TODO Найдите количество книг, которое можно разместить на дискете

book_bytes = 100 * 50 * 25
all_char_bytes = book_bytes * 4
disketa_volume = 1.44 * 1024 * 1024


print("Количество книг, помещающихся на дискету:", int(disketa_volume // all_char_bytes))
