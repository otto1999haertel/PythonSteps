import os
from pathlib import Path

def creating_file_path(path):
    base_dir = Path(__file__).parent
    return base_dir / path

def getting_logs_per_level(path):
    log_level = {"INFO":0, "ERROR":0, "WARN":0}
    log_file = creating_file_path(path)
    with open(log_file) as file:
        for line in file:
            splittedLine = line.split()
            log_level[splittedLine[2].upper()]+=1 
            #print(line)
    return log_level
    
def getting_errors_per_user(path):
    users_logged =dict()
    log_file = creating_file_path(path)
    with open(log_file) as file:
        for line in file.readlines():
            splittedLine = line.split()
            if(splittedLine[2]=="ERROR"):
                user = splittedLine[4]
                users_logged[user] = users_logged.get(user, 0) + 1 # Increase counter for user (starts at 0 if user does not exist yet)
            #print(line)
    return users_logged

def getting_users_with_most_errors(path):
    users_error = getting_errors_per_user(path)
    return max(users_error,key=users_error.get)


if __name__ == "__main__":
    print("Log Analyzer")
    print(getting_logs_per_level("app.log"))
    print(getting_errors_per_user("app.log"))
    print (getting_users_with_most_errors("app.log"))