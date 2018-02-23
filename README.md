# WeConnect-Api
Holds the API for the UI contained within [WeConnect](https://github.com/leni1/WeConnect)

## API should have the following endpoints
Endpoint | Functionality
------------------------
POST /api/auth/register | Creates a user account
POST /api/auth/login | Logs in a user
POST /api/auth/logout | Logs out a user
POST /api/auth/reset-password | Password reset
POST /api/businesses | Register a business
POST /api/businesses/<businessId> | Updates a business profile
DELETE /api//businesses/<businessId> | Remove a business
GET /api/businesses | Retrieves all businesses
GET /api/businesses/<businessId> | Get a business
POST /api/businesses/<businessId> | Add a review for a business
GET /api/businesses/<businessId>/reviews | Get all reviews for a business


