dct = {
    "region": ["A", "A", "B", "B"],
    "sales": [100, 200, 400, 500],
}
total_sales = {}
print(set(dct["region"]))
for region in set(dct["region"]):
    print(region)

    total_sales[region] = 0
    for i in range(len(dct["region"])):
        if dct["region"][i] == region:
            total_sales[region] += dct["sales"][i]
print(total_sales)
