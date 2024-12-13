# Stock Ranking Too
import csv
import pandas as pd
df =pd.read_csv(r"C:\Users\samfa\OneDrive\The Falken Composite\Python Codes\Dec042024CSStocksCSV.csv")

# Filter the DataFrame based on a condition
df['Market Cap'] = df['Market Cap'].astype(int)

#df['Price to Earnings'] = df['Price to Earnings'].replace('--', '-1')
#df['Price/Sales (TTM)'] = df['Price/Sales (TTM)'].replace('--', '-1')
#df['PB MRQ'] = df['PB MRQ'].replace('--', '-1')
#df['Current Ratio (MRQ)'] = df['Current Ratio (MRQ)'].replace('--', '-1')
#df['Debt to Equity (MRQ)'] = df['Debt to Equity (MRQ)'].replace('--', '-1')
#df['Price to Earnings'] = df['Price to Earnings'].astype(float)

filtered_df_PE = df[(df['Universe']  == "Domestic") & (df['Market Cap'] >= 25000000) & (df['Price to Earnings'] != '--')]
filtered_df_PE = filtered_df_PE.sort_values(by='Price to Earnings', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False)
filtered_df_PE['Price to Earnings'] = filtered_df_PE['Price to Earnings'].astype(float)
filtered_df_PE['PE Rank'] = filtered_df_PE['Price to Earnings'].rank(method='average', ascending = False)
df_PE = filtered_df_PE[['Symbol','PE Rank']]


filtered_df_PS = df[(df['Universe']  == "Domestic") & (df['Market Cap'] >= 25000000) & (df['Price/Sales (TTM)'] != '--')]
filtered_df_PS = filtered_df_PS.sort_values(by='Price/Sales (TTM)', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False)
filtered_df_PS['Price/Sales (TTM)'] = filtered_df_PS['Price/Sales (TTM)'].astype(float)
filtered_df_PS['PS Rank'] = filtered_df_PS['Price/Sales (TTM)'].rank(method='average', ascending = False)
df_PS = filtered_df_PS[['Symbol','PS Rank']]

filtered_df_PB = df[(df['Universe']  == "Domestic") & (df['Market Cap'] >= 25000000) & (df['P:B MRQ'] != '--')]
filtered_df_PB = filtered_df_PB.sort_values(by='P:B MRQ', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False)
filtered_df_PB['PB MRQ'] = filtered_df_PB['P:B MRQ'].astype(float)
filtered_df_PB['PB Rank'] = filtered_df_PB['PB MRQ'].rank(method='average',ascending = False)
df_PB = filtered_df_PB[['Symbol','PB Rank']]

filtered_df_CR = df[(df['Universe']  == "Domestic") & (df['Market Cap'] >= 25000000) & (df['Current Ratio (MRQ)'] != '--')]
filtered_df_CR = filtered_df_CR.sort_values(by='Current Ratio (MRQ)', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False)
filtered_df_CR['Current Ratio (MRQ)'] = filtered_df_CR['Current Ratio (MRQ)'].astype(float) 
filtered_df_CR['CR Rank'] = filtered_df_CR['Current Ratio (MRQ)'].rank(method='average', ascending = True)
df_CR = filtered_df_CR[['Symbol','CR Rank']]

filtered_df_DE = df[(df['Universe']  == "Domestic") & (df['Market Cap'] >= 25000000) & (df['Debt to Equity (MRQ)'] != '--')]
filtered_df_DE = filtered_df_DE.sort_values(by='Debt to Equity (MRQ)', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False)
filtered_df_DE['Debt to Equity (MRQ)'] = filtered_df_DE['Debt to Equity (MRQ)'].astype(float)
filtered_df_DE['DE Rank'] = filtered_df_DE['Debt to Equity (MRQ)'].rank(method='average', ascending = False)
df_DE = filtered_df_DE[['Symbol','DE Rank']]



#df_PE['PE Rank'].fillna(0) 
#df_PS['PB Rank'].fillna(0)
#df_PB['PS Rank'].fillna(0)
#df_CR['CR Rank'].fillna(0)
#df_DE['DE Rank'].fillna(0)


final_df = df[(df['Universe']  == "Domestic") & (df['Market Cap'] >= 25000000)]


final_df = pd.merge(final_df, df_PE, on='Symbol', how='left')
final_df = pd.merge(final_df, df_PS, on='Symbol', how='left')
final_df = pd.merge(final_df, df_PB, on='Symbol', how='left')
final_df = pd.merge(final_df, df_CR, on='Symbol', how='left')
final_df = pd.merge(final_df, df_DE, on='Symbol', how='left')


final_df['PE Rank_y'] = final_df['PE Rank_y'].fillna(0)
final_df['PS Rank_y'] = final_df['PS Rank_y'].fillna(0)
final_df['PB Rank_y'] = final_df['PB Rank_y'].fillna(0)
final_df['CR Rank_y'] = final_df['CR Rank_y'].fillna(0)
final_df['DE Rank_y'] = final_df['DE Rank_y'].fillna(0)



final_df['Value Composite Score'] = final_df['PE Rank_y'] + final_df['PS Rank_y'] + final_df['PB Rank_y'] + final_df['CR Rank_y'] + final_df['DE Rank_y']
final_df = final_df.sort_values(by='Value Composite Score', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last', ignore_index=False)


print(final_df)



filename0 = "AnalyzedStocks Domestic Value.csv"

#filename = 'AnalyzedStocksPE.csv'
#filename2 = 'AnalyzedStocksPS.csv'
#filename3 = 'AnalyzedStocksPB.csv'
#filename4 = 'AnalyzedStocksCR.csv'
#filename5 = 'AnalyzedStocksDE.csv'

final_df.to_csv(filename0, sep=",", header=True, encoding='utf-8',index=False)

#filtered_df_PE.to_csv(filename, sep=",", header=True, encoding='utf-8',index=False)
#filtered_df_PS.to_csv(filename2, sep=",", header=True, encoding='utf-8',index=False)
#filtered_df_PB.to_csv(filename3, sep=",", header=True, encoding='utf-8',index=False)
#filtered_df_CR.to_csv(filename4, sep=",", header=True, encoding='utf-8',index=False)
#filtered_df_DE.to_csv(filename5, sep=",", header=True, encoding='utf-8',index=False)





#with open(filename, 'w', newline='') as file:
 #   writer = csv.writer(file)
  #  writer.writerows(filtered_df)

print(f"Data has been exported to {filename0}")
#ranked_df_MarCap = filtered_df[]

#filtered_df['rank'] = filtered_df['column_to_rank'].rank(ascending=False)



# Optionally, sort by the rank
#ranked_df = filtered_df.sort_values(by='rank')

# Display the ranked DataFrame
#print(ranked_df)

# Save the ranked DataFrame to a new CSV file if needed
#ranked_df.to_csv('ranked_output.csv', index=False)