# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv

with open('07.txt', 'r', encoding='GBK') as f:
    lines = f.readlines()
    first_list = list()
    second_list = list()
    for line_counter, line in enumerate(lines):
        if line.find("insert into lottery.match values") != -1:
            first_list.append(line.rstrip("\n").strip("insert into lottery.match values\(").strip('"').strip(");").split(","))

        if line.find("insert into lottery.europe_data values(") != -1:
            second_list.append(line.rstrip("\n").strip("insert into lottery.europe_data values\(").strip(");").split(","))

    headers = ['Interwetten0_end', 'Interwetten0_raw', 'Interwetten1_end', 'Interwetten1_raw', 'Interwetten3_end', 'Interwetten3_raw', 'guest', 'host', 'league', 'number', 'result', 'score', 'session', 'william0_end', 'william0_raw', 'william1_end', 'william1_raw', 'william3_end', 'william3_raw']

    final_list = list()
    for item in first_list:
        sub_dict = {}
        # number
        sub_dict.update({'number':  item[0].strip("'")[:5]})
        # league
        sub_dict.update({'league': item[1].strip("'")})
        # host
        sub_dict.update({'host': item[2].strip("'")})
        # guest
        sub_dict.update({'guest': item[3].strip("'")})
        # score
        sub_dict.update({'score': item[4].strip("'")})
        # result
        sub_dict.update({'result': item[5].strip("'")})

        for sub in second_list:
            if sub[5].find(item[0]) != -1:
                if sub[0].find('williamHill') != -1:
                    if sub[1].find('firstData') != -1:
                        sub_dict.update({'william3_raw': sub[2].strip("'")})
                        sub_dict.update({'william1_raw': sub[3].strip("'")})
                        sub_dict.update({'william0_raw': sub[4].strip("'")})
                    else:
                        sub_dict.update({'william3_end': sub[2].strip("'")})
                        sub_dict.update({'william1_end': sub[3].strip("'")})
                        sub_dict.update({'william0_end': sub[4].strip("'")})
                elif sub[0].find('Interwetten') != -1:
                    if sub[1].find('firstData') != -1:
                        sub_dict.update({'Interwetten3_raw': sub[2].strip("'")})
                        sub_dict.update({'Interwetten1_raw': sub[3].strip("'")})
                        sub_dict.update({'Interwetten0_raw': sub[4].strip("'")})
                    else:
                        sub_dict.update({'Interwetten3_end': sub[2].strip("'")})
                        sub_dict.update({'Interwetten1_end': sub[3].strip("'")})
                        sub_dict.update({'Interwetten0_end': sub[4].strip("'")})

        final_list.append(sub_dict)

    with open('07105-07001_final.csv', 'w', newline='')as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(final_list)









