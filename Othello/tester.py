a_dict = {'color': ['1','2','3','4','5'], 'fruit': [6,7,8,9,10], 'pet': 'dog'}

for key in a_dict.keys():
    if '2' in a_dict[key]:
        arb_lst = a_dict[key]
        for col in range(len(arb_lst)):
            if arb_lst[col] == '2':
                arb_lst[col] = '100'
        a_dict[key] = arb_lst

print(a_dict)