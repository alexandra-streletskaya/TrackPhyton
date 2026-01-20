weight_1_book_b = 4 * 25 * 50 * 100
Mb_to_b = 1.44 * 1024 * 1024
numb_of_books = Mb_to_b // weight_1_book_b
numb_of_books = int(numb_of_books)
print("Количество книг, помещающихся на дискету:", numb_of_books)
