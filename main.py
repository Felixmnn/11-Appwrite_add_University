#What a new University needs
"""
 1.University List Entry
        {name: str,
        code: str,
        id: str,
        image: url,
        slang: str,
        facultyListID: str
    }
 2. University Subjects Entry
    {   id: must match facultyListID,
        Bachelor: [Objects],
        Master: [Objects],
        Staatsexamen: [Objects],
        Diplom: [Objects],
        Magister: [Objects],
        Other: [Objects]
    }
 3. Universty Subject Object format
    {
       name: str,
       type: enum('Bachelor', 'Master', 'Staatsexamen', 'Diplom', 'Magister', 'Other'), 
       faculty: str,
       category: str,
    }
Aditional Notes:
- Each Unviersity Subject entry needs a Other option

This script requires a JSON object containing the university and its subjects.
The JSON object should be structured as follows:
    {
    "universities":
        {
            "name": "University Name",
            "code": "UNIV123",
            "id": "univ-123",
            "image": "http://example.com/image.jpg",
            "slang": "UNIV",
            "facultyListID": "faculty-list-123"
        }
        ,
    "subjects": [
        {
            "id": "faculty-list-123",
            "name": "Subject Name",
            "type": "Bachelor",  # or 'Master', 'Staatsexamen', 'Diplom', 'Magister', 'Other'
            "faculty": "Faculty Name",
            "category": "Category Name"
        },
        ...
        ]
    }
"""

import json 
import os 
from appwrite.client import Client
from appwrite.exception import AppwriteException
from appwrite.services.databases import Databases
import uuid
import requests


def url_exists(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False
 

def add_university_to_countryList (country_list_id, university_name, university_code, university_id, university_image, university_slang, faculty_list_id,databases):
    try:
        doc = databases.get_document(
                database_id='YOUR_DATABASE_ID',  
                collection_id='YOUR_COLLECTION_ID',  
                document_id=country_list_id
            )
        databases.create_document(
            database_id='YOUR_DATABASE_ID',  
            collection_id='YOUR_COLLECTION_ID',  
            document_id=country_list_id,
            data={
                "country_list": [doc['country_list'], {
                    "name": university_name,
                    "code": university_code,
                    "id": university_id,
                    "image": university_image,
                    "slang": university_slang,
                    "facultyListID": faculty_list_id
                }]
            }
        )
    except AppwriteException as e:
        print(f"Failed to add University: {e}")


def extract_matching_subjects(type, filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)
    
    matching_subjects = []
    for subject in data['subjects']:
        if subject['type'] == type:
            matching_subjects.append(subject)
    
    return matching_subjects

def add_facultyList_to_appwrite (facultyListID,databases):
    
    try:
        databases.create_document(
            database_id='YOUR_DATABASE_ID',  
            collection_id='YOUR_COLLECTION_ID',  
            document_id=facultyListID,
            data={
                "id": facultyListID,
                "Bachelor": extract_matching_subjects('Bachelor', 'path/to/your/file.json'),
                "Master": extract_matching_subjects('Master', 'path/to/your/file.json'),
                "Staatsexamen": extract_matching_subjects('Staatsexamen', 'path/to/your/file.json'),
                "Diplom": extract_matching_subjects('Diplom', 'path/to/your/file.json'),
                "Magister": extract_matching_subjects('Magister', 'path/to/your/file.json'),
                "Other": extract_matching_subjects('Other', 'path/to/your/file.json'),
            }
        )
        print(f"Faculty List {facultyListID} added successfully.")
    except AppwriteException as e:
        print(f"Failed to add Faculty List: {e}")

def main ():
    client = Client()
    client.set_endpoint(os.getenv('APPWRITE_ENDPOINT'))  
    client.set_project(os.getenv('APPWRITE_PROJECT_ID'))  
    client.set_key(os.getenv('APPWRITE_API_KEY'))  

    databases = Databases(client)

    country_list_id = "THE ID OF THE COUNTRY LIST"
    university_name = "EXAMPLE NAME"
    university_code = "EXAMPLE CODE"
    university_id = uuid.uuid4().hex
    university_image = "http://example.com/image.jpg"
    university_slang = "EXU"
    faculty_list_id = uuid.uuid4().hex


    if not url_exists(university_image):
        print(f"Image URL {university_image} does not exist. Please provide a valid URL.")
        return
    print(f"Adding University: {university_name} with code: {university_code} and id: {university_id}")
    add_facultyList_to_appwrite(country_list_id, university_name, university_code, university_id, university_image, university_slang, faculty_list_id, databases)
    add_university_to_countryList(faculty_list_id, databases)
