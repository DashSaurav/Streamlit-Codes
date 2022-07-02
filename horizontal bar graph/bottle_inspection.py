import pandas as pd
import matplotlib.pyplot as plt

# read csv
data = pd.read_csv("data_bottle.csv")
# print(data)

new_df = data.tail(1)
print(new_df)


def make_graph(df):
    # df will be the csv file from where we are selecting data in tru false format.
    data_new = pd.DataFrame({'True':[sum(df.bottle == True),sum(df.cap == True),sum(df.gloves == True)],
            'False':[sum(df.bottle == False),sum(df.cap == False),sum(df.gloves == False)],
                }, index = ['Bottle', 'Cap','Gloves'])
    print(data_new)
    data_new.plot.barh(stacked=True, color=['green', 'red'])
    # plt.title('Activity Chart')
    plt.yticks([0, 1, 2], ['Bottle', 'Cap', 'Gloves'],rotation=45, fontsize=17)
    plt.xlabel('Current State', fontsize=17)
    plt.legend(bbox_to_anchor=(0.9, 1))
    # change the path.
    plt.savefig("graph_bottle_inference.png")

make_graph(new_df)