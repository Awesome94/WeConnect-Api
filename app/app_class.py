import bcrypt
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
        - business: Businesses' database"""

        self.userdb = [{
            'id': '4',
            'first_name': 'Joy',
            'last_name': 'Chips',
            'email': 'joychips@aol.com',
            'password': 'someonehere'
        }, {
            'id': '3',
            'first_name': 'Mungai',
            'last_name': 'Otieno',
            'email': 'omungai@hotmail.com',
            'password': 'notimetolose'
        }]

        self.business = []

    def register_user(self, user_id, first_name, last_name, email, password):
        """Adds a user to the application
        - user_id: uniquely identifies the user record
        - first_name: Holds the user's first name
        - last_name: Holds the user's last name
        - password: Holds the user's password"""
        for user_record in self.userdb:
            if user_record['email'] == email and user_record['id'] is not None:
                return "You're already registered. Try signing in."

            if email is not None and password is not None:
                user = User(user_id, first_name, last_name, email, password)
                user_password = user.set_password(password)
                new_user = {
                    'id': user.user_id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'password': user_password
                }
                self.userdb.append(new_user)
                return new_user

    def login_user(self, email, password):
        """Logs in users to the application.
        - email: Holds the user's entered e-mail address.
        - password: Holds the user's entered password"""
        for user_record in self.userdb:
            salt = bcrypt.gensalt(16)
            entered_password = bcrypt.hashpw(password, salt)
            user_password = user_record['password']
            user_email = user_record['email']
            if user_email == email and user_password == entered_password:
                user = {
                    'user_id': user_record['id'],
                    'user_email': user_email
                }
                return user
        return False

    def reset_password(self, email, password, new_password):
        """Changes the user's password
        - email: Holds the user's entered e-mail address.
        - password: Holds the user's entered password."""
        for user_record in self.userdb:
            salt = bcrypt.gensalt(16)
            entered_password = bcrypt.hashpw(password, salt)
            user_password = user_record['password']
            user_email = user_record['email']
            if user_email == email and user_password == entered_password:
                old_password = user_password

                if old_password:
                    salt = bcrypt.gensalt(16)
                    user_password = bcrypt.hashpw(new_password, salt)
                    return user_password
        return False

    def create_business(self, business_id, name, location, category, description):
        """Creates a business for the user"""
        if name is None or location is None or category is None or description is None:
            return "Missing Field: Please provide Name & Description."

        business = Business(business_id, name, location, description, category)
        user_business = {
            'id': business.business_id,
            'name': business.name,
            'location': business.location,
            'description': business.description,
            'category': business.category,
            'reviews': []
        }

        self.business.append(user_business)
        return user_business

    def get_businesses(self):
        """Gets all businesses on the application
        for a logged-in user"""
        all_businesses = []
        for item in self.business:
            item1 = item.copy()
            item1.pop('reviews', None)
            all_businesses.append(item1)
        return all_businesses

    def update_business(self,
                        business_id,
                        name=None,
                        location=None,
                        description=None,
                        category=None):
        """Updates an existing business with details provided by the user."""
        if business_id is not None:
            for my_business in self.business:
                for key in my_business.keys():
                    if key == 'id' and my_business[key] == business_id:
                        old_name = my_business['name']
                        old_description = my_business['description']
                        old_location = my_business['location']
                        old_category = my_business['category']
                        business = Business(business_id, old_name, old_description,
                                            old_location, old_category)

                        if old_name is not None:
                            new_name = business.change_name(name)
                            my_business['name'] = new_name

                        if old_location is not None:
                            new_location = business.change_location(location)
                            my_business['location'] = new_location

                        if old_description is not None:
                            new_description = business.change_description(
                                description)
                            my_business['description'] = new_description

                        if old_category is not None:
                            new_category = business.change_category(category)
                            my_business['category'] = new_category

                        return my_business

    def get_business(self, business_id):
        all_businesses = []
        for item in self.business:
            item1 = item.copy()
            item1.pop('reviews', None)
            all_businesses.append(item1)

            for business in all_businesses:
                for key in business.keys():
                    if key == 'id' and business[key] == business_id:
                        return business

    def delete_business(self, business_id):
        """Deletes a business created by the user."""
        if business_id is not None:
            for my_business in self.business:
                if my_business['id'] == business_id:
                    self.business.remove(my_business)
                    return True

    def add_review(self, business_id, review_id, user_review):
        """Adds a review by a user"""
        if business_id is not None:
            for business in self.business:
                for key, value in business.items():
                    if key == 'id' and value == business_id:
                        review = Review(review_id, user_review)
                        new_review = {
                            'id': review.review_id,
                            'review': review.review
                        }
                        business['reviews'].append(new_review)
                        return business

    def get_reviews(self, business_id):
        """Gets all reviews for a single business and
        shows them to a logged-in user."""
        if business_id is not None:
            for business in self.business:
                for business_id in business:
                    return business['reviews']


class User():
    """Basic blueprint of the User class.
    Provides the foundation for how the user interacts
    with the application."""

    def __init__(self, user_id, first_name, last_name, email, password):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def set_password(self, password):
        salt = bcrypt.gensalt(16)
        hashed_password = bcrypt.hashpw(self.password, salt)
        return hashed_password

    def check_password(self, password):
        salt = bcrypt.gensalt(16)
        hashed_password = bcrypt.hashpw(self.password, salt)
        if hashed_password == bcrypt.hashpw(self.password, hashed_password):
            return True
        return False


class Business():
    """Basic blueprint of the Business class.
    Provides the foundation for how the businesses will
    be modeled in with the application."""

    def __init__(self, business_id, name, location, description, category):
        self.business_id = business_id
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
