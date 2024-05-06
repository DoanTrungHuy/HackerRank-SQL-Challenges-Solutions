import pandas as pd
import matplotlib.pyplot as plt

# PROBLEM: https://www.hackerrank.com/challenges/occupations/problem

data = {
    'Name': ['Abigail', 'Samantha', 'Julia', 'Ashley', 'Maria', 'Jane', 'Christeen', 'Kristeen', 'Scarlet', 'Amelia', 'Priya', 'Meera', 'Priyanka', 'Priyanka', 'Jennifer', 'Priya', 'Julia', 'Kristeen', 'Samantha', 'Ashley'],
    'Occupation': ['Doctor']*10 + ['Professor']*3 + ['Singer']*7,
}

df = pd.DataFrame(data)

grouped = df.groupby('Occupation').size()

grouped.plot(kind='bar', color='skyblue')
plt.title('Number of People in Each Occupation')
plt.xlabel('Occupation')
plt.ylabel('Number of People')
plt.xticks(rotation=45)
plt.show()
