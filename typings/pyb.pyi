from typing import Optional, Any, Union
from typing_extensions import TypeAlias

from pyb_i2c import *
from pyb_spi import *
from pyb_uart import *
from pyb_usbvcp import *
from pyb_led import *

hid_type: TypeAlias = int

# Time related functions¶
def delay(ms: int) -> None: "Delay for the given number of milliseconds."

def udelay(us: int) -> None: "Delay for the given number of microseconds."

def millis() -> int: """Returns the number of milliseconds since the board was last reset.

    The result is always a MicroPython smallint (31-bit signed number), so after 2^30 milliseconds (about 12.4 days) this will start to return negative numbers.

    Note that if pyb.stop() is issued the hardware counter supporting this function will pause for the duration of the “sleeping” state. This will affect the outcome of pyb.elapsed_millis()."""

def micros() -> int: """Returns the number of microseconds since the board was last reset.

    The result is always a MicroPython smallint (31-bit signed number), so after 2^30 microseconds (about 17.8 minutes) this will start to return negative numbers.

    Note that if pyb.stop() is issued the hardware counter supporting this function will pause for the duration of the “sleeping” state. This will affect the outcome of pyb.elapsed_micros()."""

def elapsed_millis(start: int) -> int: """Returns the number of milliseconds which have elapsed since start.

    This function takes care of counter wrap, and always returns a positive number. This means it can be used to measure periods up to about 12.4 days.

    Example:

    start = pyb.millis()
    while pyb.elapsed_millis(start) < 1000:
        # Perform some operation"""

def elapsed_micros(start: int) -> int: """Returns the number of microseconds which have elapsed since start.

    This function takes care of counter wrap, and always returns a positive number. This means it can be used to measure periods up to about 17.8 minutes.

    Example:

    start = pyb.micros()
    while pyb.elapsed_micros(start) < 1000:
        # Perform some operation
        pass"""

# Reset related functions¶
def hard_reset() -> None: "Resets the OpenMV Cam in a manner similar to pushing the external RESET button."

def bootloader() -> None: "Activate the bootloader without BOOT* pins."

def fault_debug(value: bool) -> None: """Enable or disable hard-fault debugging. A hard-fault is when there is a fatal error in the underlying system, like an invalid memory access.

    If the value argument is False then the board will automatically reset if there is a hard fault.

    If value is True then, when the board has a hard fault, it will print the registers and the stack trace, and then cycle the LEDs indefinitely.

    The default value is disabled, i.e. to automatically reset."""

# Interrupt related functions¶
def disable_irq() -> None: """Disable interrupt requests. Returns the previous IRQ state: False/True for disabled/enabled IRQs respectively. This return value can be passed to enable_irq to restore the IRQ to its original state."""

def enable_irq(state: Optional[bool] = ...) -> None: """Enable interrupt requests. If state is True (the "default value) then IRQs are enabled. If state is False then IRQs are disabled. The most common use of this function is to pass it the value returned by disable_irq to exit a critical section."""

# Power related functions¶
def wfi() -> None: """Wait for an internal or external interrupt.

    This executes a wfi instruction which reduces power consumption of the MCU until any interrupt occurs (be it internal or external), at which point execution continues. Note that the system-tick interrupt occurs once every millisecond (1000Hz) so this function will block for at most 1ms."""

def stop() -> None: """Put the OpenMV Cam in a “sleeping” state.

    This reduces power consumption to less than 500 uA. To wake from this sleep state requires an external interrupt or a real-time-clock event. Upon waking execution continues where it left off.

    See rtc.wakeup() to configure a real-time-clock wakeup event."""

def standby() -> None: """Put the OpenMV Cam into a “deep sleep” state.

    This reduces power consumption to less than 50 uA. To wake from this sleep state requires a real-time-clock event. Upon waking the system undergoes a hard reset.

    See rtc.wakeup() to configure a real-time-clock wakeup event."""

# Miscellaneous functions¶
def have_cdc() -> bool: """Return True if USB is connected as a serial device, False otherwise.

    Note

    This function is deprecated. Use pyb.USB_VCP().isconnected() instead."""

def hid(arg: tuple[list[Any], float, float, float]) -> None: """Takes a 4-tuple (or list) and sends it to the USB "host (the PC) to signal a HID mouse-motion event.

    Note

    This function is deprecated. Use pyb.USB_HID.send() instead."""

def info(dump_alloc_table: Optional[bool] = ...) -> None: "Print out lots of information about the board."

def main(filename: str) -> None: """Set the filename of the main script to run after boot.py "is finished. If this function is not called then the default file main.py will be executed.

    It only makes sense to call this function from within boot.py."""

