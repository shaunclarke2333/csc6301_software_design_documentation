"""Interactive driver for the flexible notification system.

Author: Shaun Clarke
Course: CSC6301

Copilot is in my VSCODE editor and i accept and reject it's suggestions as i see fit.

This is the program entry point. It wires the concrete channels to one
AlertSystem and offers a menu to send messages, switch the active channel at
runtime, and print the session log. The engine and channels are imported from
their own modules, so adding a channel here does not require editing them.

Run from the command line:
    python notification_app.py
"""

from notification_system import AlertSystem, NotificationMedium
from email_service import EmailService
from sms_service import SMSService


def main() -> None:
    """Run an interactive menu demonstrating the notification system.

    The menu lets the user switch the active channel, send messages, and
    print the session log, showing that delivery behavior changes at
    runtime without any change to AlertSystem.
    """
    # Building the channels once and reusing them as the active medium is swapped.
    channels: dict[str, NotificationMedium] = {
        "email": EmailService(),
        "sms": SMSService(),
    }
    system: AlertSystem = AlertSystem(channels["email"])
    active_name: str = "email"

    menu: str = (
        "\nFlexible Notification System\n"
        "1. Send a notification\n"
        "2. Switch channel (email / sms)\n"
        "3. Show session log\n"
        "4. Quit\n"
        "Choose an option: "
    )

    while True:
        choice: str = input(menu).strip()

        if choice == "1":
            message: str = input("Message: ").strip()
            if message:
                confirmation: str = system.notify_user(message)
                print(f"Sent -> {confirmation}")
            else:
                print("Nothing to send.")

        elif choice == "2":
            name: str = input("Channel (email / sms): ").strip().lower()
            if name in channels:
                system.set_medium(channels[name])
                active_name = name
                print(f"Active channel is now: {active_name}")
            else:
                print("Unknown channel. Use 'email', or 'sms'.")

        elif choice == "3":
            session_log: list[str] = system.get_log()
            if session_log:
                print(f"\nSession log ({len(session_log)} message(s)):")
                for index, entry in enumerate(session_log, start=1):
                    print(f"  {index}. {entry}")
            else:
                print("Log is empty.")

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Choose 1-4.")


if __name__ == "__main__":
    main()