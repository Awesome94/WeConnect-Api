user_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "user-schema",
    "description": "Schema of post data for creating a new user \
                    in the WeConnect app.",
    "type": "object",
    "properties": {
        "user_id": {
            "type": "string",
            "description": "User's unique id.",
            "maxLength": 255
        },
        "first_name": {
            "type": "string",
            "description": "User's first name",
            "minLength": 3,
            "maxLength": 255,
            "pattern": "^[A-Za-z\\s]*$"
        },
        "last_name": {
            "type": "string",
            "description": "User's last name",
            "minLength": 3,
            "maxLength": 255,
            "pattern": "^[A-Za-z\\s]*$"
        },
        "email": {
            "type": "string",
            "description": "User's e-mail",
            "maxLength": 255
        },
        "password": {
            "type": "string",
            "description": "User's password",
            "minLength": 7,
            "maxLength": 255
        }
    },
    "additionalProperties": False,
    "required": [ "email", "first_name", "last_name", "password"]
}
