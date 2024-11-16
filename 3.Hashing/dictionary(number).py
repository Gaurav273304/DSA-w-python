arr1 = [1,3,2,4,455,65,2,4,6,8,99]
hash_map = {}

for num in arr1:
    hash_map[num] = hash_map.get(num,0) + 1

number = int(input("Enter the number to count = "))
print(hash_map.get(number,0))