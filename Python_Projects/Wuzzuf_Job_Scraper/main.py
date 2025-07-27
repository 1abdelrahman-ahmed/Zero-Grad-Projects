from scrape import scrape_pages, combine_dfs, combine_dicts

if __name__ == "__main__":

    ds_dict, ds_df = scrape_pages('Data science')
    ml_dict, ml_df = scrape_pages('Machine learning')
    ai_dict, ai_df = scrape_pages('Artificial intelligence')

    combined_dict = combine_dicts([ds_dict, ml_dict, ai_dict])
    combined_df = combine_dfs([ds_df, ml_df, ai_df])

    combined_df.to_csv('data.csv', index=False)