companies = {'Sony': 120, 'HTC': 150, 'Mozilla': 500, 'Safari': 400}

# sort by values ascending, if -x[1] - descending, returns as tuples
sorted_companies_data = sorted(companies.items(), key=lambda x: x[1])
# sort by values descending, if -x[1] - descending
sorted_companies_data1 = sorted(companies.items(), key=lambda x: -x[1])
# sort by keys alphabetical
sorted_companies_data2 = sorted(companies.items(), key=lambda x: x[0])
# sort first by values then by keys
sorted_companies_data3 = sorted(companies.items(), key=lambda x: (x[1], x[0]))

print(sorted_companies_data)
print(sorted_companies_data1)
print(sorted_companies_data2)
print(sorted_companies_data3)