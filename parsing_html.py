import json
import pandas as pd

# name = "optomate_4507_031"
# name = "optomate_2042_049"
# name = "optomate_2000_060"

time_dict = ["2022-09-15", "2022-09-16", "2022-09-17", "2022-09-18", "2022-09-19", "2022-09-20", "2022-09-21",
             "2022-09-22", "2022-09-23"]
name_dict = ["optomate_2000_060", "optomate_2042_049", "optomate_4507_031"]

for name in name_dict:
    for date_time in time_dict:
        json_name = name + "_all_info.json"
        csv_monthly = name + "_monthly.csv"
        csv_daily = name + "_" + date_time + "_daily.csv"
        # Opening JSON file
        f = open("1_database/" + json_name)

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Create an empty List
        list_monthly_table = []
        list_monthly_mar = []
        list_all_date = []

        # MONTHLY DATA
        # Take values from json and save into a list
        for i in range(len(data['monthly'])):
            monthly_table_name = list(data['monthly'][i].values())[1]
            monthly_mar_values = list(data['monthly'][i].values())[2]
            list_monthly_table.append(monthly_table_name)
            list_monthly_mar.append(monthly_mar_values)

        print(list_monthly_table)
        print(list_monthly_mar)

        # Create dict from 2 list created from json file
        data_monthly_dict = {
            'table_name': list_monthly_table,
            'mar_values': list_monthly_mar
        }

        # DAILY DATA
        # Take values from json and save into a list
        for i in range(len(data['daily'])):
            daily_table_name = list(data['daily'][i].values())[1]
            daily_date = list(data['daily'][i].values())[2]
            daily_mar_values = list(data['daily'][i].values())[3]
            daily_list = [daily_table_name, daily_date, daily_mar_values]
            list_all_date.append(daily_list)

        print(list_monthly_table)
        print(list_monthly_mar)
        print(list_all_date)

        # Create dict from 2 list created from json file
        data_monthly_dict = {
            'table_name': list_monthly_table,
            'mar_values': list_monthly_mar
        }

        # Create dataframe from monthly dict
        monthly_df = pd.DataFrame(data_monthly_dict)
        print(monthly_df.head())

        # Create dataframe from daily list
        daily_df = pd.DataFrame(list_all_date, columns=['table', 'date', 'MARs'])
        print(daily_df.head())
        # Filter record that date from "2022-09-15"
        daily_df = daily_df[daily_df["date"] == date_time].reset_index(drop=True)
        df_date_table = daily_df.groupby(['date', 'table'])

        # Set display max_row to display all record
        pd.set_option('display.max_rows', None)
        print(df_date_table.first())

        # Save a monthly dataframe into a CSV file
        monthly_df.to_csv("2_monthly_data/" + csv_monthly, sep='\t', encoding='utf-8', index=False)

        # Save a daily dataframe into a CSV file
        df_date_table.sum().reset_index().to_csv("3_daily_data/" + csv_daily, sep='\t', encoding='utf-8', index=False)

        # Closing file
        f.close()
