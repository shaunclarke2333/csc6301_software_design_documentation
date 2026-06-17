"""SMS delivery channel for the flexible alert system.

Author: Shaun Clarke
Course: CSC6301

Copilot is in my VSCODE editor and i accept and reject it's suggestions as i see fit.

This concrete channel is kept in its own module so it can change without touching the
engine. It imports the NotificationMedium interface and implements it.
"""

from notification_system import NotificationMedium

__author__ = "Shaun Clarke"
__version__ = "1.0"


class SMSService(NotificationMedium):
    """Concrete channel that delivers notifications by SMS.
    """

    def send(self, message: str) -> str:
        """Deliver a message as an SMS text.

        Parameters:
            message (str): The notification text to deliver.

        Returns:
            str: Confirmation that the SMS was sent.
        """
        return f"[SMS] {message}"