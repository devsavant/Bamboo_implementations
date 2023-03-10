# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:23:59 2022

@author: RichieHeredia Devsavant
"""  
# Almacenar los campos que lee cada Webhook para que pueda ser escalable.        
import requests
TOKEN = 'token'
out_url = 'https://1a69-181-58-38-151.ngrok.io'

 # Webhook number 7
url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/webhooks/7/"

payload = {
    "monitorFields": ['employeeNumber'],
    "postFields": {'employeeNumber':'employeeNumber', "hireDate":"hireDate", 
                   "terminationDate":"terminationDate", 'status':'status', 
                   'gender':'gender', 'workEmail':'workEmail' ,
                   'mobilePhone': 'mobilePhone', 'workPhone':'workPhone',
                   'firstName':'firstName', 'lastName':'lastName','location':'location', 
                   'dateOfBirth':'dateOfBirth', 'customNationalID#':'customNationalID#'},
    "name": "Webhook-create",
    "url": out_url + str('/create'),
    "format": "json"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}
response = requests.put(url,
                        auth=(TOKEN, 'DevSavant'), 
                        headers=headers, json=payload)
print(response.text)

# Webhook number 8 - Tabla Employee

url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/webhooks/8/"
payload = {
    "monitorFields":  ['hireDate', 'status','gender', 'terminationDate', 'customNationalID#',
                       'workEmail','mobilePhone','workPhone',
                       'firstName','lastName', 'location','dateOfBirth'],
    
    "postFields": {"hireDate":"hireDate", "terminationDate":"terminationDate", 
                   'status':'status', 'gender':'gender', 'workEmail':'workEmail' ,
                   'mobilePhone': 'mobilePhone', 'workPhone':'workPhone',
                   'firstName':'firstName', 'customNationalID#':'customNationalID#', 
                   'lastName':'lastName','location':'location', 
                   'dateOfBirth':'dateOfBirth'},
    
    "name": "Webhook-employee",
    "url": out_url + str('/updateEmployee'),
    "format": "json"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}
response = requests.put(url,
                        auth=(TOKEN, 'DevSavant'), 
                        headers=headers, json=payload)
print(response.text)

url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/webhooks/"
payload = {
    "monitorFields":  ['customNetPayments1','customCompanyCost1',
                       'customSalary','customGrossCompensation',
                       'customPaySchedule'],
    
    "postFields": {"customNetPayments1":"customNetPayments1", 
                   "customCompanyCost1":"customCompanyCost1", 
                   'customSalary':'customSalary', 
                   'customGrossCompensation':'customGrossCompensation', 
                   'customPaySchedule':'customPaySchedule' },
    "name": "Webhook-money",
    "url": url_out + str('/updateCPA'),
    "format": "json"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}
response = requests.post(url,
                        auth=(TOKEN, 'DevSavant'), 
                        headers=headers, json=payload)
print(response.text)


#%% Update Webhook

url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/webhooks/6/"

payload = {
    "monitorFields": ["division", "jobTitle"],
    "postFields": {"division": "division",
                   'jobTitle':'jobTitle',
                   'employeeNumber':'employeeNumber'},
    "name": "basic",
    "url": "https://0c73-181-58-38-151.ngrok.io",
    "format": "json"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
}

response = requests.put(url, 
                        auth=(TOKEN, 'DevSavant'),
                        json=payload, headers=headers)

print(response.text)



#%% GEt DevSavant fields
url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/meta/tables/"

headers = {
    "Accept": "application/json"
}

response = requests.get(url, 
                        auth=(TOKEN, 'DevSavant'),
                        headers=headers)
fields = response.json()

tables = {}
for x in range(len(fields)):
    dict_tempo = {}
    for j in fields[x]['fields']:
        dict_tempo[j['alias']] = j['name']
    tables[str(fields[x]['alias'])] = dict_tempo
