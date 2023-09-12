import requests
r = requests.get("https://raw.githubusercontent.com/jamessch16/CMPUT_404_Lab_1/master/lab1_script.py")
print(r.text)