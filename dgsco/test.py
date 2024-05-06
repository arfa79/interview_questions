# how can ern max profit from days of work based on days of work
# if i want to ern that from numbers minus work in max proft to minimum

final = []
profit = [7,1,5,3,6,4]
for i in profit :
    for j in profit :
        result = i - j 
        final.append(result) 
print(max(final))

# leetcode
# python book : fluent python and head first python