import pandas as pd

table_name = "test.csv"
# Create a dataframe from CSV
df = pd.read_csv("optomate_2042_049_daily.csv", delimiter="\t", index_col=0)

# Filter record that date from "2022-09-15"
df = df[df["date"] >= "2022-09-15"].reset_index()
df_date_table = df.groupby(['date', 'table'])

# Set display max_row to display all record
pd.set_option('display.max_rows', None)
print(df_date_table.first())

df_date_table.sum().reset_index().to_csv(table_name, sep='\t', encoding='utf-8', index=False)