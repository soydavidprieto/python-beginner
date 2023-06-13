if __name__ == '__main__':
    print('Task 7. String slice')

s = input("Enter a string: ")
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

substring = s[start:end]
print("The substring is:", substring)

