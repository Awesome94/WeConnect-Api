reset_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "reset_schema",
    "description": "Schema of post data for resetting a password \
                    in the WeConnect app.",
    "type": "object",
    "properties": {
        "user_id": {
            "type": "string",
            "description": "The unique id of user.",
            "maxLength": 255
        },
        "email": {
            "type": "string",
            "description": "The category of the business",
            "maxLength": 255
        },
        "password": {
            "type": "string",
            "description": "The description of the business",
            "maxLength": 255
        },
        "new_password": {
            "type": "string",
            "description": "The location of the business",
            "maxLength": 255
        },
    },
    "additionalProperties": False,
    "required": [ "email", "password", "new_password"]
}