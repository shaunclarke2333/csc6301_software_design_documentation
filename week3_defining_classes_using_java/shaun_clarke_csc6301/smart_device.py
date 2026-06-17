"""Smart device module for the smart home device manager system.

Author: Shaun Clarke
Course: CSC6301
Date: 5/22/2026

I will also preface this by saying copilot is in my IDE so some of this is its suggestion.
No i did not give it any specific prompts. Just accepted or refused its suggestions.

Provides the Connectable interface (modeled as an abstract base
class), the SmartDevice superclass, and the SmartLight subclass for
representing electronic devices in a smart home. SmartDevice tracks
a brand and a power state, and can toggle that power state on or
off. SmartLight extends SmartDevice and implements Connectable to
add brightness control and Wi-Fi connectivity.

In Java this design would use a public interface Connectable, a
public class SmartDevice, and a public class SmartLight, each in
its own file. In Python a single module can hold all three since
the language has no one-public-class-per-file rule.

The Java equivalent of the class hierarchy would be:

    public interface Connectable { void connectToWiFi(); }
    public class SmartDevice {}
    public class SmartLight extends SmartDevice implements Connectable {}

Typical usage would be:
    from smart_device import SmartLight

    light: SmartLight = SmartLight(brand="Philips", brightness_level=75)
    light.toggle_power()
    light.connect_to_wifi()
    light.set_brightness_level(50)

To run interactively:
    python smart_device.py
"""

from abc import ABC, abstractmethod


class Connectable(ABC):
    """
    Interface for any device that can connect to Wi-Fi.

    The connectable class is modeled as a Python abstract base class to mirror
    a Java interface. Any class that inherits from Connectable parent class must
    provide its own implementation of connect_to_wifi, otherwise the child class
    cannot be instantiated.

    Attributes:
        None. Connectable defines behavior, not st  ate.
    """

    @abstractmethod
    def connect_to_wifi(self) -> None:
        """
        Connect the device to a Wi-Fi network.

        This method is an abstract method. Concrete subclasses must override
        it and provide a real implementation. The Java equivalent
        would be:

            void connectToWiFi();

        Returns:
            None
        """

        pass


class SmartDevice:
    """
    Represents a generic electronic device in the smart home.

    This SmartDevice class keeps track of the brand of the device and whether
    it is currently powered on. The power state can be toggled on and off using
    toggle_power. This class is intended to be used as a superclass
    for more specific device types such as SmartLight.

    Attributes:
        brand: str
            The manufacturer or brand of the device.
        power_on: bool
            Current power state of the device. True if the device
            is on, False if it is off.
    """

    def __init__(self, brand: str) -> None:
        """
        Create a new SmartDevice with the given brand.

        The device always starts in the powered-off state.

        Parameters:
            brand : str
                The manufacturer or brand of the device.
        """

        # I use an underscore to mark these as private by
        # convention. Python doesn't really enforce access modifiers like
        # Java's private, but the underscore basically signals the intent.
        self._brand: str = brand
        self._power_on: bool = False

    def toggle_power(self) -> None:
        """
        Toggle the power state of the device.

        If the device is currently off, it will be turned on. If it
        is currently on, it will be turned off. A short status
        message is printed so the user can see what happened.

        Returns:
            None
        """

        # Changing the boolean from true to false is the easiest way to toggle the state
        self._power_on = not self._power_on

        if self._power_on:
            print(f"The {self._brand} device is now ON.")
        else:
            print(f"The {self._brand} device is now OFF.")

    def get_brand(self) -> str:
        """
        Return the brand of the device.

        Returns:
            str
                The brand string that was supplied to the constructor.
        """

        return self._brand

    def is_power_on(self) -> bool:
        """
        Return whether the device is currently powered on.

        Returns:
            bool
                True if the device is on, False otherwise.
        """

        return self._power_on


