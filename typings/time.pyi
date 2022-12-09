class clock: # type:ignore
    def tick(self) -> None: "run this every time in loop"
    def fps(self) -> int: "calculates fps based on last time tick() was called"