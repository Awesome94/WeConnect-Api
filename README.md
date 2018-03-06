# WeConnect-Api
[![Build Status](https://travis-ci.org/leni1/WeConnect-Api.svg?branch=master](https://travis-ci.org/leni1/WeConnect-Api/)

Holds the API for the UI contained within [WeConnect](https://github.com/leni1/WeConnect)

## API should have the following endpoints
Endpoint | Functionality
-------- | -------------
POST /api/v1/auth/register | Creates a user account
POST /api/v1/auth/login | Logs in a user
POST /api/v1/auth/logout | Logs out a user
POST /api/v1/auth/reset-password | Password reset
POST /api/v1/businesses | Register a business
POST /api/v1/businesses/`<businessId>` | Updates a business profile
DELETE /api/v1/businesses/`<businessId>` | Remove a business
GET /api/v1/businesses | Retrieves all businesses
GET /api/v1/businesses/`<businessId>` | Get a business
POST /api/v1/businesses/`<businessId>`/reviews | Add a review for a business
GET /api/v1/businesses/`<businessId>`/reviews | Get all reviews for a business