class SmartLight(SmartDevice, Connectable):
    """
    Represents a Wi-Fi connected smart light bulb.

    This SmartLight class is a SmartDevice that can also connect to Wi-Fi.
    It adds a brightness level on top of the brand and power on
    state that it inherits from the SmartDevice. The brightness is
    measured on a 0 to 100 scale.

    In Java the class declaration would be:

        public class SmartLight extends SmartDevice implements Connectable

    In Python the same relationship is expressed with multiple
    inheritance: SmartDevice first, Connectable second.

    Attributes:
        brand: str
            Inherited from SmartDevice. The manufacturer of the light.
        power_on: bool
            Inherited from SmartDevice. Current power state.
        brightness_level: int
            How bright the light is, on a 0 to 100 scale.
    """

    def __init__(self, brand: str, brightness_level: int) -> None:
        """
        Create a new SmartLight with a brand and brightness level.

        This method calls the SmartDevice constructor with super() so the brand
        and power state are initialized in the superclass. This is
        the Python equivalent of calling super(p_brand) in a Java
        subclass constructor.

        Parameters:
            brand : str
                The manufacturer or brand of the light.
            brightness_level : int
                Initial brightness on a 0 to 100 scale.
        """
        super().__init__(brand)
        self._brightness_level: int = brightness_level

    def connect_to_wifi(self) -> None:
        """
        Connect the smart light to a Wi-Fi network.

        This method provides the concrete implementation of the abstract method
        declared on the Connectable interface. It prints a message
        showing which brand of light is connecting. This is the
        polymorphism step being satisfied.

        Returns:
            None
        """

        print(f"The {self.get_brand()} smart light is connecting to Wi-Fi...")
        print("Connection successful.")

    def set_brightness_level(self, new_level: int) -> bool:
        """
        Update the brightness level of the light.

        The new level must be between 0 and 100 inclusive. If it is
        out of range, the brightness is not changed and the method
        returns False.

        Parameters:
            new_level : int
                The new brightness level on a 0 to 100 scale.

        Returns:
            bool
                True if the brightness was updated, False if the
                requested level was out of range.
        """

        # Validating the brightness range before applying it
        if new_level < 0 or new_level > 100:
            return False

        self._brightness_level = new_level
        return True

    def get_brightness_level(self) -> int:
        """
        Return the current brightness level of the light.

        Returns:
            int
                The current brightness on a 0 to 100 scale.
        """

        return self._brightness_level


def main() -> None:
    """
    Run the interactive SmartLight menu loop.

    This main method displays a menu that lets the user create a SmartLight, toggle
    its power, connect it to Wi-Fi, change its brightness level,
    view its current state, or exit the program. The loop continues
    until the user selects the exit option.

    Notes:
        A SmartLight must be created via option 1 before the other
        options can be used, since those options operate on the
        most recently created SmartLight instance.
    """

    new_light: SmartLight = None

    while True:
        # Display menu
        print("\n--- Smart Light Menu ---")
        print("1. Add a smart light")
        print("2. Toggle the power")
        print("3. Connect to Wi-Fi")
        print("4. Set the brightness level")
        print("5. Show the light's current state")
        print("6. Exit")

        # Get the user's selection
        choice: str = input("\nChoose an option to continue: ").strip()

        # Validating the selection
        if choice == "1":
            # Getting inputs:
            brand: str = input("Enter the light's brand: ")
            brightness_level: int = int(input("Enter the brightness level (0-100): "))

            # Instantiating the SmartLight class
            new_light = SmartLight(brand, brightness_level)
            print(f"\nA {brand} smart light has been added.")

        elif choice == "2":
            if new_light is None:
                print("Please add a smart light first using option 1.")
                continue
            new_light.toggle_power()

        elif choice == "3":
            if new_light is None:
                print("Please add a smart light first using option 1.")
                continue
            new_light.connect_to_wifi()

        elif choice == "4":
            if new_light is None:
                print("Please add a smart light first using option 1.")
                continue
            new_level: int = int(input("Enter the new brightness level (0-100): "))
            change_brightness: bool = new_light.set_brightness_level(new_level)

            if change_brightness:
                print(f"Brightness has been updated to {new_level}.")
            else:
                print("Invalid brightness level. Must be between 0 and 100.")

        elif choice == "5":
            if new_light is None:
                print("Please add a smart light first using option 1.")
                continue
            print(f"\nBrand: {new_light.get_brand()}")
            print(f"Power on: {new_light.is_power_on()}")
            print(f"Brightness: {new_light.get_brightness_level()}")

        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()