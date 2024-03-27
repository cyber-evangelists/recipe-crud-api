from beanie import Document

class User(Document):  
    name: str               # Required
    email: str              # Required
    password: str           # Required

    class Config: 
        # orm_mode = True
        schema_extra = {
            "example": {
                "name": "example",
                "email": "example@example.com",
                "password": "password"
            }
        }