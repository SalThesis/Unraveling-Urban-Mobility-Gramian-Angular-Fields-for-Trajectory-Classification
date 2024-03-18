import numpy as np
import math


def ceil_list(my_list, final_length):
    if len(my_list) <= final_length:
        final_list = my_list
        return final_list 
    
    old_length = len(my_list)
    final_list = []
    seg_length = 1
    for index, value in enumerate(my_list):
        if index != len(my_list) - 1:
            if value == my_list[index + 1]:
                seg_length += 1
            else:
                final_list = final_list + [value] * math.ceil((seg_length * final_length / old_length))
                seg_length = 1
        else:
            final_list = final_list + [value] * math.ceil((seg_length * final_length / old_length))
            seg_length = 1
    return final_list

def index_and_length(my_list):
    
    list_start_index = []
    list_length = []
    seg_length = 1
    for index, value in enumerate(my_list):
        if index != len(my_list) - 1:
            if value == my_list[index + 1]:
                seg_length += 1
            else:
                list_start_index.append(index + 1 - seg_length)
                list_length.append(seg_length)
                seg_length = 1
        else:
            list_start_index.append(index + 1 - seg_length)
            list_length.append(seg_length)
            seg_length = 1
    return list_start_index, list_length, my_list

def squeeze(my_list, final_length):
    my_list = ceil_list(my_list, final_length)
    list_start_index, list_length, my_list = index_and_length(my_list)
    
    index = sorted(range(len(list_length)), key = lambda k: list_length[k], reverse = True)
    list_start_index = [list_start_index[i] for i in index]
    list_length = [list_length[i] for i in index]
    
    list_length_updated = list_length.copy()
    j = 0
    while( (np.isnan(np.array(my_list)).sum() < len(my_list) - final_length) and (len(my_list) > final_length)):
        if all(item == 1 for item in list_length_updated) == True:
            print('The list cannot be compressed')
            break
        else:
            if list_length_updated[j] > 1:
                removed_index = list_start_index[j]
                my_list[removed_index] = float('nan')
                list_start_index.append(list_start_index[j] + 1)
                list_length_updated.append(list_length_updated[j] - 1)
                list_start_index.pop(0)
                list_length_updated.pop(0)
            else:
                list_start_index.append(list_start_index[j])
                list_length_updated.append(list_length_updated[j])
                list_start_index.pop(0)
                list_length_updated.pop(0)
    my_list = list(filter(lambda x: not math.isnan(x), my_list))
    
    return my_list