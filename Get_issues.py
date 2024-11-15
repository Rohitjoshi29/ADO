import requests
from requests.auth import HTTPBasicAuth
import json
import Config  # Import the configuration file

# WIQL query to get work items assigned to you
wiql_query = {
    "query": f"SELECT [System.Id], [System.Title], [System.AssignedTo], [System.State], [System.WorkItemType] FROM workitems WHERE [State] = 'Active' AND [System.AssignedTo] = '{Config.user_email}'"
}

# Make the request
response = requests.post(Config.base_url, auth=HTTPBasicAuth('', Config.pat), headers={'Content-Type': 'application/json'}, data=json.dumps(wiql_query))

# Check if the request was successful
if response.status_code == 200:
    work_items = response.json()['workItems']
    print(f"Found {len(work_items)} work items assigned to {Config.user_email}:")
    for item in work_items:
        #print(f"ID: {item['id']}")
        id = item['id']
        link =  item['url']
        #print(link)


        work_item_response = requests.get(link, auth=HTTPBasicAuth('', Config.pat), headers={'Content-Type': 'application/json'})
        
        if work_item_response.status_code == 200:
                work_item_details = work_item_response.json()
                work_item_title = work_item_details['fields']['System.Title']
                state = work_item_details['fields']['System.State']
          
                print (id, "-",work_item_title, "-", state)

     
        else:
            print(f"Failed to fetch details for work item ID: ")

        
    #print(response.text)
else:
    print(f"Failed to fetch work items: {response.status_code}")
    print(response.text)