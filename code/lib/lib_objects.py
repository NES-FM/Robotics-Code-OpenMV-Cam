#from image import histogram, blob
class base_object:
    def __init__(self) -> None:
        self.screen_x:int
        self.screen_y:int
        self.screen_w:int
        self.screen_h:int
        self.det_rad_x:int
        self.det_rad_y:int
        self.det_rad_w:int
        self.det_rad_h:int
        self.confidence:float
        self.histogram:histogram
        self.valid:bool

    def init(self, screen_rect=None, screen_x=0, screen_y=0, screen_w=0, screen_h=0, confidence=0.0, histogram=None, reset=False):
        if not isinstance(screen_rect, type(None)):
            self.screen_x, self.screen_y, self.screen_w, self.screen_h = screen_rect
        else:
            self.screen_x=screen_x
            self.screen_y=screen_y
            self.screen_w=screen_w
            self.screen_h=screen_h

        self.confidence=confidence

        if not isinstance(histogram, type(None)):
            self.histogram=histogram

        self.valid = not reset

        return self

    def get_screen_rect(self) -> tuple[int, int, int, int]:
        return (self.screen_x, self.screen_y, self.screen_w, self.screen_h)

    def set_screen_det_rad(self, x, y, w, h):
        self.det_rad_x=x
        self.det_rad_y=y
        self.det_rad_w=w
        self.det_rad_h=h

    def get_screen_det_rad(self):
        return (self.det_rad_x, self.det_rad_y, self.det_rad_w, self.det_rad_h)

class ball(base_object):
    SILVER = False
    BLACK = True
    def __init__(self) -> None:
        self.classified_as:bool
        self.classification_value:float
        self.circles_detected:list
        self.histogram_classification:bool
        super().__init__()

    def init(self, screen_rect=None, screen_x=0, screen_y=0, screen_w=0, screen_h=0, confidence=0.0, histogram=None, classified_as=SILVER, classification_value=0.0, circles_detected=None, histogram_classification=SILVER, reset=False):
        self.classified_as=classified_as
        self.classification_value=classification_value

        if not isinstance(circles_detected, type(None)):
            self.circles_detected=circles_detected
        else:
            self.circles_detected=[]

        self.histogram_classification=histogram_classification
        return super().init(screen_rect, screen_x, screen_y, screen_w, screen_h, confidence, histogram, reset)

class corner(base_object):
    def __init__(self) -> None:
        self.classification_value:float
        self.blob:blob
        self.detected_by_tf:bool
        super().__init__()

    def init(self, screen_rect=None, screen_x=0, screen_y=0, screen_w=0, screen_h=0, confidence=0.0, histogram=None, classification_value=0.0, blob=None, detected_by_tf=False, reset=False):
        self.classification_value=classification_value
        if not isinstance(blob, type(None)):
            self.blob=blob
        self.detected_by_tf=detected_by_tf
        return super().init(screen_rect, screen_x, screen_y, screen_w, screen_h, confidence, histogram, reset)

class exit_line(base_object):
    def __init__(self) -> None:
        self.blob:blob
        super().__init__()
    def init(self, screen_rect=None, screen_x=0, screen_y=0, screen_w=0, screen_h=0, confidence=0.0, histogram=None, blob=None, reset=False):
        if not isinstance(blob, type(None)):
            self.blob=blob
        return super().init(screen_rect, screen_x, screen_y, screen_w, screen_h, confidence, histogram, reset)
