def split_str_of_json_objects(s):
    """takes str of full json object and returns a list of objects"""
    # split by '{'
    lst = s.split('{')
    # cut by '}'
    for i in range(len(lst)):
        bracket_index = lst[i].rfind('}')
        lst[i] = lst[i][:bracket_index]
    # clear empty ''
    lst = list(filter(lambda x: len(str(x)) > 0, lst))
    return lst

# 1. split by ":"
# 2. split by last ","


def json_object_to_dict(j_str):
    """Splits string of 1 json object into dict.
    1. split by ':', except ':' in description
    2. then splits by last ','
    3. int(numbers)
    4. 'null'
    5. clear empty ''
    p.s. some descriptions remain in '"'
    """
    # split by ':' -- will get [1st key, ...,  value[i], key[i+1], ..., last value]
    lst = []
    lst.extend(j_str.split(':'))

    # now there are some descriptions separated because they also had MULTIPLE ':', fix this by:
    new_lst = []
    tmp = ''
    gather = False
    for item in lst:
        if item.count('"') % 2 == 0 and not gather:
            # "title", 'null', 87...
            new_lst.append(item)
        elif item.count('"') % 2 == 0 and gather:
            tmp += item
        elif item.count('"') % 2 == 1:
            if gather:
                tmp += item
                new_lst.append(tmp)
                tmp = ''
                gather = False
                continue
            tmp += item
            gather = True
        else:
            print(item.count('"'))
            print(item)
            raise AssertionError

    # split by last comma -- will get list with all keys and values
    # first and last -- append manually
    # get rid of '"' and spaces
    # int() numbers

    pre_dict = [new_lst[0].strip().strip('"')]
    for item in new_lst[1:-1]:
        last_comma = item.rfind(',')
        if last_comma == -1:
            if item.isdigit():
                pre_dict.append(int(item))
            else:
                pre_dict.append(item.strip().strip('"'))
            continue
        first = (item[:last_comma]).strip().strip('"')
        second = (item[last_comma + 1:]).strip().strip('"')
        for i in (first, second):
            if i.isdigit():
                pre_dict.append(int(i))
            else:
                pre_dict.append(i)
    pre_dict.append(new_lst[-1].strip().strip('"'))

    # make dict from list
    result_dict = {pre_dict[i]: pre_dict[i + 1] for i in range(0, len(pre_dict), 2)}
    return result_dict


def json_parse(j_str):
    """takes string of json object, returns list of dicts with json objects"""
    str_list = split_str_of_json_objects(j_str)
    dict_list = []
    for item in str_list:
        dict_i = json_object_to_dict(item)
        dict_list.append(dict_i)
    return dict_list


with open(r'winedata_1.json', 'r') as vine_1:
    vines_str_1 = vine_1.read()
with open(r'winedata_2.json', 'r') as vine_2:
    vines_str_2 = vine_2.read()

vines_1 = json_parse(vines_str_1)
vines_2 = json_parse(vines_str_2)
print(len(vines_1), len(vines_2))

# merge 2 vines list
vines = []
for vine in vines_1[:5]:
    if vine not in vines_2[:5]:
        vines.append(vine)
        continue

for vine in vines_2:
    vines.append(vine)

# print(f'num of duplicates: {len(vines_1) + len(vines_2) - len(vines)}') # 1989
print(f'num of vines {len(vines)}')

with open(r'wine_data.json', 'w') as vines_file:
    vines_file.write(repr(vines))
