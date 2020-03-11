def get_WH_data_for_given_year(data_path: str, year: int) -> pd.DataFrame:
    WH_df=pd.read_csv(data_path)
    selected_rows=WH_df["Year"]==year
    selected_columns=WH_df.columns[2:9]

    WH_year_df=WH_df.loc[selected_rows,selected_columns]
    return WH_year_df