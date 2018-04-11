reset_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "reset_schema",
    "description": "Schema of post data for resetting a password \
                    in the WeConnect app.",
    "type": "object",
    "properties": {
        "email": {
            "type": "string",
            "description": "User's e-mail address",
            "maxLength": 255
        },
        "password": {
            "type": "string",
            "description": "User's password",
            "maxLength": 255
        },
        "new_password": {
            "type": "string",
            "description": "User's new password",
            "minLength": 7,
            "maxLength": 255
        },
    },
    "additionalProperties": False,
    "required": [ "email", "password", "new_password"]
}