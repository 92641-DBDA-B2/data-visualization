import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('mtcars.csv')
print(df)

def function1():
    plt.scatter(df['wt'], df['qsec'])
    plt.tight_layout()

    plt.show()

# function1()

def function2():
    categories = []
    for qsec in df['qsec']:
        if qsec > 18:
            categories.append(1)
        elif qsec > 16:
            categories.append(2)
        else:
            categories.append(3)

    plt.scatter(
        df['wt'], 
        df['qsec'],
        c=categories, 
        cmap='CMRmap',
        )
    
    plt.title("wt vs qsec")
    plt.xlabel("wt")
    plt.ylabel("qsec")

    plt.tight_layout()
    plt.show()
    
# function2()


def function3():
    plt.plot(
        df['wt'], 
        df['qsec'], 
        color = 'red',
        linestyle = '--'
        )
    
    plt.title("wt vs qsec")
    plt.xlabel("wt")
    plt.ylabel("qsec")
    plt.grid(visible=True)

    plt.tight_layout()
    plt.show()

# function3()


def function4():
    plt.scatter(
        df['wt'], 
        df['qsec']
    )

    plt.plot(
        df['wt'], 
        df['qsec'], 
        color = 'red',
        )
    
    plt.title("wt vs qsec")
    plt.xlabel("wt")
    plt.ylabel("qsec")
    plt.grid(visible=True)

    plt.tight_layout()
    plt.show()

# function4()

def function5():
    _,axes = plt.subplots(2,2)

    axes[0,0].scatter(df['wt'], df['qsec'])
    axes[0,1].scatter(df['drat'], df['hp'])
    axes[1,0].scatter(df['wt'], df['hp'])
    axes[1,1].scatter(df['cyl'], df['qsec'])

    plt.tight_layout()
    plt.show()

function5()    