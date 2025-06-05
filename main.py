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
