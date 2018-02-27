"""This contains the WeConnect, User, and Business classes.
The WeConnect class acts as the main class, handling
the interactions of the user with the application by
utilizing the other classes defined here."""

class WeConnect():
    """Overall application class.
    Manages the other classes"""
    def __init__(self):
        """
        - userdb: User database.
        - business: Businesses' database
        - reviews: Reviews' database"""

        self.userdb = [
            {
                'id': '4',
                'first_name': 'Joy',
                'last_name': 'Chips',
                'email': 'joychips@aol.com',
                'password': 'someonehere'
            },
            {
                'id': '3',
                'first_name': 'Mungai',
                'last_name': 'Otieno',
                'email': 'omungai@hotmail.com',
                'password': 'notimetolose'
            }
        ]

        self.business = [
            {
                'id': 1,
                'name': 'Joy Salon',
                'description': 'Unisex Hairdresses',
                'location': 'Wakiso',
                'category': 'Hair'
            },
            {
                'id': 2,
                'name': 'Karunhanga & Sons Hardware Store',
                'description': 'We deal in hardware of all kinds',
                'location': 'Kitojo',
                'category': 'Hardware'
            },
            {
                'id': 3,
                'name': 'Psalms Grocery',
                'description': 'We deal in hardware of all kinds',
                'location': 'Kisaasi',
                'category': 'Hardware'
            }
        ]

        self.reviews = {
            1: {
                1: 'great business',
                2: 'my head got burnt!'
            },
            2: {
                1: 'Great hardware at a cheap price',
                2: 'quality of hardware could improve'
            }
        }

    def register_user(self, first_name, last_name, email, password, confirm_password):
        """Adds a user to the application
        - first_name: Holds the user's first name
        - last_name: Holds the user's last name
        - password: Holds the user's password
        - confirm_password: Holds the second entry of the password
        by the user."""
        if email in self.userdb:
            return "You're already registered. Try signing in."
        else:
            if password != confirm_password:
                return "Sorry, the two passwords don't match. Try again. "
            elif email is not None and password is not None:
                user = User(first_name, last_name, email, password)
                self.userdb[email] = user
                return user

    def login_user(self, email, password):
        """Logs in users to the application.
        - email: Holds the user's entered e-mail address.
        - password: Holds the user's entered password"""
        if email not in self.userdb:
            return "You don't have an account. Please register."
        user = self.userdb[email]

        if user.verify_credentials(email, password) is False:
            return "Wrong e-mail and/or password."

        return True

    def create_business(self, id, name, location, category, description):
        """Creates a business for the user"""
        if name is None or location is None or category is None or description is None:
            return "Missing Field: Please provide Name & Description."

        business = Business(id, name, location, description, category)
        user_business = {
            'id': business.id,
            'name': business.name,
            'location': business.location,
            'description': business.description,
            'category': business.category
        }

        self.business.append(user_business)
        return user_business

    def get_businesses(self):
            """Gets all businesses on the application
            for a logged-in user"""
            all_businesses = self.business
            return all_businesses


    def update_business(self, id, name=None, location=None, description=None, category=None):
        """Updates an existing business with details provided by the user."""
        if id is not None:
            for my_business in self.business:
                for key in my_business.keys():
                    if key == 'id' and my_business[key] == id:
                        old_name = my_business['name']
                        old_description = my_business['description']
                        old_location = my_business['location']
                        old_category = my_business['category']
                        business = Business(id, old_name, old_description, old_location, old_category)

                        if old_name is not None:
                            new_name = business.change_name(name)
                            my_business['name'] = new_name

                        if old_location is not None:
                            new_location = business.change_location(location)
                            my_business['location'] = new_location

                        if old_description is not None:
                            new_description = business.change_description(description)
                            my_business['description'] = new_description

                        if old_category is not None:
                            new_category = business.change_category(category)
                            my_business['category'] = new_category

                        return my_business

    def get_business(self, id):
        for business in self.business:
            for key in business.keys():
                if key == 'id' and business[key] == id:
                    return business

    def delete_business(self, id):
        """Deletes a business created by the user."""
        if id is not None:
            for my_business in self.business:
                for key, value in my_business.items():
                    if key == 'id' and value == id:
                        business = self.business
                        business.remove(my_business)
                        return True


    def add_review(self, business_id, id, user_review):
        """Adds a review by a user"""
        if business_id is not None:
            for business in self.business:
                for key, value in business.items():
                    if key == 'id' and value == business_id:
                        review = Review(id, user_review)
                        new_review = {
                                'id': review.review_id,
                                'review': review.review
                            }

                        self.reviews.update({business_id: new_review})
                        return {business_id: new_review}

    def get_reviews(self, business_id):
        """Gets all reviews for a single business and
        shows them to a logged-in user."""
        if business_id is not None:
            for biz_id in self.reviews:
                if business_id == biz_id:
                    return self.reviews[biz_id]

class User():
    """Basic blueprint of the User class.
    Provides the foundation for how the user interacts
    with the application."""
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_email(self):
        """Returns user email"""
        return self.email

    def verify_credentials(self, email, password):
        """Checks that the user email and password match
        what is in the user database"""
        if email == self.email and password == self.password:
            return True

        return False

class Business():
    """Basic blueprint of the Business class.
    Provides the foundation for how the businesses will
    be modeled in with the application."""
    def __init__(self, id, name, location, description, category):
        self.id = id
        self.name = name
        self.location = location
        self.description = description
        self.category = category

    def change_name(self, new_name):
        """Changes business name."""
        self.name = new_name
        return new_name

    def change_description(self, new_description):
        """Changes business description"""
        self.description = new_description
        return new_description

    def change_location(self, new_location):
        """Changes business name."""
        self.name = new_location
        return new_location

    def change_category(self, new_category):
        """Changes business description"""
        self.category = new_category
        return new_category

class Review():
    def __init__(self, review_id, review):
        self.review = review
        self.review_id = review_id