input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]                   
#output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]


def convert(lst):
    return [[[[int(n) for n in item.strip("()").split(",")]for item in inner]for inner in outer]for outer in lst]
print(convert(input))
