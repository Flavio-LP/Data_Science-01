import pandas as pd
import matplotlib.pyplot as plt

credit = pd.read_excel('credit_card_info.xlsx')

#print(credit.shape) # Retorna a dminesão do datafarme

#print(credit.head()) # visualizar começo do dataframe

#AGE_34 = credit["AGE"] > 35

#print (credit["AGE"].plot())
credit.plot.scatter(x="AGE", y="EDUCATION", alpha=0.5)

print(plt.show())
