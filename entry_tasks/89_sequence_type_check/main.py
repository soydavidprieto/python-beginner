def parse_value(string_value):
    if string_value.isdigit():
        return int(string_value.strip())
    elif string_value.strip().replace('.', '').isdigit():
        return float(string_value)
    elif string_value.strip().lower() == "false":
        return False
    elif string_value.strip().lower() == "true":
        return True
    elif string_value.strip().lower() == "none":
        return None
    elif string_value.isspace():
        return string_value.strip()
    elif string_value:
        if "(" in string_value and ")" in string_value:
            array_tuple = string_value.replace("(", "").replace(")", "").replace(" ", "").split(",")
            for idx, item in enumerate(array_tuple):
                array_tuple[idx] = parse_value(item)
            return tuple(array_tuple)
        else:
            return string_value.strip()
    else:
        raise ValueError("Enter correct type value!")


if __name__ == "__main__":
    lst = []
    a = input("Input some sequence values, separated by comma: ").strip()

    start_index = 0
    while start_index < len(a):
        comma_index = a.find(',', start_index)
        if comma_index == -1:
            value = a[start_index:]
        else:
            value = a[start_index:comma_index]
            start_tuple_index = value.find('(')
            if start_tuple_index != -1:
                end_tuple_index = a.find(')', start_index)
                value = a[start_index:end_tuple_index + 1]
        start_index = start_index + len(value) + 1
        value = value.strip()
        parsed_value = parse_value(value)
        lst.append((parsed_value, type(parsed_value)))
    print(lst)
