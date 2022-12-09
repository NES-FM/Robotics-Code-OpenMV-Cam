from image import Image, blob
def classify(path: str, img: Image, roi: tuple[int,int,int,int]=..., min_scale:int=..., scale_mul:int=..., x_overlap:int=..., y_overlap:int=...) -> tf_classification: """Executes the TensorFlow Lite image classification model on the img: Image object and returns a list of tf_classification objects. This method executes the network multiple times on the image in a controllable sliding window type manner (by default the algorithm only executes the network once on the whole image frame).

    path a path to a .tflite model to execute on your OpenMV Cam’s disk. The model is loaded into memory, executed, and released all in one function call to save from having to load the model in the MicroPython heap. Pass "person_detection" to load the built-in person detection model from your OpenMV Cam’s internal flash.

    roi is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the roi are operated on.

    min_scale controls how much scaling is applied to the network. At the default value the network is not scaled. However, a value of 0.5 would allow for detecting objects 50% in size of the image roi size…

    scale_mul controls how many different scales are tested out. The sliding window method works by multiplying a default scale of 1 by scale_mul while the result is over min_scale. The default value of scale_mul, 0.5, tests out a 50% size reduction per scale change. However, a value of 0.95 would only be a 5% size reductioin.

    x_overlap controls the percentage of overlap with the next detector area of the sliding window. A value of zero means no overlap. A value of 0.95 would mean 95% overlap.

    y_overlap controls the percentage of overlap with the next detector area of the sliding window. A value of zero means no overlap. A value of 0.95 would mean 95% overlap."""
def segment(path: str, img: Image, roi: tuple[int,int,int,int]=...) -> list[Image]: """Executes the TensorFlow Lite image segmentation model on the img: Image object and returns a list of grayscale image objects for each segmentation class output channel.

    path a path to a .tflite model to execute on your OpenMV Cam’s disk. The model is loaded into memory, executed, and released all in one function call to save from having to load the model in the MicroPython heap.

    roi is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the roi are operated on."""
def detect(path: str, img: Image, roi: tuple[int,int,int,int]=..., thresholds:list[tuple[int,int]]=..., invert:bool=...) -> list[list[blob]]: """Executes the TensorFlow Lite image segmentation model on the img: Image object and returns a list of image.blob objects for each segmentation class output. E.g. if you have an image that’s segmented into two classes this method will return a list of two lists of blobs that match the requested thresholds.

    path a path to a .tflite model to execute on your OpenMV Cam’s disk. The model is loaded into memory, executed, and released all in one function call to save from having to load the model in the MicroPython heap.

    roi is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the roi are operated on.

    thresholds must be a list of tuples [(lo, hi), (lo, hi), ..., (lo, hi)] defining the ranges of color you want to track. You may pass up to 32 threshold tuples in one call. Each tuple needs to contain two values - a min grayscale value and a max grayscale value. Only pixel regions that fall between these thresholds will be considered. For easy usage this function will automatically fix swapped min and max values. If the tuple is too short the rest of the thresholds are assumed to be at maximum range. If no thresholds are specified they are assumed to be (128, 255) which will detect “active” pixel regions in the segmented images.

    invert inverts the thresholding operation such that instead of matching pixels inside of some known color bounds pixels are matched that are outside of the known color bounds."""
def load(path: str, load_to_fb:bool=...)->tf_model: """path a path to a .tflite model to load into memory on the MicroPython heap by default.

    NOTE! The MicroPython heap is only ~50 KB on the OpenMV Cam M7 and ~256 KB on the OpenMV Cam H7.

    Pass "person_detection" to load the built-in person detection model from your OpenMV Cam’s internal flash. This built-in model does not use any Micropython Heap as all the weights are stored in flash which is accessible in the same way as RAM.

    load_to_fb if passed as True will instead reserve part of the OpenMV Cam frame buffer stack for storing the TensorFlow Lite model. You will get the most efficent execution performance for large models that do not fit on the heap by loading them into frame buffer memory once from disk and then repeatedly executing the model. That said, the frame buffer space used will not be available anymore for other algorithms.

    Returns a tf_model object which can operate on an image."""
def free_from_fb()->None: """Deallocates a previously allocated tf_model object created with load_to_fb set to True.

    Note that deallocations happen in the reverse order of allocation."""