def repl_uart(uart: UART) -> None: "Get or set the UART object where the REPL is repeated on."

def rng() -> int: "Return a 30-bit hardware generated random number."

def sync() -> None: "Sync all file systems."

def unique_id() -> str: "Returns a string of 12 bytes (96 bits), which is the unique ID of the MCU."

def usb_mode(modestr: Optional[str] = ..., port: Optional[int] = ..., vid:Optional[int] = ..., pid:Optional[int] = ..., msc:Optional[Any] = ..., hid: Optional[hid_type] = ..., high_speed:Optional[bool] = ...) -> Optional[str]: """If called with no arguments, return the current USB mode as a string.

    If called with modestr provided, attempts to configure the USB mode. The following values of modestr are understood:

        None: disables USB

        'VCP': enable with VCP (Virtual COM Port) interface

        'MSC': enable with MSC (mass storage device class) interface

        'VCP+MSC': enable with VCP and MSC

        'VCP+HID': enable with VCP and HID (human interface device)

        'VCP+MSC+HID': enabled with VCP, MSC and HID (only available on PYBD boards)

    For backwards compatibility, 'CDC' is understood to mean 'VCP' (and similarly for 'CDC+MSC' and 'CDC+HID').

    The port parameter should be an integer (0, 1, …) and selects which USB port to use if the board supports multiple ports. A value of -1 uses the default or automatically selected port.

    The vid and pid parameters allow you to specify the VID (vendor id) and PID (product id). A pid value of -1 will select a PID based on the value of modestr.

    If enabling MSC mode, the msc parameter can be used to specify a list of SCSI LUNs to expose on the mass storage interface. For example msc=(pyb.Flash(), pyb.SDCard()).

    If enabling HID mode, you may also specify the HID details by passing the hid keyword parameter. It takes a tuple of (subclass, protocol, max packet length, polling interval, report descriptor). By default it will set appropriate values for a USB mouse. There is also a pyb.hid_keyboard constant, which is an appropriate tuple for a USB keyboard.

    The high_speed parameter, when set to True, enables USB HS mode if it is supported by the hardware."""

# Constants

hid_mouse: hid_type
hid_keyboard: hid_type

# Classes

class ADC:
    def __init__(self, pin:int) -> None: """Create an ADC object associated with the given pin.
   This allows you to then read analog values on that pin."""


    def read(self) -> int: """Read the value on the analog pin and return it.  The returned value
   will be between 0 and 4095."""

    def read_timed(self, buf: Union[bytearray, Any], timer: Any) -> None: """
   Read analog values into ``buf`` at a rate set by the ``timer`` object.

   ``buf`` can be bytearray or array.array for example.  The ADC values have
   12-bit resolution and are stored directly into ``buf`` if its element size is
   16 bits or greater.  If ``buf`` has only 8-bit elements (eg a bytearray) then
   the sample resolution will be reduced to 8 bits.

   ``timer`` should be a Timer object, and a sample is read each time the timer
   triggers.  The timer must already be initialised and running at the desired
   sampling frequency.

   To support previous behaviour of this function, ``timer`` can also be an
   integer which specifies the frequency (in Hz) to sample at.  In this case
   Timer(6) will be automatically configured to run at the given frequency.

   Example using a Timer object (preferred way)::

       adc = pyb.ADC(pyb.Pin("P5"))        # create an ADC on pin P5
       tim = pyb.Timer(6, freq=10)         # create a timer running at 10Hz
       buf = bytearray(100)                # creat a buffer to store the samples
       adc.read_timed(buf, tim)            # sample 100 values, taking 10s

   Example using an integer for the frequency::

       adc = pyb.ADC(pyb.Pin("P5"))        # create an ADC on pin P5
       buf = bytearray(100)                # create a buffer of 100 bytes
       adc.read_timed(buf, 10)             # read analog values into buf at 10Hz
                                           #   this will take 10 seconds to finish
       for val in buf:                     # loop over all values
           print(val)                      # print the value out

   This function does not allocate any heap memory. It has blocking behaviour:
   it does not return to the calling program until the buffer is full."""
# class CAN – controller area network communication bus
# class DAC – digital to analog conversion
# class ExtInt – configure I/O pins to interrupt on external events
# class Flash – access to built-in flash storage
# class LED – LED object
# class Pin – control I/O pins
# class PinAF – Pin Alternate Functions
# class RTC – real time clock
# class Servo – 3-wire hobby servo driver
# class Timer – control internal timers
# class TimerChannel — setup a channel for a timer
# class USB_HID – USB Human Interface Device (HID)
# class USB_VCP – USB virtual comm port

