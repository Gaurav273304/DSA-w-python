'''
Time Complexity: O(n) — The function processes each element in the list once (half the list is swapped).
Space Complexity: O(n) — The recursive call stack grows linearly with 
n, making the space complexity O(n) for large inputs.
'''

def reverse(lst,start,end):
    if start > end:
        return
    lst[start] , lst[end] = lst[end] ,lst[start]
    reverse(lst,start+1,end-1)

if __name__ == "__main__":
    my_list = [1,3,4,6,7,9]
    reverse(my_list,0,len(my_list)-1)
    print(my_list)
