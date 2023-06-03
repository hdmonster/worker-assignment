import os
import inquirer
from pprint import pprint

from src.services.mail_service import MailService
from src.models.mail import Mail, User


class Compose:
    def __init__(cls, sender):
        os.system("cls")
        """
        # Guide
        1. Initialize sender variable so other methods can access it
        2. Initialize these variables and assign input() function so users can write their own mail
            1) recipient
            2) subject
            3) message

        # Hint
        Use input() function to retrieve input from user

        example
        initialize data --> self.data = data
        input variable --> cls.data = input('Data: ')
        """
        ## Uncommenr these lines
        # INSERT YOUR CODE HERE

        confirm = [
            inquirer.Confirm(
                "send",
                message="Send mail to {}".format(cls.recipient),
                default=True,
            )
        ]

        answer = inquirer.prompt(confirm)
        pprint(answer)

        if answer["send"]:
            mail = Mail(
                sender=User(sender[0], sender[1]),
                recipient=User("", cls.recipient),
                subject=cls.subject,
                message=cls.message,
            )

            MailService.send(mail)
