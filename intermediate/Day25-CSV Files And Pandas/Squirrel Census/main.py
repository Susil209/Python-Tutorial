import pandas as pd

data = pd.read_csv("data.csv")

# Gray Squirrels
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_by_id = gray_squirrels['Unique Squirrel ID'].count()
print(f"No of gray squirrels: {gray_squirrels_by_id}")

# Cinnamon
cin_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
cin_squirrels_by_id = cin_squirrels['Unique Squirrel ID'].count()
print(f"No of cinnamon squirrels: {cin_squirrels_by_id}")

# Black
black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_by_id = black_squirrels['Unique Squirrel ID'].count()
print(f"No of black squirrels: {black_squirrels_by_id}")

# construct dataframe
data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_by_id, cin_squirrels_by_id, black_squirrels_by_id]
}

df = pd.DataFrame(data_dict)
# print(df)

# create another csv file and put the dataframe
df.to_csv("squirrels_count.csv")