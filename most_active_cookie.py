import csv
from collections import defaultdict
import sys
import datetime

#date = "2018-12-08" 
#file_name = 'cookie_log.csv'

def read_file(file_name):
    file = open(file_name)
    csvreader = csv.reader(file)
    next(csvreader) #skip header
    return file, csvreader

def convert_UTC_date(date_and_time):
    return datetime.datetime.fromisoformat(date_and_time).strftime('%Y-%m-%d')

def create_dict(csvreader):
    data_dict = defaultdict(lambda: defaultdict(int))
    for cookie, date_and_time in csvreader:
        date = convert_UTC_date(date_and_time) 
        data_dict[date][cookie]+=1
    return data_dict

def find_max_cookie_count_for_date(data_dict, date):
    cookies_for_date = data_dict[date]
    max_count = max(cookies_for_date.values())
    return cookies_for_date, max_count

def find_most_active_cookies(cookies_for_date, max_count):
    return list(filter(lambda x: cookies_for_date[x] ==max_count, cookies_for_date))

def display_result(most_active_cookies):
    for cookie in most_active_cookies:
        print(cookie)
    

def main():
    file_name, utc, date = sys.argv[1:]
    file, csvreader = read_file(file_name)
    data_dict = create_dict(csvreader)
    cookies_for_date, max_count = find_max_cookie_count_for_date(data_dict, date)
    most_active_cookies = find_most_active_cookies(cookies_for_date, max_count)
    display_result(most_active_cookies)
    file.close()

if __name__ == "__main__":
    main()
