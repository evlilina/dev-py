# TODO Напишите функцию для поиска индекса товара
def search_item(spisok, item):
    for index, current_item in enumerate(spisok):
        if current_item == item:
            return spisok.index(item)


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


for find_item in ['банан', 'груша', 'персик']:
   index_item = search_item(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
   if index_item is not None:
       print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
   else:
       print(f"Товар '{find_item}' не найден в списке.")

