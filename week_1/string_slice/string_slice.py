if __name__ == '__main__':
    print('Task 7. String slice')
    s = input('Type any string: ')
    start = input('Start symbol: ')
    end = input('End symbol: ')
    substring=s[int(start):int(end)]
    print("substring(from start to end) = ", substring)