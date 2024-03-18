import numpy as np
import math


def uniform_Sampling(my_list, final_length):
    if len(my_list) > final_length:
        step = math.floor(len(my_list)/final_length)
        return my_list[0:step*final_length:step]
    else:
        return my_list