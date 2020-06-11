import os
import re
import pandas as pd
import time
import twint
from twitter_scraper import Profile 
import importlib as im

def read_and_append(path):    
    mylist = os.listdir(path)
    mylist = mylist[:]
    date_list = []
    covid_df = pd.DataFrame()
    #Covid Tweets CSVs start with 2020 so 
    #we identify those
    counter = 0
    csv_name = mylist[7]

    '''
    for file in mylist:
        counter += 1
        if file[:4].isdigit():
            date_list.append(file)
    '''
    counter = 0
    t0 = time.time()

    #for file in date_list:
    csv_file = path + "/" + csv_name
    df = pd.read_csv(csv_file)
    print("With all languages: ", df.shape[0])
    df = df[df['lang'] == "en"]
    print("With just english:", df.shape)
    covid_df = covid_df.append(df)
    print("Df appended:", time.time() - t0)
    counter += 1

    print(time.time() - t0)
    print(covid_df.shape)
    return covid_df

def drop_dup_users(covid_df, user_var):

    user_df = covid_df[user_var].drop_duplicates().reset_index()
    user_df = user_df.drop(columns=['index'])

    return user_df

def get_user_information(user_df, path):

    success = 0
    errors = 0
    restart = 0
    tmp = pd.DataFrame()
    t0 = time.time()
    output_csv_file = path + ".csv"
    output_pkl_file = path + ".pkl"
    missing_info = pd.DataFrame(columns=['user_id'])

    for user in user_df['user_id']:

        try:
            im.reload(twint)
            c = twint.Config()
            c.Followers = True
            c.Following = True
            c.Profile_full = True 
            c.Pandas = True
            c.User_full = False
            c.User_id = user
            twint.run.Lookup(c)
            df = twint.storage.panda.User_df
            df = df.drop_duplicates()
            tmp = tmp.append(df)
            success += 1
            restart += 1
            print(success, time.time() - t0)
            if restart == 500:
                restart = 0
                tmp = tmp.drop_duplicates()
                print(tmp)
                tmp.to_csv(output_csv_file)
                tmp.to_pickle(output_pkl_file)
        except:
            missing_info = missing_info.append({'user_id': user}, ignore_index=True)

            missing_info.to_csv("covid_error_info.csv")
            missing_info.to_pickle("covid_error_info.pkl")

            errors += 1
            print(user, "Not Found", errors)

    tmp = tmp.drop_duplicates()
    tmp.to_csv(output_csv_file)

    print(time.time() - t0)
    return tmp


def merge_with_bots(user_df, bots_df, save_path):
    user_df = user_df.rename(columns={"user_id": "id"})
    result = pd.merge(user_df, bots_df, on='id')
    result.to_csv(save_path)

