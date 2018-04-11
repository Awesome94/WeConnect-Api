review_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "review-schema",
    "description": "Schema of post data for creating a new review \
                    in the WeConnect app.",
    "type": "object",
    "properties": {
        "business_id": {
            "type": "string",
            "description": "The unique id of the business",
            "maxLength": 255
        },
        "review_id": {
            "type": "string",
            "description": "The description of the business",
            "maxLength": 255
        },
        "review": {
            "type": "string",
            "pattern": "^[A-Za-z\\s]*$"
        }
    },
    "additionalProperties": False,
    "required": ["review"]
}
