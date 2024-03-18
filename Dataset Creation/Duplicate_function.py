def duplicate(my_list, K):
    list_new = my_list
    if len(list_new) > K:
        print('The list exceeds the limit')
        return list_new
    while len(list_new) < K:
        list_new = list_new + list_new[::-1]
    list_new = list_new[0:K]
    return list_new