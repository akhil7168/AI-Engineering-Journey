from typing import Optional

def find_user(
    user_id:int
) -> Optional[str]:

    users = {
        1:"Akhil"
    }

    return users.get(user_id)

print(find_user(1))
print(find_user(2))