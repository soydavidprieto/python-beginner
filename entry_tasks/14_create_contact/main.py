if __name__ == "__main__":
    users = []
    num = int(input("Enter total number of contacts to add: "))
    for i in range(1, num + 1):
        user_data = {}
        user_data['name'] = input("Enter your name: ")
        user_data['age'] = int(input("Enter your age: "))
        user_data['address'] = input("Enter your address: ")
        user_data['phone'] = input("Enter your phone: ")
        print('>>> Contact created: ', f'{user_data}')
        users.append(user_data)
    print('Your contact book: ')
    for i in range(len(users)):
        print(f'{i + 1}. {users[i]["name"]}: {users[i]["phone"]}')
