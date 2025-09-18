import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('tips.csv')


def function1():
    df.drop(['sex', 'smoker','day', 'time'], axis=1, inplace=True)

    plt.boxplot(df)

    plt.tight_layout()
    plt.show()

# function1()

def function2():
    plt.pie(df['size'],
            labels=df['size'],
            autopct='%1.1f%%'
            )
    plt.tight_layout()
    plt.show()

# function2()

def function3():
    plt.hist(df['day'])
    plt.tight_layout()
    plt.show()

# function3()

def function4():
    plt.bar(df['day'],df['total_bill'], alpha = 0.3)
    plt.xlabel("Days")
    plt.ylabel('Total Bill')
    plt.show()

# function4()

def function5():
    df.drop(['sex', 'smoker','day', 'time'], axis=1, inplace=True)

    correlation = df.corr()
    print(correlation)
    sns.heatmap(correlation, annot=True)

    plt.show()

function5()

