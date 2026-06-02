from typing import List
from typing import Dict
from typing import Optional

students: List[Dict[str,str]] = []

def add_student(
    name:str,
    college:str
) -> None:

    students.append(
        {
            "name":name,
            "college":college
        }
    )

def find_student(
    name:str
) -> Optional[Dict[str,str]]:

    for student in students:

        if student["name"] == name:

            return student

    return None

add_student(
    "Akhil",
    "CVR"
)

print(
    find_student(
        "Akhil"
    )
)