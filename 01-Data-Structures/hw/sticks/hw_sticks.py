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
    result_dict = {pre_dict[i]: pre_dict[i + 1] for i in range(0, len(pre_dict), 2)}
    return result_dict


def remove_duplicates_and_merge(*lists):
    """takes several lists with dicts and returns 1 list
    with no duplicates (comparing by title)"""
    result_set = set()
    result = []
    for lst in lists:
        for item in lst:
            item_items = tuple(item.items())
            if item_items in result_set:
                continue
            result.append(item)
            result_set.add(item_items)
    return result


def stats_for_parsed_json(wines, wines_selection):
    """takes list of dicts with wines and list with selection to make stats
    returns dict with stats:
    
    "average_price", "min_price", "max_price", 
    "most_common_region", "most_common_country", "average_score" """

    # make template

    wines_stats = {}
    for variety in wines_selection:
        metrics = {'"average_price"': {"total": None, "count": 0},
                   '"min_price"': {"total": None, "count": 0},
                   '"max_price"': {"total": None, "count": 0},
                   '"most_common_region"': {},
                   '"most_common_country"': {},
                   '"average_score"': {"total": None, "count": 0}}
        wines_stats.update({variety: metrics})

    # gather stats info

    for wine in wines:
        variety = wine.get('"variety"')
        title = wine.get('"title"')

        if title.find('Madera') != -1:
            variety = '"Madera"'
        elif title.find('Gewurztraminer') != -1:
            variety = '"Gewurztraminer"'
        if variety in wines_selection:

            # average price
            total = wines_stats[variety]['"average_price"']["total"] or 0
            wines_stats[variety]['"average_price"']["total"] = total + wine['"price"']
            count = wines_stats[variety]['"average_price"']["count"] or 0
            wines_stats[variety]['"average_price"']["count"] = count + 1

            # min price
            min_price = wines_stats[variety]['"min_price"']["total"] or 1000000
            new_price = wine['"price"']
            if new_price < min_price:
                wines_stats[variety]['"min_price"']["total"] = new_price

            # max price
            max_price = wines_stats[variety]['"max_price"']["total"] or 0
            new_price = wine['"price"']
            if new_price > max_price:
                wines_stats[variety]['"max_price"']["total"] = new_price

            # most common region
            regions = wines_stats[variety]['"most_common_region"']
            if wine['"region_1"'] != 'null':
                if wine['"region_1"'] not in regions:
                    regions.update({wine['"region_1"']: 1})
                else:
                    regions[wine['"region_1"']] += 1

            # most common country
            countries = wines_stats[variety]['"most_common_country"']
            if wine['"country"'] != 'null':
                if wine['"country"'] not in countries:
                    countries.update({wine['"country"']: 1})
                else:
                    countries[wine['"country"']] += 1

            # average score
            total = wines_stats[variety]['"average_score"']["total"] or 0
            wines_stats[variety]['"average_score"']["total"] = total + int(wine[
                '"points"'].strip('"'))
            count = wines_stats[variety]['"average_score"']["count"] or 0
            wines_stats[variety]['"average_score"']["count"] = count + 1
    # make stats in right view

    for key, value in wines_stats.items():
        # average price
        if value['"average_price"']["count"] == 0:
            value['"average_price"'] = 'null'
        else:
            value['"average_price"'] = round(
                value['"average_price"']["total"]/value['"average_price"']["count"],3)

        # min price
        value['"min_price"'] = value['"min_price"']["total"] or 'null'

        # max price
        value['"max_price"'] = value['"max_price"']["total"] or 'null'

        # most common region
        if len(value['"most_common_region"']) > 0:
            value['"most_common_region"'] = max(value['"most_common_region"'])
        else:
            value['"most_common_region"'] = 'null'

        # most common country
        if len(value['"most_common_country"']) > 0:
            value['"most_common_country"'] = max(value['"most_common_country"'])
        else:
            value['"most_common_country"'] = 'null'

        # average score
        if value['"average_score"']["count"] == 0:
            value['"average_score"'] = 'null'
        else:
            value['"average_score"'] = round(
                value['"average_score"']["total"] /
                value['"average_score"']["count"], 3)

    return wines_stats


def json_parse(j_str):
    """takes string of json object, returns list of dicts with json objects"""
    str_list = split_str_of_json_objects(j_str)
    dict_list = []
    for item in str_list:
        dict_i = json_object_to_dict(item)
        dict_list.append(dict_i)
    return dict_list


def json_dump (lst, tabs=False):
    """takes list of dicts and return a string json file"""
    result = ''
    for item in lst:
        dict_items = item.items()
        tmp = ''
        for key, value in dict_items:
            if type(value) == dict:
                value = json_dump([value])[1:-1]
            tmp += f"{str(key)}: {str(value)}, "
        result += '{' + tmp[:-2] + '}, '

    return '[' + result[:-2] + ']'


# OPEN FILES

print('opening files')

with open('winedata_1.json', 'r') as wine_1:
    wines_str_1 = wine_1.read()

with open('winedata_2.json', 'r') as wine_2:
    wines_str_2 = wine_2.read()

# PARSE and remove duplicates

print('parsing file')

wines_1 = json_parse(wines_str_1)
wines_2 = json_parse(wines_str_2)

print('removing duplicates')

wines = remove_duplicates_and_merge(wines_1, wines_2)

print('num of wines: ' + str(len(wines)))

# change wine's price and score from 'null' to 0 for sorting
for wine in wines:
    if wine.get('"price"') == 'null':
        wine['"price"'] = 0
    if wine.get('"points"') == 'null':
        wine['"points"'] = 0


#  STATISTICS

print('making stats')

one = '"Gewurztraminer"'
another = '"Gew\u00fcrztraminer"'
wines_selection = [one, '"Riesling"', '"Merlot"',
                   '"Madera"', '"Tempranillo"', '"Red Blend"']

stats = stats_for_parsed_json(wines, wines_selection)
print(stats)

with open('wines_stats.json', 'w', encoding='utf-8') as stats_file:
    stats_file.write(json_dump([stats]))


# SORTING


# 1. sort by variety
print('soring variety')

wines = sorted(wines, key=lambda i: i['"variety"'])

# 2. sort by price
print('soring price')

wines = sorted(wines, key=lambda i: i['"price"'], reverse=True)

# change back wine's price from 0 to 'null'
for wine in wines:
    if wine.get('"price"') == 0:
        wine['"price"'] = 'null'
    if wine.get('"points"') == 0:
        wine['"points"'] = 'null'


# DUMP and WRITE into file

print('dumping')

wines = json_dump(wines)

print('writing winedata_full')

with open('winedata_full.json', 'w') as wines_file:
    wines_file.write(wines)
