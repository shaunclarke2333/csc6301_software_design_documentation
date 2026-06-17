"""WhatsApp delivery channel for the flexible alert system.

Author: Shaun Clarke
Course: CSC6301

Copilot is in my VSCODE editor and i accept and reject it's suggestions as i see fit.

This is the week 5 maintenance addition. A new concrete channel in its own module that
imports and implements the existing NotificationMedium interface. The engine's
AlertSystem and the interface is not changed, so this is an extension rather
than a rewrite.
"""

from notification_system import NotificationMedium

__author__ = "Shaun Clarke"
__version__ = "1.0"


class WhatsAppService(NotificationMedium):
    """Concrete channel that delivers notifications over WhatsApp.
    """

    def send(self, message: str) -> str:
        """Deliver a message over WhatsApp.

        Parameters:
            message (str): The notification text to deliver.

        Returns:
            str: Confirmation that the WhatsApp message was sent.
        """
        return f"[WhatsApp] Sending message: {message}"