import pandas as pd
import numpy as np

# WEATHER DATA FILE PATH IS HARD CODED IN LINE 10.
def parse_file(obj):
    
    min_lat, max_lat, min_lon, max_lon, file_name, i, job_num, bucket_ind = obj
    print(job_num)
    # Iterate all of file names in this file
    file_path = "./weatherdata/" + file_name
    df = pd.read_csv(file_path, compression='gzip', sep=",")
    df = df[[' Lat', ' Lon', ' HourlyPrecipRate']]
    
    # filter the df
    df = df[(df[' Lat'] >= min_lat) & (df[' Lat'] < max_lat) & (df[' Lon'] >= min_lon) & (df[' Lon'] < max_lon)]
    df = df.reset_index(drop=True)
    
    # If not enough data, skip this file
    if df.shape[0] <= 1000:
        print("None")
        return None

    '''Add in all missing data'''

    ### Determine which lat/lon cords already exist
    s = set()
    for i in df.index:
        s.add(tuple((df.iloc[i][0], df.iloc[i][1])))


    ### Add all other lat/lon cords that do not exist in s
    for lat in np.arange(min_lat, max_lat, 0.1):
        lat = np.round(lat, 2)
        for lon in np.arange(min_lon, max_lon, 0.1):
            lon = np.round(lon, 2)
            if tuple([lat, lon]) not in s:
                # print(lat,lon,np.count_nonzero(np.array(X[" Lat"] == lat) & np.array(X[" Lon"] == lon)))
                # if this lat/lon cord does not exist, add [lat, lon, 0]
                df.loc[-1] = [lat, lon, 0]
                df.index = df.index + 1

    df.sort_values(by=[" Lat", " Lon"]).reset_index(drop=True)

    return df[[df.columns[0], df.columns[1], df.columns[2]]].to_numpy()


def make_trios(curr_data):
    
    trio_data = []
    for i in np.arange(len(curr_data)-2):
        trio_data.append([curr_data[i], curr_data[i+1], curr_data[i+2]])
    trio_data = np.array(trio_data)
    
    return trio_data