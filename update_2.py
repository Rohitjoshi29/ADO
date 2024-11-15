import requests
from requests.auth import HTTPBasicAuth
import json
import Config  # Import the Configuration file

# Function to update a work item
def update_work_item(work_item_id, field, new_value):
    url = f'{Config.base_url1}/_apis/wit/workitems/{work_item_id}?api-version=6.0'
    print(url)
    headers = {
        'Content-Type': 'application/json-patch+json'
    }
    data = [
                
                {
                    "op": "add",
                    "path": "/fields/System.Title",
                    "value": "Updated_title_2"
                },
                {
                    "op": "add",
                    "path": "/relations/-",
                    "value": {
                    "rel": "System.LinkTypes.Related",
                    "url": "https://dev.azure.com/ONEGN/GN/_workitems/11447",
                    "attributes": {
                        "comment": "Making a new link for the test"
                      }
                    }
                }
            ]


    response = requests.patch(url, auth=HTTPBasicAuth('', Config.pat), headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        work_item = response.json()
        print(f"Work item updated successfully. ID: {work_item['id']}")
    else:
        print(f"Failed to update work item: {response.status_code}")
        print(response.text)

# Main function to get user input and update work item
def main():
    work_item_id = input("Enter the ID of the work item: ")
    #field = input("Enter the field to update (e.g., System.Title): ")
    #new_value = input("Enter the new value for the field: ")

    update_work_item(work_item_id, 1, 1)

if __name__ == "__main__":
    main()