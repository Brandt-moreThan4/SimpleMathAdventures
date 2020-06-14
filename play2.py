import matplotlib.pyplot as plt
import bmathy
import csv
import datetime

folder = r'C:\Users\bgreen3\Desktop\Data'

dates, wealth, gdp = [], [], []
c_row = 0
with open(folder + r'\testyWealth.csv') as f:
    csv_file = csv.reader(f)
    for row in csv_file:
        # Skip Headers
        if c_row == 0:
            pass
        else:
            dates.append(row[0])
            wealth.append(int(float(row[1])))
            gdp.append(float(row[2]))
        c_row += 1

print(f'correlation is {bmathy.correlation(gdp, wealth)}')

# plt.plot(dates, wealth, dates, gdp)
plt.scatter(gdp, wealth)
plt.xlabel('gdp')
plt.show()

