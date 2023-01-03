if __name__ == '__main__':
    #x = '1, sss, none, false, True, None, False,        qqq      ,  2.0, (ssss, 1)'
    #out_put = [(1, <class 'int'>), ('sss', <class 'str'>), (None, <class 'NoneType'>), (False, <class 'bool'>), (True,  <class 'bool'>), (None, <class 'NoneType'>), (False, <class 'bool'>), ('qqq', <class 'str'>), (2.0, <class 'float'>), (('ssss', 1), <class 'tuple'>)]
    x = input('Input any number or string, or True, or None or tuple. Separated by comma:')
    def get_type(item):
        try:
            return int(item), int
        except:
            try:
                return float(item), float
            except:
                if item == 'false' or item == 'true':
                    return item, bool
                elif item == 'True' or item == 'False':
                    return item, bool
                if item == 'none' or item == 'None':
                    return item, None
                elif item.startswith('(') and item.endswith(')'):
                    return item, tuple
                else:
                    return str(item), str

    array = [item.strip() for item in x.split(',')]
    final_array = []
    should_skip_index = False
    for item in array:
        if should_skip_index:
            should_skip_index = False
            continue
        if item.startswith('('):
            index = array.index(item)
            updated_index = index + 1
            finishing_element_of_tuple = array[updated_index]
            real_tuple = f'{item}, {finishing_element_of_tuple}'
            final_array.append(get_type(real_tuple))
            should_skip_index = True
            continue

        final_array.append(get_type(item))

    print('This is the the list with a values of certain type:' , final_array)