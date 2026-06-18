# Flexible Notification System (SDLC Maintenance Phase)

The Week 5 maintenance release of the flexible notification system from Week 4 of CSC6301 (Software Development Life Cycle). This week exercises the maintenance phase of the SDLC: a new WhatsApp channel is added to the existing system without changing the engine or the interface. The new channel is a separate module that implements the existing contract, so the change is an extension rather than a rewrite. A non interactive demo proves that one alert system can switch across all three channels at runtime with no change to the core.

## What changed from Week 4

* `whatsapp_service.py` is new. It is a `WhatsAppService` channel in its own module.
* `notification_app.py` was updated to wire the WhatsApp channel into the menu.
* `maintenance_demo.py` is new. It proves the maintenance requirement by switching one alert system across all three channels.
* `notification_system.py` (the engine and the `NotificationMedium` interface) was not changed. It is identical to the Week 4 version. That is the point: the system was extended without editing its stable core.

## Class design

The framework is split across modules so the engine and the channels can change independently.

* `NotificationMedium` (in `notification_system.py`) is an abstract base class that acts as the interface every channel must honor. It declares one abstract method, `send(message)`.
* `AlertSystem` (in `notification_system.py`) is the container. It holds one `NotificationMedium` and a running log. `notify_user(message)` delegates delivery to the held channel and records the confirmation. `set_medium(medium)` swaps the active channel at runtime. `get_log()` returns the session log.
* `EmailService` (in `email_service.py`) returns a confirmation prefixed with `[EMAIL]`.
* `SMSService` (in `sms_service.py`) returns a confirmation prefixed with `[SMS]`.
* `WhatsAppService` (in `whatsapp_service.py`) is the maintenance addition. It returns a confirmation prefixed with `[WhatsApp]`.

There are two entry points: `notification_app.py` for the interactive menu, and `maintenance_demo.py` for the automated proof.

## Project structure

```
week5_sdlc/
└── shaun_clarke_csc6301/
    ├── notification_system.py    Engine: NotificationMedium interface and AlertSystem (unchanged from Week 4)
    ├── email_service.py          EmailService channel
    ├── sms_service.py            SMSService channel
    ├── whatsapp_service.py       WhatsAppService channel (new this week)
    ├── notification_app.py       Interactive menu entry point
    ├── maintenance_demo.py       Automated proof that switches all three channels at runtime
    ├── ai_tool_use.zip           Snapshot bundle of the writeup and all source files
    └── requirements.txt          Full environment freeze (see Requirements)
```

## Requirements

* Python 3.9 or newer. The type hints use built in generics such as `list[str]`, which require 3.9 or later.
* No third party packages. The program uses only the Python standard library (the `abc` module), so nothing needs to be installed to run it.
* A `requirements.txt` is included, but it is a full freeze of the development environment rather than the direct dependencies of this project. You do not need to install it to run the program.

## Getting started

Clone the repository and move into the project folder:

```bash
git clone https://github.com/shaunclarke2333/csc6301_software_design_documentation.git
cd csc6301_software_design_documentation/week5_sdlc/shaun_clarke_csc6301
```

Run either entry point from inside that folder, not from the repository root. The modules import each other by name, so they need to be in the current directory.

## Running the program

### Interactive app

```bash
python3 notification_app.py
```

On start you get this menu:

```
Flexible Notification System
1. Send a notification
2. Switch channel (email / sms / whatsapp)
3. Show session log
4. Quit
Choose an option:
```

* Option 1 prompts for a message and sends it over the active channel. An empty message is not sent.
* Option 2 switches the channel. Valid values are `email`, `sms`, and `whatsapp`. Anything else is rejected.
* Option 3 prints the numbered session log, or says it is empty.
* Option 4 quits.

The active channel starts as email.

```
Choose an option: 2
Channel (email / sms / whatsapp): whatsapp
Active channel is now: whatsapp

Choose an option: 1
Message: Your order has shipped
Sent -> [WhatsApp] Sending message: Your order has shipped

Choose an option: 4
Goodbye.
```

### Maintenance demo

This script takes no input. It switches one alert system across all three channels and prints a shared log, which is the proof for the maintenance requirement.

```bash
python3 maintenance_demo.py
```

Output:

```
active = email     -> [EMAIL] Welcome aboard
active = sms       -> [SMS] Your code is 4821
active = whatsapp  -> [WhatsApp] Sending message: Your order has shipped

Session log:
  1. [EMAIL] Welcome aboard
  2. [SMS] Your code is 4821
  3. [WhatsApp] Sending message: Your order has shipped
```

## Generated documentation

`ai_tool_use.pdf` and `ai_tool_use.docx` document how AI tooling was used during development. `ai_tool_use.zip` is a snapshot bundle of that writeup together with every source file in the project.

To generate a pydoc HTML reference for any module, run this from inside the project folder using the module name without the .py extension:

```bash
python3 -m pydoc -w notification_system
```

## Author

Shaun Clarke
CSC6301 Software Design and Documentation