import pandas as pd

table_name = "test.csv"
# Create a dataframe from CSV
# df = pd.read_csv("2_monthly_data/optomate_2000_060_monthly.csv", delimiter="\t", index_col=0)
# df1 = pd.read_csv("3_daily_data/optomate_4507_031_2022-09-16_daily.csv", delimiter="\t", index_col=0)
# df2 = pd.read_csv("3_daily_data/optomate_4507_031_2022-09-17_daily.csv", delimiter="\t", index_col=0)
# df1 = df1.reset_index(drop=True)
# df1 = df1.sort_values(by=['MARs'], ascending=False)
# df2 = df2.reset_index(drop=True)
# df2 = df2.sort_values(by=['MARs'], ascending=False)
# merged = df1.merge(df2, on='table')

time_dict = ["2022-09-16", "2022-09-17", "2022-09-18", "2022-09-19",
             "2022-09-20", "2022-09-21", "2022-09-22"]
col_dict_2000_060 = ["speclensaddons",
            "specframe_branch",
            "specframe",
            "speclenses_branch",
            "speclenses",
            "sunglass_branch",
            "sunglass",
            "spectaclelens_tint_branch",
            "spectaclelens_tint",
            "fivetran_audit",]

col_dict_2042_049 = ["speclensaddons",
            "specframe",
            "specframe_branch",
            "speclenses",
            "speclenses_branch",
            "sunglass_branch",
            "sunglass",
            "spectaclelens_tint_branch",
            "spectaclelens_tint",
            "fivetran_audit",]

col_dict_4507_031 = ["speclensaddons",
            "specframe",
            "specframe_branch",
            "sunglass_branch",
            "sunglass",
            "speclenses_branch",
            "speclenses",
            "spectaclelens_tint_branch",
            "spectaclelens_tint",
            "patient",]

name_dict = [
    "optomate_2000_060_",
    "optomate_2042_049_",
    "optomate_4507_031_",
]

for date_time in time_dict:
    daily_data = '3_daily_data/optomate_4507_031_' + str(date_time) + '_daily.csv'
    df3 = pd.read_csv(daily_data, delimiter="\t",  index_col=0)
    for column in col_dict_4507_031:
        df4 = df3[df3["table"] == str(column)]
        df4.columns = [''] * len(df4.columns)
        print(df4.head(10))

# print(merged.drop(merged.columns[[1]], axis=1).head(20))

# print(merged.sort_values(by=['MARs'], ascending=False).head(10))

# # Filter record that date from "2022-09-15"
# df = df[df["date"] >= "2022-09-15"].reset_index()
# df_date_table = df.groupby(['date', 'table'])
#
# # Set display max_row to display all record
# pd.set_option('display.max_rows', None)
# print(df_date_table.first())

# df_date_table.sum().reset_index().to_csv(table_name, sep='\t', encoding='utf-8', index=False)
