"""Notification system engine for the flexible alert system.

Author: Shaun Clarke
Course: CSC6301

Copilot is in my VSCODE editor and i accept and reject it's suggestions as i see fit.
So yes copilot is helping me write this code, but i am the one who is ultimately responsible for the final product.

This module holds the stable core of the framework, built on composition
rather than inheritance: the NotificationMedium interface (an abstract base
class) that every delivery channel implements, and the AlertSystem container.
AlertSystem holds a single NotificationMedium and delegates delivery to it, so
the active channel can be swapped at runtime without touching AlertSystem
itself.

Each concrete channel (EmailService, SMSService, WhatsAppService) lives in its
own module and implements this interface. Keeping the channels separate from
the engine means a channel can be added or changed without editing this file,
which keeps changes isolated and lowers the risk of regression errors.

Typical usage would be:
    from notification_system import AlertSystem
    from email_service import EmailService
    from sms_service import SMSService

    system: AlertSystem = AlertSystem(EmailService())
    system.notify_user("Server back online")

    system.set_medium(SMSService())
    system.notify_user("Disk usage at 90 percent")

    log: list[str] = system.get_log()
"""

from abc import ABC, abstractmethod

__author__ = "Shaun Clarke"
__version__ = "1.0"


class NotificationMedium(ABC):
    """Interface for any channel that can deliver a notification.

    This class behaves like a contract every delivery channel must honor. The AlertSystem
    depends on this abstraction, not on any concrete channel, which is what
    lets the channels be swapped freely at runtime.
    """

    @abstractmethod
    def send(self, message: str) -> str:
        """Deliver a single message over this channel.

        Parameters:
            message (str): The notification text to deliver.

        Returns:
            str: A human readable confirmation describing what was sent.
        """
        raise NotImplementedError


class AlertSystem:
    """Container that delegates notification delivery to a swappable medium.

    AlertSystem owns a NotificationMedium and a running log of every message
    sent during the session. It never knows or cares which concrete channel
    it holds, which is the point of buiding in the behavior rather than
    inheriting it.

    Attributes:
        medium (NotificationMedium): The channel currently used for delivery.
        log (list[str]): An ordered record of every message sent this session.
    """

    def __init__(self, medium: NotificationMedium) -> None:
        """Create an alert system with an initial delivery channel.

        Parameters:
            medium (NotificationMedium): The channel to start with.
        """
        self.medium: NotificationMedium = medium
        self.log: list[str] = []

    def set_medium(self, medium: NotificationMedium) -> None:
        """Swap the active delivery channel.

        Parameters:
            medium (NotificationMedium): The channel to switch to.
        """
        self.medium = medium

    def notify_user(self, message: str) -> str:
        """Send a message over the active channel and record it in the log.

        Parameters:
            message (str): The notification text to deliver.

        Returns:
            str: The confirmation returned by the active channel.
        """
        confirmation: str = self.medium.send(message)
        self.log.append(confirmation)
        return confirmation

    def get_log(self) -> list[str]:
        """Return the full session log of sent messages.

        Returns:
            list[str]: Every confirmation recorded, in the order it was sent.
        """
        return self.log