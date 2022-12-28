class LED:
    """The LED object controls an individual LED (Light Emitting Diode)"""

    def __init__(self, id:int) -> None:
        """Create an LED object associated with the given LED, id is the LED number, 1-4.
        1: Red
        2: Green
        3: Blue
        4: IR
        """

    def off(self) -> None: "Turn the LED off."

    def on(self) -> None: "Turn the LED on, to maximum intensity."

    def toggle(self) -> None: "Toggle the LED between on (maximum intensity) and off. If the LED is at non-zero intensity then it is considered “on” and toggle will turn it off."

