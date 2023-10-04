# given two dimensional array
array = [['January', 'February', 'March', 'April'], ['May', 'June', 'July', 'August'], ['September', 'October', 'November', 'December']]

# double loop to loop into array inside other array & print month names
# for trimester in array:
#     for month in trimester:
#         print(month)

i = 0
j = 0
while i < len(array):
    trimester = array[i]
    while j < len(trimester):
        print(trimester[j])
        j += 1
    i += 1
    j = 0