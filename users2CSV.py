#!/usr/local/bin/python3.6
# Author: Franklin E.
# Description: Uses MobileIron's API to retrieve list of users in JSON format and converts the output to CSV. NOTE: An administrator account is required to export information.
import requests, json, csv

# Script variables.
miclouduser="<USERNAME>"
micloudpass="<PASSWORD>"
micloudcluster="https://<CLUSTER>.mobileiron.com"
exportfilepath="/home/<USER>/miCloudUsers.csv"

# Call API.
headers = "Accept: application/json, text/plain, */*"
apicall = requests.get(micloudcluster + '/api/v1/account', auth=(miclouduser, micloudpass), params=headers)

# Load JSON data.
jsondata = json.loads(apicall.text)

# Open CSV file.
csvfile = open(exportfilepath, 'w')

# CSV Writer Object.
csvwriter = csv.writer(csvfile)

count = 0
userList = {}

# Process JSON data -> CSV
for user in jsondata['result']['searchResults']:
    if count == 0:
        header = 'id','createdAt','uid','emailAddress','accountSource','inviteState','inviteResendCount','accountType','enabled','locked'
        csvwriter.writerow(header)
        count += 1
    userList['id'] = user['id']
    userList['createdAt'] = user['createdAt']
    userList['uid'] = user['uid']
    userList['emailAddress'] = user['emailAddress']
    userList['accountSource'] = user['accountSource']
    userList['inviteState'] = user['inviteState']
    userList['inviteResendCount'] = user['inviteResendCount']
    userList['accountType'] = user['accountType']
    userList['enabled'] = user['enabled']
    userList['locked'] = user['locked']
    csvwriter.writerow(userList.values())

# Close file
csvfile.close()
