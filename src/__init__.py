from src.models.mail import User
from src.services.mail_service import MailService
from src.pages.main import Home


name = input("Enter your name: ")
email = input("Enter your email: ")

MailService.setup_user(User(name, email))
MailService.start()

"""
# Guide
Invoke Home class with user as argument.

# Hint
user data type is tuple

example
user = ('vince', 'vince@mail.com')

"""
## Uncomment these lines
# _ = INSERT YOUR CODE HERE
