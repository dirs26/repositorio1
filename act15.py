import pandas as pd
import matplotlib.pyplot as plt

z1=['YZY 350', 400]
z2=['YZY 700', 520]
z3=['YZY 500', 320]
z4=['AF1', 120]
z5=['YZY FOAM ', 400]
z6=['YZY 380', 550]

list_zaps=[z1,z2,z3,z4,z5,z6]
zapatos=pd.DataFrame(list_zaps,columns=['Modelo', 'Precio'])
print(zapatos)

plt.plot(zapatos['Modelo'], zapatos['Precio'])
plt.show()

plt.scatter(zapatos['Modelo'], zapatos['Precio'])
plt.show()

plt.barh(zapatos['Modelo'], zapatos['Precio'])
plt.show()

plt.bar(zapatos['Modelo'], zapatos['Precio'])
plt.show()

plt.pie(zapatos['Precio'], labels=zapatos['Modelo'])
plt.show()