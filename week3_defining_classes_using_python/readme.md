# Smart Home Device Manager

A small smart home device model built for Week 3 of CSC6301 (Defining Classes Using Java). It demonstrates the core object oriented building blocks: an interface, a superclass, a subclass, inheritance, polymorphism, and encapsulation. The assignment frames each piece against its Java equivalent, since the goal is to map Python class design onto Java class design. An interactive terminal menu lets you drive a smart light through every method.

## Class design

The module defines three classes:

* `Connectable` is an abstract base class that stands in for a Java interface. It declares one abstract method, `connect_to_wifi`, and holds no state. Any class that inherits from it must implement that method or it cannot be instantiated.
* `SmartDevice` is the superclass. It tracks a brand and a power state, starts powered off, and can flip its power with `toggle_power`. It also exposes `get_brand` and `is_power_on`.
* `SmartLight` is the subclass. It inherits from `SmartDevice` and implements `Connectable`, so it gains brand and power behavior, adds a brightness level on a 0 to 100 scale, and provides the concrete `connect_to_wifi` implementation. This is the polymorphism step.

The Java equivalent of the hierarchy is:

```java
public interface Connectable { void connectToWiFi(); }
public class SmartDevice {}
public class SmartLight extends SmartDevice implements Connectable {}
```

Fields use a single leading underscore (`_brand`, `_power_on`, `_brightness_level`) to signal that they are private by convention. Python does not enforce access modifiers the way Java does, so the underscore communicates intent.

## Project structure

```
week3_defining_classes_using_java/
└── shaun_clarke_csc6301/
    ├── smart_device.py            Source (Connectable, SmartDevice, SmartLight, menu)
    ├── smart_device.html          pydoc reference generated from the source
    ├── smart_device.pdf           PDF export of the reference
    ├── smart_device.puml          PlantUML source for the class diagram
    ├── classes_smart_device.png   Rendered UML class diagram
    ├── smart_device.zip           Bundle of the source and its PDF
    └── wee3_discussion.docx        Weekly discussion writeup (not part of the program)
```

## Requirements

* Python 3.9 or newer
* No third party packages to run the program. The standard library `abc` module is used and ships with Python.

## Getting started

Clone the repository and move into the project folder:

```bash
git clone https://github.com/shaunclarke2333/csc6301_software_design_documentation.git
cd csc6301_software_design_documentation/week3_defining_classes_using_java/shaun_clarke_csc6301
```

Run the program:

```bash
python3 smart_device.py
```

## Using the menu

On start you get this menu:

```
--- Smart Light Menu ---
1. Add a smart light
2. Toggle the power
3. Connect to Wi-Fi
4. Set the brightness level
5. Show the light's current state
6. Exit
```

Create a light first with option 1. Options 2 through 5 act on the most recently created light. If you choose one of them before adding a light, the program tells you to add one first and returns you to the menu, so it will not crash.

* Option 1 prompts for a brand and a brightness level, then creates the light.
* Option 2 toggles power on or off and prints the new state.
* Option 3 connects the light to Wi-Fi and prints a confirmation.
* Option 4 prompts for a new brightness level. Valid values are 0 through 100. Anything outside that range is rejected and the brightness is left unchanged.
* Option 5 prints the current brand, power state, and brightness.
* Option 6 exits.

### Example session

```
Choose an option to continue: 1
Enter the light's brand: Philips
Enter the brightness level (0-100): 75

A Philips smart light has been added.

Choose an option to continue: 2
The Philips device is now ON.

Choose an option to continue: 3
The Philips smart light is connecting to Wi-Fi...
Connection successful.

Choose an option to continue: 4
Enter the new brightness level (0-100): 50
Brightness has been updated to 50.

Choose an option to continue: 5
Brand: Philips
Power on: True
Brightness: 50

Choose an option to continue: 6
Goodbye!
```

## Generated documentation

The HTML reference in `smart_device.html` was generated with pydoc. Open it in any browser to read the full documentation for all three classes.

To regenerate it after a code change, run this from inside the project folder:

```bash
python3 -m pydoc -w smart_device
```

## UML diagram

`classes_smart_device.png` shows the class diagram: `SmartLight` inheriting from both `SmartDevice` and `Connectable`, with each class and its members.

The diagram source is `smart_device.puml`, generated from the code with py2puml and rendered to PNG with PlantUML. To regenerate the image from the source, run PlantUML against the puml file:

```bash
plantuml smart_device.puml
```

## Author

Shaun Clarke
CSC6301 Software Design and Documentation