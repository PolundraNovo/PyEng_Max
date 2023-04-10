with open('ospf.txt') as f:
    list1 = ['Prefix', 'AD/Metric','Next-Hop','Last update','Outbound Interface']
    for line in f:
        line_list = line.split()
        if line_list and 'via' in line_list:
            print(f'{list1[0]:20} {line_list[1]:20}')
            print(f'{list1[1]:20} {line_list[2][1:-1]:20}')
            print(f'{list1[2]:20} {line_list[4][:-1]:20}')
            print(f'{list1[3]:20} {line_list[5][:-1]:20}')
            print(f'{list1[4]:20} {line_list[6]:20}')

#            print({15}.format('AD/Metric',line_list[3]))