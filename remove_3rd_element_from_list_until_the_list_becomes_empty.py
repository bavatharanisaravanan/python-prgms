def remove_nums(int_list):
    pos=3-1
    idx=0
    len_list=(len(int_list))
    while len_list>0:
        idx=(pos+idx)%len_list
        print(int_list.pop(idx))
        len_list=len_list-1
print("the list is empty")   
nums=[1,2,3,4,5,6,7,8,9]
remove_nums=(nums)
