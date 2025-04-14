sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales_w2.append(17)
###
sales_w1.extend(sales_w2)
###
best_day = max(sales_w1)
worst_day = min(sales_w1)
###
earnd_best_day = best_day * 1.5
earnd_worst_day = worst_day * 1.5
print(earnd_best_day)
print(earnd_worst_day)