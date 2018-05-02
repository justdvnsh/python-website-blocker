import time
from datetime import datetime as dt

host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

website_list = []

while True:
	website_to_be_blocked = input("Enter the website you wish to block [--Help: Type 'done' to stop]: ")
	if website_to_be_blocked == 'done':
		break;
	else:
		if 'www.' in website_to_be_blocked:
			website_list.append(website_to_be_blocked)
		else:
			website_list.append('www.' + website_to_be_blocked)


print(website_list)

start_time = int(input("Enter the starting time (in 24 HR rule) : "))
end_time = int(input("Enter the end time (in 24 HR rule) : "))

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,start_time) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end_time):
        print("Working hours...")
        with open(host_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
