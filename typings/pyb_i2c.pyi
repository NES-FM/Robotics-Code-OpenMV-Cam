from typing import Optional, Any, Union
from typing_extensions import TypeAlias

I2C_mode: TypeAlias = int

class I2C:
    """I2C is a two-wire protocol for communicating between devices. At the physical level it consists of 2 wires: SCL and SDA, the clock and data lines respectively. OpenMV Cam does not provide Pullups on the SDA or SCL lines and external pullups are required on both SDA and SCL lines for the I2C bus to be functional.

    I2C objects are created attached to a specific bus. They can be initialised when created, or initialised later on."""
    
    def __init__(self, bus: int, **kwargs: Any) -> None:"""Construct an I2C object on the given bus. bus can be 2 or 4. With no additional parameters, the I2C object is created but not initialised (it has the settings from the last initialisation of the bus, if any). If extra arguments are given, the bus is initialised. See init for parameters of initialisation.

    The physical pins of the I2C busses on the OpenMV Cam are:

            I2C(2) is on the Y position: (SCL, SDA) = (P4, P5) = (PB10, PB11)

    The physical pins of the I2C busses on the OpenMV Cam M7 are:

            I2C(2) is on the Y position: (SCL, SDA) = (P4, P5) = (PB10, PB11)

            I2C(4) is on the Y position: (SCL, SDA) = (P7, P8) = (PD12, PD13)"""
    def deinit(self) -> None: "Turn off the I2C bus."
    def init(self, mode: I2C_mode, addr: Optional[int] = ..., baudrate: Optional[int] = ..., gencall: Optional[bool] = ..., dma: Optional[bool] = ...) -> None: """Initialise the I2C bus with the given parameters:

                mode must be either I2C.CONTROLLER or I2C.PERIPHERAL

                addr is the 7-bit address (only sensible for a peripheral)

                baudrate is the SCL clock rate (only sensible for a controller)

                gencall is whether to support general call mode

                dma is whether to allow the use of DMA for the I2C transfers (note that DMA transfers have more precise timing but currently do not handle bus errors properly)"""
    def is_ready(self, addr: int) -> bool: "Check if an I2C device responds to the given address. Only valid when in controller mode."
    def mem_read(self, data: Union[int, bytes], addr: int, memaddr: int, timeout: Optional[int] = ..., addr_size: Optional[int] = ...) -> bytes: """Read from the memory of an I2C device:

                data can be an integer (number of bytes to read) or a buffer to read into

                addr is the I2C device address

                memaddr is the memory location within the I2C device

                timeout is the timeout in milliseconds to wait for the read

                addr_size selects width of memaddr: 8 or 16 bits

        Returns the read data. This is only valid in controller mode."""
    def mem_write(self, data: Union[int, bytes], addr: int, memaddr: int, timeout: Optional[int] = ..., addr_size: Optional[int] = ...) -> None: """Write to the memory of an I2C device:

                data can be an integer or a buffer to write from

                addr is the I2C device address

                memaddr is the memory location within the I2C device

                timeout is the timeout in milliseconds to wait for the write

                addr_size selects width of memaddr: 8 or 16 bits

        Returns None. This is only valid in controller mode."""
    def recv(self, recv: Union[int, bytes], addr: Optional[int] = ..., timeout: Optional[int] = ...) -> bytes: """Receive data on the bus:

                recv can be an integer, which is the number of bytes to receive, or a mutable buffer, which will be filled with received bytes

                addr is the address to receive from (only required in controller mode)

                timeout is the timeout in milliseconds to wait for the receive

        Return value: if recv is an integer then a new buffer of the bytes received, otherwise the same buffer that was passed in to recv."""
    def send(self, send: Union[int, bytes], addr: Optional[int] = ..., timeout: Optional[int] = ...) -> None: """Send data on the bus:

                send is the data to send (an integer to send, or a buffer object)

                addr is the address to send to (only required in controller mode)

                timeout is the timeout in milliseconds to wait for the send

        Return value: None."""
    def scan(self) -> list[int]: "Scan all I2C addresses from 0x01 to 0x7f and return a list of those that respond. Only valid when in controller mode."

CONTROLLER: I2C_mode
"for initialising the bus to controller mode"
PERIPHERAL: I2C_mode
"for initialising the bus to peripheral mode"
