from typing import Optional, Any, Union
from typing_extensions import TypeAlias

UART_flow: TypeAlias = int

class UART: 
    def __init__(self, bus: int, **kwargs: Any) -> None: """Construct a UART object on the given bus. bus can be 1/3. With no additional parameters, the UART object is created but not initialised (it has the settings from the last initialisation of the bus, if any). If extra arguments are given, the bus is initialised. See init for parameters of initialisation.

    The physical pins of the UART bus are for the OpenMV Cam:

            UART(3): (TX, RX) = (P4, P5) = (PB10, PB11)

    The physical pins of the UART busses are for the OpenMV Cam M7 and H7:

            UART(1): (TX, RX) = (P1, P0) = (PB14, PB15)

            UART(3): (TX, RX) = (P4, P5) = (PB10, PB11)"""
    def init(self, baudrate: int, bits: Optional[int] = ..., parity: Union[None, bool] = ..., stop: Optional[int] = ..., timeout: Optional[int] = ..., flow: Optional[UART_flow] = ..., timeout_char: Optional[int] = ..., read_buf_len: Optional[int] = ...) -> None: """Initialise the UART bus with the given parameters:

            baudrate is the clock rate.

            bits is the number of bits per character, 7, 8 or 9.

            parity is the parity, None, 0 (even) or 1 (odd).

            stop is the number of stop bits, 1 or 2.

            flow sets the flow control type. Can be 0, UART.RTS, UART.CTS or UART.RTS | UART.CTS.

            timeout is the timeout in milliseconds to wait for writing/reading the first character.

            timeout_char is the timeout in milliseconds to wait between characters while writing or reading.

            read_buf_len is the character length of the read buffer (0 to disable).

    This method will raise an exception if the baudrate could not be set within 5% of the desired value.

    Note: with parity=None, only 8 and 9 bits are supported. With parity enabled, only 7 and 8 bits are supported."""
    def deinit(self) -> None: "Turn off the UART bus."
    def any(self) -> int: "Returns the number of bytes waiting (may be 0)."
    def read(self, nbytes: Optional[int] = ...) -> Union[None, bytes]: """Read characters. If nbytes is specified then read at most that many bytes. If nbytes are available in the buffer, returns immediately, otherwise returns when sufficient characters arrive or the timeout elapses.

    If nbytes is not given then the method reads as much data as possible. It returns after the timeout has elapsed.

    Note: for 9 bit characters each character takes two bytes, nbytes must be even, and the number of characters is nbytes/2.

    Return value: a bytes object containing the bytes read in. Returns None on timeout."""
    def readchar(self) -> int: """Receive a single character on the bus.

    Return value: The character read, as an integer. Returns -1 on timeout."""
    def readinto(self, buf: bytes, nbytes: Optional[int] = ...) -> Union[int, None]: """Read bytes into the buf. If nbytes is specified then read at most that many bytes. Otherwise, read at most len(buf) bytes.

    Return value: number of bytes read and stored into buf or None on timeout."""
    def readline(self) -> bytes: """Read a line, ending in a newline character. If such a line exists, return is immediate. If the timeout elapses, all available data is returned regardless of whether a newline exists.

    Return value: the line read or None on timeout if no data is available."""
    def write(self, buf: bytes) -> None: """Write the buffer of bytes to the bus. If characters are 7 or 8 bits wide then each byte is one character. If characters are 9 bits wide then two bytes are used for each character (little endian), and buf must contain an even number of bytes.

    Return value: number of bytes written. If a timeout occurs and no bytes were written returns None."""
    def writechar(self, char: int) -> None: "Write a single character on the bus. char is an integer to write. Return value: None. See note below if CTS flow control is used."
    def sendbreak(self) -> None: "Send a break condition on the bus. This drives the bus low for a duration of 13 bits. Return value: None."


RTS: UART_flow
CTS: UART_flow
"to select the flow control type."


"""Flow Control¶

UART(3) support RTS/CTS hardware flow control using the following pins:

        UART(3) is on :(TX, RX, nRTS, nCTS) = (P4, P5, P1, P2) = (PB10, PB11, PB14, PB13)

In the following paragraphs the term “target” refers to the device connected to the UART.

When the UART’s init() method is called with flow set to one or both of UART.RTS and UART.CTS the relevant flow control pins are configured. nRTS is an active low output, nCTS is an active low input with pullup enabled. To achieve flow control the Pyboard’s nCTS signal should be connected to the target’s nRTS and the Pyboard’s nRTS to the target’s nCTS.
CTS: target controls OpenMV Cam transmitter¶

If CTS flow control is enabled the write behaviour is as follows:

If the OpenMV Cam’s UART.write(buf) method is called, transmission will stall for any periods when nCTS is False. This will result in a timeout if the entire buffer was not transmitted in the timeout period. The method returns the number of bytes written, enabling the user to write the remainder of the data if required. In the event of a timeout, a character will remain in the UART pending nCTS. The number of bytes composing this character will be included in the return value.

If UART.writechar() is called when nCTS is False the method will time out unless the target asserts nCTS in time. If it times out OSError 116 will be raised. The character will be transmitted as soon as the target asserts nCTS.
RTS: OpenMV Cam controls target’s transmitter¶

If RTS flow control is enabled, behaviour is as follows:

If buffered input is used (read_buf_len > 0), incoming characters are buffered. If the buffer becomes full, the next character to arrive will cause nRTS to go False: the target should cease transmission. nRTS will go True when characters are read from the buffer.

Note that the any() method returns the number of bytes in the buffer. Assume a buffer length of N bytes. If the buffer becomes full, and another character arrives, nRTS will be set False, and any() will return the count N. When characters are read the additional character will be placed in the buffer and will be included in the result of a subsequent any() call.

If buffered input is not used (read_buf_len == 0) the arrival of a character will cause nRTS to go False until the character is read.
"""