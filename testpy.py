lst = [4, 4, 5, 2, 7, 10, 9]

a = 9


def search(lst, a):

  for i, val in enumerate(lst):
    copy_list = lst.copy()
    # Копируем список и удалим текущее значение, 
    # так как есть вероятность, что такое же значение есть ещё в списке, 
    # напирмер, в нашем случае есть две четвёрки
    del copy_list[i]
    
    b = a - val
    if b in copy_list:
      return True

    return False

search(lst, a)
