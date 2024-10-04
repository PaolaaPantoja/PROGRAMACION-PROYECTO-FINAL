import seaborn as sns




tips = sns.load_dataset("tips")




# Create a histogram of the total bill amounts

sns.histplot(data=tips, x="total_bill")