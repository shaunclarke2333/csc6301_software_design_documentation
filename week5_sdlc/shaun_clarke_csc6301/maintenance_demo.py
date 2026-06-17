"""Maintenance proof for the Week 5 WhatsApp enhancement.

Author: Shaun Clarke
Course: CSC6301

Copilot is in my VSCODE editor and i accept and reject it's suggestions as i see fit.

Proves the Part 3 requirement: one AlertSystem switches between EmailService,
SMSService, and WhatsAppService at runtime using set_medium(), with no change
to the AlertSystem class or the NotificationMedium interface. Each channel is
imported from its own module; WhatsAppService is the new one. The shared log
captures every message regardless of which channel sent it.

Run from the command line:
    python maintenance_demo.py
"""

from notification_system import AlertSystem, NotificationMedium
from email_service import EmailService
from sms_service import SMSService
from whatsapp_service import WhatsAppService


def main() -> None:
    """
    Switch one AlertSystem across all three channels at runtime via set_medium().
    """
    # This is the same AlertSystem for the whole session. The starting medium does not
    # matter, because every channel below is selected at runtime.
    system: AlertSystem = AlertSystem(EmailService())

    # Each channel is selected the same way: set_medium() at runtime. No change
    # to AlertSystem, just a different object passed in.
    deliveries: list[tuple[str, NotificationMedium, str]] = [
        ("email", EmailService(), "Welcome aboard"),
        ("sms", SMSService(), "Your code is 4821"),
        ("whatsapp", WhatsAppService(), "Your order has shipped"),
    ]

    for name, medium, message in deliveries:
        # swap the active channel at runtime with no change to AlertSystem or NotificationMedium
        system.set_medium(medium)  
        confirmation: str = system.notify_user(message)
        print(f"active = {name:<9} -> {confirmation}")

    # Composition keeps a single log across every channel used this session.
    print("\nSession log:")
    for index, entry in enumerate(system.get_log(), start=1):
        print(f"  {index}. {entry}")


if __name__ == "__main__":
    main()