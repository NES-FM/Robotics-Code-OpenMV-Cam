from abc import abstractmethod, ABCMeta
from typing import Callable, Any, Union
from struct import unpack, pack

class ard_comm(metaclass=ABCMeta):
    def __init__(self):
        self.data_handlers = {}
        
        self.register_handler(0x01, self.heartbeat_handler)
        
        self.answer_unknown_opcode = b'\xff'
        
    def register_handler(self, opcode: int, func: Callable[[bytes], Union[bytes, None]]):
        self.data_handlers[opcode] = func
    
    @abstractmethod
    def _send_data(self, data) -> None:
        pass
    @abstractmethod
    def _receive_data(self) -> bytes:
        pass
    
    @abstractmethod
    def is_data_available(self) -> bool:
        pass
    
    def tick(self):
        if self.is_data_available():
            data = self._receive_data()
            self.interpret_data(data)
            
    def answer_data(self, data: bytes):
        self._send_data(data + b'\n')
    
    def interpret_data(self, data: bytes):
        opcode = data[0]
        params = data[1:]
        func = self.data_handlers.get(opcode, None)
        if not isinstance(func, type(None)):
            ret = func(params)
            if not isinstance(ret, type(None)):
                self.answer_data(ret)
        else:
            self.answer_data(self.answer_unknown_opcode)
            
    def heartbeat_handler(self, params: bytes) -> bytes:
        return params
        
        
class ard_comm_i2c(ard_comm):
    def test(self):
        print("hi")
        
if __name__ == '__main__':
    mycl = ard_comm_i2c()
