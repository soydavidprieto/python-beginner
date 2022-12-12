if __name__ == '__main__':
    import re

    def is_not_empty(s):
        return bool(s and s.strip())

    def reformator(listik):
        list = []
        for item in listik:
            if item.isdigit():
                list.append((int(item), type(int(item))))
            elif item.strip().replace('.', '').isdigit():
                list.append((float(item), type(float(item))))
            elif item.lower() == "none":
                list.append((None, type(None)))
            elif item.lower() == "true":
                list.append((True, type(True)))
            elif item.lower() == "false":
                list.append((False, type(False)))
            else:
                list.append((item.replace(' ', ''), type(item)))
        return list


    input_string = input('Enter string:')
    output_list = []
    tuple_pattern = r"\([^)]*\)"
    match = re.search(tuple_pattern, input_string)
    if match:
        output_list.append((match.group(), type(tuple(match.group()))))
        list_without_tuple = list(filter(is_not_empty, input_string.replace(match.group(), '').split(', ')))
        print(reformator(list_without_tuple) + output_list)
    else:
        print(reformator(input_string.split(', ')))
