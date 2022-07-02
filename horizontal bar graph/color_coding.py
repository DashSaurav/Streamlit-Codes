import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read csv
data = pd.read_csv("data.csv")
# print(data)

new_df = data.tail(1)
# print(new_df)
# fig, ax = plt.subplots(figsize=(10, 5))


# if new_df["gloves"].iloc[-1] == True:
#     print("True")
#     rect1 = ax.barh(y=new_df, width=1, color='blue', height=0.3)
# elif new_df["gloves"].iloc[-1] == False:
#     print("False")
#     rect1 = ax.barh(y=new_df, width=1, color='red', height=0.3)  


# rect2 = ax.barh(y=new_df.columns, width=0.8, label = "False")
# ax.legend(handles=[rect1, rect2], bbox_to_anchor=(1.0, 1.0))
# plt.show()

def make_graph(df):
    # df will be the csv file from where we are selecting data in tru false format.
    data_new = pd.DataFrame({'True':[sum(df.gloves == True),sum(df.bottle == True),sum(df.sop == True)],
            'False':[sum(df.gloves == False),sum(df.bottle == False),sum(df.sop == False)],
                })
    print(data_new)
    # create stacked bar chart for data_new DataFrame
    data_new.plot.barh(stacked=True, color=['lightgreen', 'pink'])
    # Add Title and Labels
    # plt.title('Activity Chart')
    plt.yticks([0, 1, 2], ['Gloves', 'Bottle', 'SOP'],rotation=45, fontsize=17)
    plt.xlabel('Current State', fontsize=17)
    plt.legend(bbox_to_anchor=(0.9, 1))
    plt.savefig("graph_new.png")

make_graph(new_df)