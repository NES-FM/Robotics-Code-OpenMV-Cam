from abc import abstractmethod, ABCMeta
from typing import Callable, Any, Union
from struct import unpack, pack

class ard_comm(metaclass=ABCMeta):
    def __init__(self, balls_dict: dict, corner_dict: dict, exit_line_dict: dict):
        self.balls_dict = balls_dict
        self.corner_dict = corner_dict
        self.exit_line_dict = exit_line_dict
        
        self.heartbeat_id = 0x01
        self.balls_id = 0x10
        self.corner_id = 0x11
        self.exit_line_id = 0x12
        
        self.data_handlers = {}
        self.register_handler(self.heartbeat_id, self.heartbeat_handler)
        self.register_handler(self.balls_id, self.pack_balls)
        self.register_handler(self.corner_id, self.pack_corner)
        self.register_handler(self.exit_line_id, self.pack_exit_line)
        
        self.answer_unknown_opcode = b'\xfe'
        self.end_line_char = b'\xff'
        
        self._init_comm()
        
    def register_handler(self, opcode: int, func: Callable[[bytes], Union[bytes, None]]):
        self.data_handlers[opcode] = func
    
    @abstractmethod
    def _init_comm(self) -> None:
        pass
    @abstractmethod
    def _send_data(self, data: bytes) -> None:
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
        self._send_data(data + self.end_line_char)
        
    def send_gray_data(self):
        if len(self.balls_dict) > 0:
            self.answer_data(self.pack_balls())
        if len(self.corner_dict) > 0:
            self.answer_data(self.pack_corner())
    def send_rgb_data(self):
        if len(self.exit_line_dict) > 0:
            self.answer_data(self.pack_exit_line())
    
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
        return pack("<B", self.heartbeat_id) + params
    
    def pack_balls(self, params = None) -> bytes:
        ret_data = pack("<B", self.balls_id)

        ret_data += pack("<B", len(self.balls_dict))
        for (x, y, w, h), data in self.balls_dict.items():
            ret_data += pack("<BBBBB?", x, y, w, h, int(data["conf"]*100), data["classified_as"] == "black") # x y w h c*100 class=black
                    
        return ret_data
    
    def pack_corner(self, params = None) -> bytes:
        (x, y, w, h), data = list(self.corner_dict.items())[0]
        return pack("<BBBBBB", self.corner_id, x, y, w, h, int(data["conf"]*100))
    
    def pack_exit_line(self, params = None) -> bytes:
        (x, y, w, h), data = list(self.exit_line_dict.items())[0]
        return pack("<BBBBBB", self.exit_line_id, x, y, w, h, int(data["conf"]*100))
    
class ard_comm_uart(ard_comm):
    def _init_comm(self) -> None:
        from pyb import UART
        
        self.uart = UART(1)
        self.uart.init(115200, bits=8, parity=None)
    def is_data_available(self) -> bool:
        return self.uart.any() > 0
    def _send_data(self, data: bytes) -> None:
        self.uart.write(data)
    def _receive_data(self) -> bytes:
        rec_data = b""
        while self.is_data_available():
            byte_rec = self.uart.read(1)
            if not isinstance(byte_rec, type(None)):
                rec_data += byte_rec
            if byte_rec == self.end_line_char:
                break
        return rec_data
    
class ard_comm_local_test(ard_comm):
    def _init_comm(self) -> None:
        print("[COMM] Initializing Communication")
    def _receive_data(self) -> bytes:
        print("[COMM] Receiving Data... Emulating heartbeat packet with data 0x47")
        return pack("<BB", self.heartbeat_id, 0x47)
    def _send_data(self, data: bytes) -> None:
        print("[COMM] Sending data: ", end="")
        for x in data:
            print("{0:#0{1}x}".format(x,4), end=" ")
        print("")
    def is_data_available(self) -> bool:
        print("[COMM] Is Data Available: True")
        return True
    
        
if __name__ == '__main__':
    balls = {(0, 0, 12, 12): {"classified_as": "black", "value": 0.7, "circles": [], "conf": 0.934, "histo_class": "silver"}, (45, 23, 12, 12): {"classified_as": "silver", "value": 0.6, "circles": [], "conf": 0.78, "histo_class": "silver"}}
    corner = {(12, 20, 200, 30): {"classified_as": "corner", "value": 1, "circles": [], "conf": 0.994}}
    exit_line = {(120, 200, 130, 10): {"classified_as": "exit", "value": 1, "circles": [], "conf": 1}}

    mycl = ard_comm_local_test(balls_dict = balls, corner_dict = corner, exit_line_dict = exit_line)
    
    mycl.tick()
    
    print("")
    
    mycl.send_gray_data()
    mycl.send_rgb_data()
    
    # print(mycl.pack_balls()) # 0x10 0x02 0x00 0x00 0x0c 0x0c 0x5d 0x01 0x2d 0x17 0x0c 0x0c 0x4e 0x00 0xff
    # print(mycl.pack_corner()) # 0x11 0x0c 0x14 0xc8 0x1e 0x63 0xff
    # print(mycl.pack_exit_line()) # 0x12 0x78 0xc8 0x82 0x0a 0x64 0xff

    
    
"""
C Code for interpreting received Data

char rec_bytes[40] = {0x2, 0x0, 0x0, 0xc, 0xc, 0x5d, 0x1, 0x2d, 0x17, 0xc, 0xc, 0x4e, 0x0, 0xa};

struct {
    uint8_t x;
    uint8_t y;
    uint8_t w;
    uint8_t h;
    uint8_t conf;
    bool black;
} typedef ball;

ball rec_balls[10];

int main()
{
    uint8_t len = rec_bytes[0];
    
    for (int i = 0; i < len; i++)
    {
        memcpy(&rec_balls[i], &rec_bytes[(i*sizeof(ball))+1], sizeof(ball));
    }
    
    //printf("len: %d ptrballs%d ptrbytes%d ptrball2s%d ptrbyte2s%d\n", len, &rec_balls, &(rec_bytes), &rec_balls[0], &rec_bytes[1]);
    
    for (ball b : rec_balls) {
        printf("Ball: x%d y%d w%d h%d c%d %s\n", b.x, b.y, b.w, b.h, b.conf, b.black ? "black" : "silver");
    }

    return 0;
}
"""