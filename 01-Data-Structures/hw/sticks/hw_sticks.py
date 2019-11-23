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
    return lst[:40]


def json_object_to_dict(j_str):
    """Splits string of 1 json object into dict.
    1. split by ':', except ':' in description
    2. then splits by last ','
    3. int(numbers)
    4. 'null'
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

    # now split by last comma -- will get list with all keys and values
    # first and last -- append manually
    # get rid of '"' and spaces
    # int() numbers

    pre_dict = [new_lst[0].strip()]
    for item in new_lst[1:-1]:
        last_comma = item.rfind(',')
        if last_comma == -1:
            if item.isdigit():
                pre_dict.append(int(item))
            else:
                pre_dict.append(item.strip())
            continue
        first = (item[:last_comma]).strip()
        second = (item[last_comma + 1:]).strip()
        for i in (first, second):
            if i.isdigit():
                pre_dict.append(int(i))
            else:
                pre_dict.append(i)
    pre_dict.append(new_lst[-1].strip())

    # make dict from list
    result_dict = {pre_dict[i]: pre_dict[i + 1] for i in
                   range(0, len(pre_dict), 2)}
    return result_dict


def json_parse(j_str):
    """takes string of json object, returns list of dicts with json objects"""
    str_list = split_str_of_json_objects(j_str)
    dict_list = []
    for item in str_list:
        dict_i = json_object_to_dict(item)
        dict_list.append(dict_i)
    return dict_list


def json_dump(lst):
    """takes list of dicts and return a string json file"""
    result = ''
    for item in lst:
        dict_items = item.items()
        tmp = ''
        for key, value in dict_items:
            tmp += f"{str(key)}: {str(value) if value != 0 else 'null'}, "
        result += '{' + tmp[:-2] + '}, '
    return '[' + result[:-2] + ']'


# OPEN FILES and REMOVE DUPLICATES


with open('winedata_1.json', 'r') as wine_1:
    wines_str_1 = wine_1.read()
with open('winedata_2.json', 'r') as wine_2:
    wines_str_2 = wine_2.read()

# remove duplicates wines_1 only by title
wines_1_with_duplicates = json_parse(wines_str_1)
wines_1_titles = []
wines_1 = []
for wine in wines_1_with_duplicates:
    wine_title = wine.get('"title"')
    if wine_title not in wines_1_titles:
        wines_1_titles.append(wine_title)
        wines_1.append(wine)
duplicates_in_wines_1 = len(wines_1_with_duplicates) - len(wines_1)
print(f'duplicates_in_wines_1 = {duplicates_in_wines_1}')

# remove duplicates wines_2 only by title
wines_2_with_duplicates = json_parse(wines_str_2)
wines_2_titles = []
wines_2 = []
for wine in wines_2_with_duplicates:
    wine_title = wine.get('"title"')
    if wine_title not in wines_2_titles:
        wines_2_titles.append(wine_title)
        wines_2.append(wine)
duplicates_in_wines_2 = len(wines_2_with_duplicates) - len(wines_2)
print(f'duplicates_in_wines_2 = {duplicates_in_wines_2}')

# merge 2 wines list of dicts
wines = wines_1 + wines_2

# SORTING


# 1. sort by variety
wines = sorted(wines, key=lambda i: i['"variety"'])

# 2. sort by price
# change wine's price from 'null' to 0 for sorting
for wine in wines:
    if wine.get('"price"') == 'null':
        wine['"price"'] = 0

wines = sorted(wines, key=lambda i: i['"price"'], reverse=True)

# change back wine's price from 0 to 'null'
for wine in wines:
    if wine.get('"price"') == 0:
        wine['"price"'] = 'null'

print(f'Num of duplicates: '
      f'{len(wines_1_with_duplicates) + len(wines_2_with_duplicates) - len(wines)}')
print(f'Total num of wines {len(wines)}')


# DUMP and WRITE into json file


wines = json_dump(wines)

with open('winedata_full.json', 'w') as wines_file:
    wines_file.write(wines)
