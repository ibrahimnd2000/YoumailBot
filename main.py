import requests
import json
import csv

resp = requests.get('https://api.youmail.com/api/v4/authenticate', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'Content-Type': 'application/json','Accept': 'application/json', 'YouMail-User':'dckrwest@gmail.com', 'YouMail-Password':'Ihateschool1!'})

resp_dict = json.loads(resp.text)

resp = requests.get('https://api.youmail.com/api/v4/messagebox/conversations/summaries', headers={'Authorization': 'YouMail ' + resp_dict["authToken"], 'Content-Type': 'application/json','Accept': 'application/json', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'})

resp_dict = json.loads(resp.text)

print(resp_dict['conversationSummaries'][0]['recentPreview'])

def getList(dict):
    return dict.keys()

with open('youmail_texts.csv', mode='w') as csv_file:
    fieldnames = getList(resp_dict['conversationSummaries'][0])
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for response in resp_dict['conversationSummaries']:
        writer.writerow(response)


