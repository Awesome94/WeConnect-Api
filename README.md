# WeConnect-Api
[![Build Status](https://travis-ci.org/leni1/WeConnect-Api.svg?branch=master)](https://travis-ci.org/leni1/WeConnect-Api/)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/leni1/WeConnect-Api/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/leni1/WeConnect-Api/test_coverage)

Holds the API for the UI contained within [WeConnect](https://github.com/leni1/WeConnect)

## API should have the following endpoints
Endpoint | Functionality
-------- | -------------
POST /api/v1/auth/register | Creates a user account
POST /api/v1/auth/login | Logs in a user
POST /api/v1/auth/logout | Logs out a user
POST /api/v1/auth/reset-password | Password reset
POST /api/v1/businesses | Register a business
PUT /api/v1/businesses/`<businessId>` | Updates a business profile
DELETE /api/v1/businesses/`<businessId>` | Remove a business
GET /api/v1/businesses | Retrieves all businesses
GET /api/v1/businesses/`<businessId>` | Get a business
POST /api/v1/businesses/`<businessId>`/reviews | Add a review for a business
GET /api/v1/businesses/`<businessId>`/reviews | Get all reviews for a business

## Running the API
1. Clone the repo as follows:
`git clone https://github.com/leni1/WeConnect-Api.git`

2. Install `virtualenv` if you don't already have it on your system.
`pip install virtualenv`

3. Change directory to where the API code is located:
`cd WeConnect-Api` or equivalent on your operating system.

4. Create a folder for the API's virtual environment:
`virtualenv your-folder-name`

5. Activate the virtual environment:
`source your-folder-name/bin/activate`

6. Install the API's dependencies:
`pip install -r requirements.txt`

7. Run the API:
`python app.py`

#### Note
This API uses Python 3. It has not been checked for compatibility with Python 2. As such, your mileage may vary.

