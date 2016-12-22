import csv
from collections import OrderedDict


my_dict=[{'b':'boats','a':'apples'},{'d':'dogs','c':'cake', 'a':'anise'}]

my_keys=['a','b','c','d']

b = open('./test.csv', 'w')

wb = csv.DictWriter(b, None)


my_ordered_list=[]

for i in my_dict:
    temp=OrderedDict()
    for j in my_keys:
        try:
            temp[j]=i[j]
        except:
            pass

    my_ordered_list.append(temp)

print my_ordered_list

#
# for d in my_dict:
#
#   if wb.fieldnames is None:
#     # initialize and write b's headers
#     dh = OrderedDict((k,k) for k,v in d.items())
#     print dh
#     lh=[k for k,v in d.my_keys()]
#     print lh
#     wb.fieldnames = lh
#     wb.writerow(dh)
#
#   wb.writerow(d)
#
# b.close()