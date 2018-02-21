"""This contains the WeConnect, User, and Business classes.
The WeConnect class acts as the main class, handling
the interactions of the user with the application by
utilizing the other classes defined here."""

class WeConnect():
    """Overall application class.
    Manages the other classes"""

    def __init__(self):
        self.userdb = {}
        self.business = {}
        self.reviews = {}

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

    def create_business(self, name, location, category, user_email):
        if name is None or location is None or category is None:
            return "Missing Field: Please provide Name & Description."

        if user_email not in self.userdb:
            return "You cannot create a business. Register or Login"

        business = Business(name, description, user_email)
        if user_email in self.business:
            user_business = self.business[user_email]

            for biz in user_business:
                if biz.name.lower() == name.lower():
                    return "This business already exists. Try updating it or create a new business."
            user_business.append(business)
        else:
            self.business[user_email] = [business]

        return business

    def update_business(self, id, user_email, name=None, description=None):
        if user_email not in self.business:
            return "You haven't created this business."

        if id is not None:
            user_business = self.business[user_email]
            change_business = user_business[id]

            if name is not None:
                change_business.set_name(name)

            if description is not None:
                change_business.set_description(description)

            self.business[user_email][id] = change_business
            return True

        return False

    def get_businesses(self, id, user_email):
        if user_email not in self.userdb:
            raise Exception("Not Logged In.")

        if id is not None:
            all_businesses = self.business
            return all_businesses[id]

    def delete_business(self, id, user_email):
        if user_email not in self.business:
            return "The business you're trying to delete doesn't exist"

        if len(self.business[user_email]) > id:
            self.business[user_email].pop(id)
            return True

        return "The business you're trying to delete doesn't exist"

    def add_review(self, name, id, user_email, review):
        if user_email not in self.userdb:
            return "User doesn't exist"

        if id is not None and name in self.business:
            review_business = self.business[id]
            self.reviews.update(review, review_business)

    def get_reviews(self, name, id, user_email, reviews):
        if user_email not in self.userdb:
            return "User doesn't exist."

        if id is not None and name in self.business:
            review_business = self.business[id]
            reviews = self.reviews
            return reviews[review_business]

class User():
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_email(self):
        return self.email

    def verify_credentials(self, email, password):
        if email == self.email and password == self.password:
            return True

        return False

class Business():
    def __init__(self, name, description, user_id):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.businesses = []
        self.business_reviews = []

    def change_name(self, new_name):
        self.name = new_name

    def change_description(self, new_description):
        self.description = new_description

    def get_all_reviews(self):
        return self.business_reviews

    def get_all_businesses(self):
        return self.businesses

    def get_business(self, id):
        if len(self.businesses) > id:
            return self.businesses[id]