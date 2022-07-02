import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read csv
data = pd.read_csv("data.csv")
# print(data)

#...............if taking ony one row of data......................
data = data.tail(1)
# print(data)
# fig, ax = plt.subplots()
# x = np.arange(len(data))

# dim = len(data)
# w = 0.3
# dimw = w / dim

# for i in range(len(data)):
#     y = [d[i] for d in data]
#     b = ax.barh(x + i * dimw, y,dimw, left = 0.001)

# ax.set_yticks(x + dimw / 2)
# ax.set_yticklabels(map(str, x))
# # ax.set_xscale('log')
  
# ax.set_title('matplotlib.axes.Axes.barh Example')

# # plt.barh(y=data.columns,width=0.5,height=0.8,align='center')
# plt.show()

# intialise data of lists.
# data = {'Column1':['True', 'False', 'True', 'True'],
#         'Column2':['True', 'False', 'False', 'True'],
#         'Column3':['True', 'False', 'True', 'True']}
# df = pd.DataFrame(data)

# if data["gloves"].values == True:
#     var1_true = "True"  
#     var1_false = "False"
# else:
#     var1_true = "False"  
#     var1_false = "True"
# print(var1_true,var1_false)
# if data["bottle"].values == True:
#     var2_true = "True"
#     var2_false = "False"
# else:
#     var2_true = "False"
#     var2_false = "True"
# print(var2_true,var2_false)
# if data["sop"].values == True:
#     var3_true = "True"
#     var3_false = "False"
# else:
#     var3_true = "False"
#     var3_false = "True"
# print(var3_true,var3_false)

# data_try = pd.DataFrame({'True':[var1_true,var2_true,var3_true],
#             'False':[var1_false,var2_false,var3_false],
#                 }, index = ['Gloves', 'Bottle','SOP'])

# print(data_try)

def make_graph(df):
    # df will be the csv file from where we are selecting data in tru false format.
    data_new = pd.DataFrame({'True':[sum(df.gloves == True),sum(df.bottle == True),sum(df.sop == True)],
            'False':[sum(df.gloves == False),sum(df.bottle == False),sum(df.sop == False)],
                }, index = ['Gloves', 'Bottle','SOP'])

    print(data_new)
    # create stacked bar chart for data_new DataFrame
    data_new.plot.barh(stacked=True, color=['red', 'pink'])
    # Add Title and Labels
    plt.title('Activity Chart')
    plt.xlabel('Number of Occurances')
    plt.legend(bbox_to_anchor=(0.9, 1))
    plt.savefig("graph_1.png")

make_graph(data)