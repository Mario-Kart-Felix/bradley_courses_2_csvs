import pandas as pd
# 
# 
# csvPath = "C:\\projects\\pg\\bradley_courses_2_csvs\\outputs\\bcc_approved_courses_page_CSVs\\Communication.csv"
# xlsxPath = "C:\\projects\\pg\\bradley_courses_2_csvs\\outputs\\bcc_approved_courses_page_CSVs\\Communication.xlsx"
# pd.read_csv(csvPath, delimiter=",").to_excel(xlsxPath, index=False)


csvPath = "C:\\projects\\pg\\bradley_courses_2_csvs\\outputs\\bcc_approved_courses_page_CSVs\\Communication.csv"
xlsxPath = "C:\\projects\\pg\\bradley_courses_2_csvs\\outputs\\bcc_approved_courses_page_CSVs\\Communication.xlsx"
pd.read_csv(csvPath, delimiter=",").to_excel(xlsxPath, index=False)