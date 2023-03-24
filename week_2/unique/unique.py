if __name__ == '__main__':
    print('Task 15. Unique.')
    sequence_of_numbers = [1, 2, 11, 1, 2, 2, 3]

    #unique_list = []
   # for x in y:
      #  if x not in unique_list:
     #      unique_list.append(x)

    #for x in unique_list:
    #   print(x)
    unique_numbers = set(sequence_of_numbers)
    unique_list = list(unique_numbers)
    print(sorted(unique_list))