class tf_classification:
    """class tf_classification – tf classification dection result¶

    The tf_classification object is returned by tf.classify() or tf_model.classify().
    Constructors¶
    Please call tf.classify() or tf_model.classify() to create this object."""

    def rect(self) -> tuple[int, int, int, int]: """Returns a rectangle tuple (x, y, w, h) for use with image methods like image.draw_rectangle() of the tf_classification’s bounding box."""
    def x(self) -> int: """Returns the tf_classification’s bounding box x coordinate (int).

    You may also get this value doing [0] on the object."""
    def y(self) -> int: """Returns the tf_classification’s bounding box y coordinate (int).

    You may also get this value doing [1] on the object."""
    def w(self) -> int: """Returns the tf_classification’s bounding box w coordinate (int).

    You may also get this value doing [2] on the object."""
    def h(self) -> int: """Returns the tf_classification’s bounding box h coordinate (int).

    You may also get this value doing [3] on the object."""
    def classification_output(self) -> list[str]: """Returns a list of the classification label scores. The size of this list is determined by your model output channel size. For example, mobilenet outputs a list of 1000 classification scores for all 1000 classes understood by mobilenet. Use zip in python to combine the classification score results with classification labels.

    You may also get this value doing [4] on the object."""



class tf_model:
    """class tf_model – TensorFlow Model¶

    If your model size is small enough and you have enough heap or frame buffer space you may wish to directly load the model into memory to save from having to load it from disk each time you wish to execute it.
    Constructors¶

    Please call tf.load() to create the TensorFlow Model object. TensorFlow Model objects allow you to execute a model from RAM versus having to load it from disk repeatedly."""
    def len(self) -> int: "Returns the size in bytes of the model."
    def ram(self) -> int: "Returns the model’s required free RAM in bytes."
    def input_height(self) -> int: "Returns the input height of the model. You can use this to size your input image height appropriately."
    def input_width(self) -> int: "Returns the input width of the model. You can use this to size your input image width appropriately."
    def input_channels(self) -> int: "Returns the number of input color channels in the model."
    def input_datatype(self) -> int: "Returns the model’s input datatype (this is a string of “uint8”, “int8”, or “float”)."
    def input_scale(self) -> int: "Returns the input scale for the model."
    def input_zero_point(self) -> int: "Returns the input zero point for the model."
    def output_height(self) -> int: "Returns the output height of the model. You can use this to size your output image height appropriately."
    def output_width(self) -> int: "Returns the output width of the model. You can use this to size your output image width appropriately."
    def output_channels(self) -> int: "Returns the number of output color channels in the model."
    def output_datatype(self) -> int: "Returns the model’s output datatype (this is a string of “uint8”, “int8”, or “float”)."
    def output_scale(self) -> int: "Returns the output scale for the model."
    def output_zero_point(self) -> int: "Returns the output zero point for the model."
    def classify(self, img: Image, roi: tuple[int,int,int,int]=..., min_scale:int=..., scale_mul:int=..., x_overlap:int=..., y_overlap:int=...) -> tf_classification: """Executes the TensorFlow Lite image classification model on the img: Image object and returns a list of tf_classification objects. This method executes the network multiple times on the image in a controllable sliding window type manner (by default the algorithm only executes the network once on the whole image frame).

        roi is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the roi are operated on.

        min_scale controls how much scaling is applied to the network. At the default value the network is not scaled. However, a value of 0.5 would allow for detecting objects 50% in size of the image roi size…

        scale_mul controls how many different scales are tested out. The sliding window method works by multiplying a default scale of 1 by scale_mul while the result is over min_scale. The default value of scale_mul, 0.5, tests out a 50% size reduction per scale change. However, a value of 0.95 would only be a 5% size reductioin.

        x_overlap controls the percentage of overlap with the next detector area of the sliding window. A value of zero means no overlap. A value of 0.95 would mean 95% overlap.

        y_overlap controls the percentage of overlap with the next detector area of the sliding window. A value of zero means no overlap. A value of 0.95 would mean 95% overlap."""
    def segment(self, img: Image, roi: tuple[int,int,int,int]=...) -> list[Image]: """Executes the TensorFlow Lite image segmentation model on the img: Image object and returns a list of grayscale image objects for each segmentation class output channel."

        roi is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the roi are operated on."""
        
    def detect(self, img: Image, roi: tuple[int,int,int,int]=..., thresholds:list[tuple[int,int]]=..., invert:bool=...) -> list[list[blob]]: """Executes the TensorFlow Lite image segmentation model on the img: Image object and returns a list of image.blob objects for each segmentation class output. E.g. if you have an image that's segmented into two classes this method will return a list of two lists of blobs that match the requested thresholds.

        roi is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the roi are operated on.

        thresholds must be a list of tuples [(lo, hi), (lo, hi), ..., (lo, hi)] defining the ranges of color you want to track. You may pass up to 32 threshold tuples in one call. Each tuple needs to contain two values - a min grayscale value and a max grayscale value. Only pixel regions that fall between these thresholds will be considered. For easy usage this function will automatically fix swapped min and max values. If the tuple is too short the rest of the thresholds are assumed to be at maximum range. If no thresholds are specified they are assumed to be (128, 255) which will detect “active” pixel regions in the segmented images.

        invert inverts the thresholding operation such that instead of matching pixels inside of some known color bounds pixels are matched that are outside of the known color bounds."""

