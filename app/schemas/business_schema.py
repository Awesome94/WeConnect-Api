business_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "business-schema",
    "description": "Schema of post data for creating a new business \
                    in the WeConnect app.",
    "type": "object",
    "properties": {
        "business_id": {
            "type": "string",
            "description": "The unique id of the business",
            "maxLength": 255
        },
        "user_id": {
            "type": "string",
            "description": "The unique id of user.",
            "maxLength": 255
        },
        "name": {
            "type": "string",
            "description": "The name of the business",
            "maxLength": 255
        },
        "location": {
            "type": "string",
            "description": "The location of the business",
            "maxLength": 255
        },
        "category": {
            "type": "string",
            "description": "The category of the business",
            "maxLength": 255
        },
        "description": {
            "type": "string",
            "description": "The description of the business",
            "maxLength": 255
        },
        "review": {
            "type": "array"
        }
    },
    "additionalProperties": False,
    "required": [ "name", "location", "category", "description"]
}
