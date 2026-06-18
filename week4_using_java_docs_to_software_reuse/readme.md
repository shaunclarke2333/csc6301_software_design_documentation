# Flexible Notification System

A multi module notification framework built for Week 4 of CSC6301 (Using Java Docs to Software Reuse). It is built on composition rather than inheritance: a stable engine holds a swappable delivery channel and delegates to it, so the active channel can be changed at runtime without touching the engine. Each channel lives in its own module, which is what makes the channels reusable and replaceable. An interactive terminal menu lets you send messages, switch channels, and view the session log.

## Class design

The framework is split across modules so the engine and the channels can change independently.

* `NotificationMedium` (in `notification_system.py`) is an abstract base class that acts as the interface every channel must honor. It declares one abstract method, `send(message)`. The engine depends on this abstraction, not on any concrete channel.
* `AlertSystem` (in `notification_system.py`) is the container. It holds one `NotificationMedium` and a running log. `notify_user(message)` delegates delivery to the held channel and records the confirmation. `set_medium(medium)` swaps the active channel at runtime. `get_log()` returns the session log. AlertSystem never knows which concrete channel it holds, which is the point of composition.
* `EmailService` (in `email_service.py`) is a concrete channel. Its `send` returns a confirmation prefixed with `[EMAIL]`.
* `SMSService` (in `sms_service.py`) is a concrete channel. Its `send` returns a confirmation prefixed with `[SMS]`.
* `notification_app.py` is the entry point. It wires the channels into one `AlertSystem` and runs the menu.

Because each channel is its own module that imports only the `NotificationMedium` interface, you can add or change a channel without editing the engine. See Adding a channel below.

## Project structure

```
week4_using_java_docs_to_software_reuse/
└── shaun_clarke_csc6301/
    ├── notification_system.py        Engine: NotificationMedium interface and AlertSystem
    ├── email_service.py              EmailService channel
    ├── sms_service.py                SMSService channel
    ├── notification_app.py           Entry point with the interactive menu
    ├── notification_system_uml.pdf   UML diagram of the design
    ├── notification_system.zip       Bundle of the engine source, its pydoc HTML, and the UML PDF
    └── requirements.txt              Full environment freeze (see Requirements)
```

## Requirements

* Python 3.9 or newer. The type hints use built in generics such as `list[str]`, which require 3.9 or later.
* No third party packages. The program uses only the Python standard library (the `abc` module), so nothing needs to be installed to run it.
* A `requirements.txt` is included, but it is a full freeze of the development environment rather than the direct dependencies of this project. You do not need to install it to run the program.

## Getting started

Clone the repository and move into the project folder:

```bash
git clone https://github.com/shaunclarke2333/csc6301_software_design_documentation.git
cd csc6301_software_design_documentation/week4_using_java_docs_to_software_reuse/shaun_clarke_csc6301
```

Run the program from inside that folder:

```bash
python3 notification_app.py
```

Run it from inside the folder, not from the repository root. The modules import each other by name (for example `from notification_system import AlertSystem`), so they need to be in the current directory.

## Using the menu

On start you get this menu:

```
Flexible Notification System
1. Send a notification
2. Switch channel (email / sms)
3. Show session log
4. Quit
Choose an option:
```

* Option 1 prompts for a message and sends it over the active channel, then prints the confirmation. An empty message is not sent.
* Option 2 prompts for a channel name. Valid values are `email` and `sms`. Anything else is rejected and the active channel is left unchanged.
* Option 3 prints the session log, numbered in the order the messages were sent. If nothing has been sent, it says the log is empty.
* Option 4 quits.

The active channel starts as email.

### Example session

```
Choose an option: 1
Message: Server back online
Sent -> [EMAIL] Server back online

Choose an option: 2
Channel (email / sms): sms
Active channel is now: sms

Choose an option: 1
Message: Disk at 90 percent
Sent -> [SMS] Disk at 90 percent

Choose an option: 3

Session log (2 message(s)):
  1. [EMAIL] Server back online
  2. [SMS] Disk at 90 percent

Choose an option: 4
Goodbye.
```

## Adding a channel

The design is meant to be extended without editing the engine. To add a channel:

1. Create a new module, for example `whatsapp_service.py`.
2. Define a class that inherits from `NotificationMedium` and implements `send(self, message: str) -> str`.
3. In `notification_app.py`, import the new class and add an instance to the `channels` dictionary.

No change to `notification_system.py` is required, which is the reuse goal of the assignment.

## Generated documentation

The UML diagram in `notification_system_uml.pdf` and `notification_system_uml.docx` documents the class relationships and the composition design.

A pydoc HTML reference for the engine is included inside `notification_system.zip`. To regenerate a pydoc reference for any module after a code change, run this from inside the project folder using the module name without the .py extension:

```bash
python3 -m pydoc -w notification_system
```

## Author

Shaun Clarke
CSC6301 Software Design and Documentation