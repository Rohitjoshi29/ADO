import requests
from requests.auth import HTTPBasicAuth
import json
import Config  # Import the configuration file

# Function to create a work item
def create_work_item(title, project):
    url = f'{Config.base_url1}/{project}/_apis/wit/workitems/$User%20Story?api-version=6.0'
    print(url)
    headers = {
        'Content-Type': 'application/json-patch+json'
    }
    data = [
        {
            "op": "add",
            "path": "/fields/System.Title",
            "from": None,
            "value": title
        },
        {
            "op": "add",
            "path": "/fields/System.AreaPath",
            "value": "GN\Video Systems\VSSW\Code Wizards"
        },
        {
            "op": "add",
            "path": "/fields/System.IterationPath",
            "value": "GN"
        },
        {
            "op": "add",
            "path": "/relations/-",
            "value": {
                "rel": "System.LinkTypes.Related",
                "url": "https://dev.azure.com/ONEGN/GN/_workitems/21909",
                "attributes": {
                    "comment": "New Onboarding "
                }
            }
        }
    ]

    response = requests.post(url, auth=HTTPBasicAuth('', Config.pat), headers=headers, data=json.dumps(data))

    if response.status_code == 200 or response.status_code == 201:
        work_item = response.json()
        print(f"Work item created successfully. ID: {work_item['id']}, Title: {work_item['fields']['System.Title']}")
    else:
        print(f"Failed to create work item: {response.status_code}")
        print(response.text)

# Main function to get user input and create multiple work items
def main():
    titles = input("Enter the titles of the work items, separated by newlines:\n").split('\n')
    project = "GN" # input("Enter the project name: ")

    for title in titles:
        if title.strip():  # Ensure the title is not empty
            create_work_item(title.strip(), project)

if __name__ == "__main__":
    main()