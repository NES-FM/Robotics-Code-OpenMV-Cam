from typing import Any, Union, Optional, Callable
from typing_extensions import TypeAlias
from sensor import Pixformat, Color_palette

Conversion_hints: TypeAlias = int

def binary_to_grayscale(binary_image_value: bool) -> int: "Returns a converted binary value (0-1) to a grayscale value (0-255)."

def binary_to_rgb(binary_image_value: bool) -> tuple[int, int, int]: "Returns a converted binary value (0-1) to a 3 value RGB888 tuple."

def binary_to_lab(binary_image_value: bool) -> tuple[int, int, int]: """Returns a converted binary value (0-1) to a 3 value LAB tuple.

   L goes between 0 and 100 and A/B go from -128 to 128."""

def binary_to_yuv(binary_image_value: bool) -> tuple[int, int, int]: """Returns a converted binary value (0-1) to a 3 value YUV tuple.

   Y goes between 0 and 255 and U/V go from -128 to 128."""

def grayscale_to_binary(grayscale_value: int) -> bool: "Returns a converted grayscale value (0-255) to a binary value (0-1)."

def grayscale_to_rgb(grayscale_value: int) -> tuple[int, int, int]: """Returns a converted grayscale value to a 3 value RGB888 tuple.

   Note
   ----
      The OpenMV Cam firmware does the conversion using a RGB565->RGB888 process
      so this method won't return the exact values as a pure RGB888 system would.
      However, it's true to how the image lib works internally."""

def grayscale_to_lab(grayscale_value: int) -> tuple[int, int, int]: """Returns a converted grayscale value to a 3 value LAB tuple.

   L goes between 0 and 100 and A/B go from -128 to 128.

   Note
   ----
      The OpenMV Cam firmware does the conversion using a RGB565->LAB process
      so this method won't return the exact values as a pure LAB system would.
      However, it's true to how the image lib works internally."""

def grayscale_to_yuv(grayscale_value: int) -> tuple[int, int, int]: """Returns a converted grayscale value to a 3 value YUV tuple.

   Y goes between 0 and 255 and U/V go from -128 to 128.

   Note
   ----
      The OpenMV Cam firmware does the conversion using a RGB565->YUV process
      so this method won't return the exact values as a pure YUV system would.
      However, it's true to how the image lib works internally."""

def rgb_to_binary(rgb_tuple: tuple[int, int, int]) -> bool: """Returns a converted 3 value RGB888 tuple to a center range thresholded binary value (0-1).

   Note
   ----

      The OpenMV Cam firmware does the conversion using a RGB888->RGB565 proces
      so this method won't return the exact values as a pure RGB888 system would.
      However, it's true to how the image lib works internally."""

def rgb_to_grayscale(rgb_tuple: tuple[int, int, int]) -> int:"""Returns a converted 3 value RGB888 tuple to a grayscale value (0-255).

   Note
   ----

      The OpenMV Cam firmware does the conversion using a RGB888->RGB565 process
      so this method won't return the exact values as a pure RGB888 system would.
      However, it's true to how the image lib works internally."""

def rgb_to_lab(rgb_tuple: tuple[int, int, int]) -> tuple[int, int, int]:"""Returns a converted 3 value RGB888 tuple to a 3 value LAB tuple.

   L goes between 0 and 100 and A/B go from -128 to 128.

   Note
   ----

      The OpenMV Cam firmware does the conversion using a RGB888->RGB565 process
      so this method won't return the exact values as a pure RGB888 system would.
      However, it's true to how the image lib works internally."""

def rgb_to_yuv(rgb_tuple: tuple[int, int, int]) -> tuple[int, int, int]:"""Returns a converted 3 value RGB888 tuple to a 3 value YUV tuple.

   Y goes between 0 and 255 and U/V go from -128 to 128.

   Note
   ----

      The OpenMV Cam firmware does the conversion using a RGB888->RGB565 process
      so this method won't return the exact values as a pure RGB888 system would.
      However, it's true to how the image lib works internally."""

def lab_to_binary(lab_tuple: tuple[int, int, int]) -> bool:"""Returns a converted 3 value LAB tuple to a center range thresholded binary value (0-1).

   Note
   ----

      The OpenMV Cam firmware does the conversion using a LAB->RGB565 process
      so this method won't return the exact values as a pure LAB system would.
      However, it's true to how the image lib works internally."""

def lab_to_grayscale(lab_tuple: tuple[int, int, int]) -> int:"""Returns a converted 3 value LAB tuple to a grayscale value (0-255).

   Note
   ----

      The OpenMV Cam firmware does the conversion using a LAB->RGB565 process
      so this method won't return the exact values as a pure LAB system would.
      However, it's true to how the image lib works internally."""

def lab_to_rgb(lab_tuple: tuple[int, int, int]) -> tuple[int, int, int]:"""Returns a converted 3 value LAB tuple to a 3 value RGB888 tuple.

   Note
   ----

      The OpenMV Cam firmware does the conversion using a LAB->RGB565 process
      so this method won't return the exact values as a pure LAB system would.
      However, it's true to how the image lib works internally."""

def lab_to_yuv(lab_tuple: tuple[int, int, int]) -> tuple[int, int, int]:"""Returns a converted 3 value LAB tuple to a 3 value YUV tuple.

   Y goes between 0 and 255 and U/V go from -128 to 128.

   Note
   ----

      The OpenMV Cam firmware does the conversion using a LAB->RGB565 process
      so this method won't return the exact values as a pure LAB system would.
      However, it's true to how the image lib works internally."""

def yuv_to_binary(yuv_tuple: tuple[int, int, int]) -> bool:"""Returns a converted 3 value YUV tuple to a center range thresholded binary value (0-1).

   Note
   ----

      The OpenMV Cam firmware does the conversion using a YUV->RGB565 process
      so this method won't return the exact values as a pure YUV system would.
      However, it's true to how the image lib works internally."""

def yuv_to_grayscale(yuv_tuple: tuple[int, int, int]) -> int:"""Returns a converted 3 value YUV tuple to a grayscale value (0-255).

   Note
   ----

      The OpenMV Cam firmware does the conversion using a YUV->RGB565 process
      so this method won't return the exact values as a pure YUV system would.
      However, it's true to how the image lib works internally."""

def yuv_to_rgb(yuv_tuple: tuple[int, int, int]) -> tuple[int, int, int]:"""Returns a converted 3 value YUV tuple to a 3 value RGB888 tuple.

   Note
   ----

      The OpenMV Cam firmware does the conversion using a YUV->RGB565 process
      so this method won't return the exact values as a pure YUV system would.
      However, it's true to how the image lib works internally."""

def yuv_to_lab(yuv_tuple: tuple[int, int, int]) -> tuple[int, int, int]:"""Returns a converted 3 value YUV tuple to a 3 value LAB tuple.

   L goes between 0 and 100 and A/B go from -128 to 128.

   Note
   ----

      The OpenMV Cam firmware does the conversion using a YUV->RGB565 process
      so this method won't return the exact values as a pure YUV system would.
      However, it's true to how the image lib works internally."""

def load_decriptor(path: str) -> None:"""Loads a descriptor object from disk.

   ``path`` is the path to the descriptor file to load."""

def save_descriptor(path: str, descriptor: Any) -> None:"""Saves the descriptor object ``descriptor`` to disk.

   ``path`` is the path to the descriptor file to save."""

def match_descriptor(descritor0: Any, descriptor1: Any, threshold: Optional[int] = ..., filter_outliers: Optional[bool] = ...) -> int:"""For LBP descriptors this function returns an integer representing the
   difference between the two descriptors. You may then threshold/compare this
   distance metric as necessary. The distance is a measure of similarity. The
   closer it is to zero the better the LBP keypoint match.

   For ORB descriptors this function returns the ``kptmatch`` object. See above.

   ``threshold`` is used for ORB keypoints to filter ambiguous matches. A lower
   ``threshold`` value tightens the keypoint matching algorithm. ``threshold``
   may be between 0-100 (int). Defaults to 70.

   ``filter_outliers`` is used for ORB keypoints to filter out outlier
   keypoints allow you to raise the ``threshold``. Defaults to False."""

class HaarCascade:
   """The Haar Cascade feature descriptor is used for the image.find_features() method. It doesn’t have any methods itself for you to call.
   Loads a Haar Cascade into memory from a Haar Cascade binary file formatted
   for your OpenMV Cam. If you pass "frontalface" instead of a path then this
   constructor will load the built-in frontal face Haar Cascade into memory.
   Additionally, you can also pass "eye" to load a Haar Cascade for eyes into
   memory. Finally, this method returns the loaded Haar Cascade object for use
   with `image.find_features()`.

   ``stages`` defaults to the number of stages in the Haar Cascade. However,
   you can specify a lower number of stages to speed up processing the feature
   detector at the cost of a higher rate of false positives.

   Note
   ----
      You can make your own Haar Cascades to use with your OpenMV Cam.
      First, Google for "<thing> Haar Cascade" to see if someone
      already made an OpenCV Haar Cascade for an object you want to
      detect. If not... then you'll have to generate your own (which is
      a lot of work). See `here <http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html>`_
      for how to make your own Haar Cascade. Then see this `script <https://github.com/openmv/openmv/blob/master/usr/openmv-cascade.py>`_
      for converting OpenCV Haar Cascades into a format your OpenMV Cam
      can read.

   Q: What is a Haar Cascade?

   A: A Haar Cascade is a series of contrast checks that are used to determine
   if an object is present in the image. The contrast checks are split of into
   stages where a stage is only run if previous stages have already passed.
   The contrast checks are simple things like checking if the center vertical
   of the image is lighter than the edges. Large area checks are performed
   first in the earlier stages followed by more numerous and smaller area
   checks in later stages.

   Q: How are Haar Cascades made?

   A: Haar Cascades are made by training the generator algorithm against
   positive and negative labeled images. For example, you'd train the
   generator algorithm against hundreds of pictures with cats in them that
   have been labeled as images with cats and against hundreds of images with
   not cat like things labeled differently. The generator algorithm will then
   produce a Haar Cascade that detects cats."""
   def __init__(self, path: str, stages: Optional[Any] = ...) -> None:...
      
class histogram:
   """The histogram object is returned by `image.get_histogram()`.

   Grayscale histograms have one channel with some number of bins. All bins are
   normalized so that all bins sum to 1.

   RGB565 histograms have three channels with some number of bins each. All bins
   are normalized so that all bins in a channel sum to 1.
   Please call `image.get_histogram()` to create this object."""

   def bins(self) -> list[float]:"""Returns a list of floats for the grayscale histogram.

      You may also get this value doing ``[0]`` on the object."""

   def l_bins(self) -> list[float]:"""Returns a list of floats for the RGB565 histogram LAB L channel.

      You may also get this value doing ``[0]`` on the object."""

   def a_bins(self) -> list[float]:"""Returns a list of floats for the RGB565 histogram LAB A channel.

      You may also get this value doing ``[1]`` on the object."""

   def b_bins(self) -> list[float]:"""Returns a list of floats for the RGB565 histogram LAB B channel.

      You may also get this value doing ``[2]`` on the object."""

   def get_percentile(self, percentile: float) -> percentile:"""Computes the CDF of the histogram channels and returns a `image.percentile`
      object with the values of the histogram at the passed in ``percentile`` (0.0
      - 1.0) (float). So, if you pass in 0.1 this method will tell you (going from
      left-to-right in the histogram) what bin when summed into an accumulator
      caused the accumulator to cross 0.1. This is useful to determine min (with
      0.1) and max (with 0.9) of a color distribution without outlier effects
      ruining your results for adaptive color tracking."""

   def get_threshold(self) -> threshold:"""Uses Otsu's Method to compute the optimal threshold values that split the
      histogram into two halves for each channel of the histogram. This method
      returns a `image.threshold` object. This method is particularly useful for
      determining optimal `image.binary()` thresholds."""

   def get_statistics(self) -> statistics:"""Computes the mean, median, mode, standard deviation, min, max, lower
      quartile, and upper quartile of each color channel in the histogram and
      returns a `statistics` object.

      You may also use ``histogram.statistics()`` and ``histogram.get_stats()``
      as aliases for this method."""

class percentile:
   """The percentile object is returned by `histogram.get_percentile()`.

Grayscale percentiles have one channel. Use the non ``l_*``, ``a_*``, and
``b_*`` method.

RGB565 percentiles have three channels. Use the ``l_*``, ``a_*``, and ``b_*``
methods.
Please call `histogram.get_percentile()` to create this object."""

   def value(self) -> int:"""Return the grayscale percentile value (between 0 and 255).

      You may also get this value doing ``[0]`` on the object."""

   def l_value(self) -> int:"""Return the RGB565 LAB L channel percentile value (between 0 and 100).

      You may also get this value doing ``[0]`` on the object."""

   def a_value(self) -> int:"""Return the RGB565 LAB A channel percentile value (between -128 and 127).

      You may also get this value doing ``[1]`` on the object."""

   def b_value(self) -> int:"""Return the RGB565 LAB B channel percentile value (between -128 and 127).

      You may also get this value doing ``[2]`` on the object."""

class threshold:
   """The threshold object is returned by `histogram.get_threshold()`.

Grayscale thresholds have one channel. Use the non ``l_*``, ``a_*``, and
``b_*`` method.

RGB565 thresholds have three channels. Use the ``l_*``, ``a_*``, and ``b_*``
methods.
Please call `histogram.get_threshold()` to create this object."""

   def value(self) -> int:"""Return the grayscale threshold value (between 0 and 255).

      You may also get this value doing ``[0]`` on the object."""

   def l_value(self) -> int:"""Return the RGB565 LAB L channel threshold value (between 0 and 100).

      You may also get this value doing ``[0]`` on the object."""

   def a_value(self) -> int:"""Return the RGB565 LAB A channel threshold value (between -128 and 127).

      You may also get this value doing ``[1]`` on the object."""

   def b_value(self) -> int:"""Return the RGB565 LAB B channel threshold value (between -128 and 127).

      You may also get this value doing ``[2]`` on the object."""

class statistics:
   """The percentile object is returned by `histogram.get_statistics()` or
`image.get_statistics()`.

Grayscale statistics have one channel. Use the non ``l_*``, ``a_*``, and
``b_*`` method.

RGB565 statistics have three channels. Use the ``l_*``, ``a_*``, and ``b_*``
methods.
Please call `histogram.get_statistics()` or `image.get_statistics()` to create this object."""

   def mean(self) -> int:"""Returns the grayscale mean (0-255) (int).

      You may also get this value doing ``[0]`` on the object."""

   def median(self) -> int:"""Returns the grayscale median (0-255) (int).

      You may also get this value doing ``[1]`` on the object."""

   def mode(self) -> int:"""Returns the grayscale mode (0-255) (int).

      You may also get this value doing ``[2]`` on the object."""

   def stdev(self) -> int:"""Returns the grayscale standard deviation (0-255) (int).

      You may also get this value doing ``[3]`` on the object."""

   def min(self) -> int:"""Returns the grayscale min (0-255) (int).

      You may also get this value doing ``[4]`` on the object."""

   def max(self) -> int:"""Returns the grayscale max (0-255) (int).

      You may also get this value doing ``[5]`` on the object."""

   def lq(self) -> int:"""Returns the grayscale lower quartile (0-255) (int).

      You may also get this value doing ``[6]`` on the object."""

   def uq(self) -> int:"""Returns the grayscale upper quartile (0-255) (int).

      You may also get this value doing ``[7]`` on the object."""

   def l_mean(self) -> int:"""Returns the RGB565 LAB L mean (0-255) (int).

      You may also get this value doing ``[0]`` on the object."""

   def l_median(self) -> int:"""Returns the RGB565 LAB L median (0-255) (int).

      You may also get this value doing ``[1]`` on the object."""

   def l_mode(self) -> int:"""Returns the RGB565 LAB L mode (0-255) (int).

      You may also get this value doing ``[2]`` on the object."""

   def l_stdev(self) -> int:"""Returns the RGB565 LAB L standard deviation (0-255) (int).

      You may also get this value doing ``[3]`` on the object."""

   def l_min(self) -> int:"""Returns the RGB565 LAB L min (0-255) (int).

      You may also get this value doing ``[4]`` on the object."""

   def l_max(self) -> int:"""Returns the RGB565 LAB L max (0-255) (int).

      You may also get this value doing ``[5]`` on the object."""

   def l_lq(self) -> int:"""Returns the RGB565 LAB L lower quartile (0-255) (int).

      You may also get this value doing ``[6]`` on the object."""

   def l_uq(self) -> int:"""Returns the RGB565 LAB L upper quartile (0-255) (int).

      You may also get this value doing ``[7]`` on the object."""

   def a_mean(self) -> int:"""Returns the RGB565 LAB A mean (0-255) (int).

      You may also get this value doing ``[8]`` on the object."""

   def a_median(self) -> int:"""Returns the RGB565 LAB A median (0-255) (int).

      You may also get this value doing ``[9]`` on the object."""

   def a_mode(self) -> int:"""Returns the RGB565 LAB A mode (0-255) (int).

      You may also get this value doing ``[10]`` on the object."""

   def a_stdev(self) -> int:"""Returns the RGB565 LAB A standard deviation (0-255) (int).

      You may also get this value doing ``[11]`` on the object."""

   def a_min(self) -> int:"""Returns the RGB565 LAB A min (0-255) (int).

      You may also get this value doing ``[12]`` on the object."""

   def a_max(self) -> int:"""Returns the RGB565 LAB A max (0-255) (int).

      You may also get this value doing ``[13]`` on the object."""

   def a_lq(self) -> int:"""Returns the RGB565 LAB A lower quartile (0-255) (int).

      You may also get this value doing ``[14]`` on the object."""

   def a_uq(self) -> int:"""Returns the RGB565 LAB A upper quartile (0-255) (int).

      You may also get this value doing ``[15]`` on the object."""

   def b_mean(self) -> int:"""Returns the RGB565 LAB B mean (0-255) (int).

      You may also get this value doing ``[16]`` on the object."""

   def b_median(self) -> int:"""Returns the RGB565 LAB B median (0-255) (int).

      You may also get this value doing ``[17]`` on the object."""

   def b_mode(self) -> int:"""Returns the RGB565 LAB B mode (0-255) (int).

      You may also get this value doing ``[18]`` on the object."""

   def b_stdev(self) -> int:"""Returns the RGB565 LAB B standard deviation (0-255) (int).

      You may also get this value doing ``[19]`` on the object."""

   def b_min(self) -> int:"""Returns the RGB565 LAB B min (0-255) (int).

      You may also get this value doing ``[20]`` on the object."""

   def b_max(self) -> int:"""Returns the RGB565 LAB B max (0-255) (int).

      You may also get this value doing ``[21]`` on the object."""

   def b_lq(self) -> int:"""Returns the RGB565 LAB B lower quartile (0-255) (int).

      You may also get this value doing ``[22]`` on the object."""

   def b_uq(self) -> int:"""Returns the RGB565 LAB B upper quartile (0-255) (int).

      You may also get this value doing ``[23]`` on the object."""

class blob:
   """The blob object is returned by `image.find_blobs()`.
   Please call `image.find_blobs()` to create this object."""

   def corners(self) -> list[tuple[int, int]]:"""Returns a list of 4 (x,y) tuples of the 4 corners of the object. Corners are
      always returned in sorted clock-wise order starting from the top left."""

   def min_corners(self) -> list[tuple[int, int]]:"""Returns a list of 4 (x,y) tuples of the 4 corners than bound the min area
      rectangle of the blob. Unlike `blob.corners()` the min area rectangle corners
      do not necessarily lie on the blob."""

   def rect(self) -> tuple[int, int, int, int]:"""Returns a rectangle tuple (x, y, w, h) for use with other `image` methods
      like `image.draw_rectangle()` of the blob's bounding box."""

   def x(self) -> int:"""Returns the blob's bounding box x coordinate (int).

      You may also get this value doing ``[0]`` on the object."""

   def y(self) -> int:"""Returns the blob's bounding box y coordinate (int).

      You may also get this value doing ``[1]`` on the object."""

   def w(self) -> int:"""Returns the blob's bounding box w coordinate (int).

      You may also get this value doing ``[2]`` on the object."""

   def h(self) -> int:"""Returns the blob's bounding box h coordinate (int).

      You may also get this value doing ``[3]`` on the object."""

   def pixels(self) -> int:"""Returns the number of pixels that are part of this blob (int).

      You may also get this value doing ``[4]`` on the object."""

   def cx(self) -> int:"""Returns the centroid x position of the blob (int).

      You may also get this value doing ``[5]`` on the object."""

   def cxf(self) -> float:"""Returns the centroid x position of the blob (float)."""

   def cy(self) -> int:"""Returns the centroid y position of the blob (int).

      You may also get this value doing ``[6]`` on the object."""

   def cyf(self) -> float:"""Returns the centroid y position of the blob (float)."""

   def rotation(self) -> float:"""Returns the rotation of the blob in radians (float). If the blob is like
      a pencil or pen this value will be unique for 0-180 degrees. If the blob
      is round this value is not useful.

      You may also get this value doing ``[7]`` on the object."""

   def rotation_deg(self) -> float:"""Returns the rotation of the blob in degrees."""

   def rotation_rad(self) -> float:"""Returns the rotation of the blob in radians. This method is more descriptive
      than just `blob.rotation()`."""

   def code(self) -> int:"""Returns a 32-bit binary number with a bit set in it for each color threshold
      that's part of this blob. For example, if you passed `image.find_blobs()`
      three color thresholds to look for then bits 0/1/2 may be set for this blob.
      Note that only one bit will be set for each blob unless `image.find_blobs()`
      was called with ``merge=True``. Then its possible for multiple blobs with
      different color thresholds to be merged together. You can use this method
      along with multiple thresholds to implement color code tracking.

      You may also get this value doing ``[8]`` on the object."""

   def count(self) -> int:"""Returns the number of blobs merged into this blob. This is 1 unless you
      called `image.find_blobs()` with ``merge=True``.

      You may also get this value doing ``[9]`` on the object."""

   def perimeter(self) -> int:"""Returns the number of pixels on this blob's perimeter."""

   def roundness(self) -> float:"""Returns a value between 0 and 1 representing how round the object is. A circle would be a 1."""

   def elongation(self) -> float:"""Returns a value between 0 and 1 representing how long (not round) the object is. A line would be a 1."""

   def area(self) -> int:"""Returns the area of the bounding box around the blob. (w * h)."""

   def density(self) -> float:"""Returns the density ratio of the blob. This is the number of pixels in the
      blob over its bounding box area. A low density ratio means in general that
      the lock on the object isn't very good. The result is between 0 and 1."""

   def extent(self) -> float:"""Alias for `blob.density()`."""

   def compactness(self) -> float:"""Like `blob.density()`, but, uses the perimeter of the blob instead to measure
      the objects density and is thus more accurate. The result is between 0 and 1."""

   def solidity(self) -> float:"""Like `blob.density()` but, uses the minimum area rotated rectangle versus the
      bounding rectangle to measure density. The result is between 0 and 1."""

   def convexity(self) -> float:"""Returns a value between 0 and 1 representing how convex the object is. A square would be 1."""

   def x_hist_bins(self) -> float:"""Returns a histogram of the x axis of all columns in a blob. Bin values are
      scaled between 0 and 1."""

   def y_hist_bins(self) -> float:"""Returns a histogram of the y axis of all the rows in a blob. Bin values are
      scaled between 0 and 1."""

   def major_axis_line(self) -> tuple[int, int, int, int]:"""Returns a line tuple (x1, y1, x2, y2) that can be drawn with `image.draw_line()` of the major
      axis of the blob (the line going through the longest side of the min area rectangle)."""

   def minor_axis_line(self) -> tuple[int, int, int, int]:"""Returns a line tuple (x1, y1, x2, y2) that can be drawn with `image.draw_line()` of the minor
      axis of the blob (the line going through the shortest side of the min area rectangle)."""

   def enclosing_circle(self) -> tuple[int, int, float]:"""Returns a circle tuple (x, y, r) that can be drawn with `image.draw_circle()` of
      the circle that encloses the min area rectangle of a blob."""

   def enclosed_ellipse(self) -> tuple[int, int, int, int, float]:"""Returns an ellipse tuple (x, y, rx, ry, rotation) that can be drawn with `image.draw_ellipse()`
      of the ellipse that fits inside of the min area rectangle of a blob."""
   def __iter__(self) -> Any: pass
   
   def output(self) -> float: "Only valid in the context of tf.detect()"

class line:
   """The line object is returned by `image.find_lines()`, `image.find_line_segments()`, or `image.get_regression()`.
   Please call `image.find_lines()`, `image.find_line_segments()`, or `image.get_regression()` to create this object."""

   def line(self) -> tuple[int, int, int, int]: """Returns a line tuple (x1, y1, x2, y2) for use with other `image` methods
      like `image.draw_line()`.
"""
   def x1(self) -> int: """Returns the line's p1 x component.

      You may also get this value doing ``[0]`` on the object."""

   def y1(self) -> int: """Returns the line's p1 y component.

      You may also get this value doing ``[1]`` on the object."""

   def x2(self) -> int: """Returns the line's p2 x component.

      You may also get this value doing ``[2]`` on the object."""

   def y2(self) -> int: """Returns the line's p2 y component.

      You may also get this value doing ``[3]`` on the object."""

   def length(self) -> float: """Returns the line's length: sqrt(((x2-x1)^2) + ((y2-y1)^2).

      You may also get this value doing ``[4]`` on the object."""

   def magnitude(self) -> int: """Returns the magnitude of the line from the hough transform.

      You may also get this value doing ``[5]`` on the object."""

   def theta(self) -> float: """Returns the angle of the line from the hough transform - (0 - 179) degrees.

      You may also get this value doing ``[7]`` on the object."""

   def rho(self) -> int: """Returns the the rho value for the line from the hough transform.

      You may also get this value doing ``[8]`` on the object."""

class circle:

   """The circle object is returned by `image.find_circles()`.
   Please call `image.find_circles()` to create this object."""

   def x(self) -> int: """Returns the circle's x position.

      You may also get this value doing ``[0]`` on the object."""

   def y(self) -> int: """Returns the circle's y position.

      You may also get this value doing ``[1]`` on the object."""

   def r(self) -> int: """Returns the circle's radius.

      You may also get this value doing ``[2]`` on the object."""

   def magnitude(self) -> int: """Returns the circle's magnitude.

      You may also get this value doing ``[3]`` on the object."""
      
   def __iter__(self) -> Any: pass

class rect:
   """The rect object is returned by `image.find_rects()`.
   Please call `image.find_rects()` to create this object."""

   def corners(self) -> list[tuple[int, int]]: """Returns a list of 4 (x,y) tuples of the 4 corners of the object. Corners are
      always returned in sorted clock-wise order starting from the top left.
"""
   def rect(self) -> tuple[int, int, int, int]: """Returns a rectangle tuple (x, y, w, h) for use with other `image` methods
      like `image.draw_rectangle()` of the rect's bounding box.
"""
   def x(self) -> int: """Returns the rectangle's top left corner's x position.

      You may also get this value doing ``[0]`` on the object."""

   def y(self) -> int: """Returns the rectangle's top left corner's y position.

      You may also get this value doing ``[1]`` on the object."""

   def w(self) -> int: """Returns the rectangle's width.

      You may also get this value doing ``[2]`` on the object."""

   def h(self) -> int: """Returns the rectangle's height.

      You may also get this value doing ``[3]`` on the object."""

   def magnitude(self) -> int: """Returns the rectangle's magnitude.

      You may also get this value doing ``[4]`` on the object."""

class qrcode:

   """The qrcode object is returned by `image.find_qrcodes()`.
   Please call `image.find_qrcodes()` to create this object."""

   def corners(self) -> list[tuple[int, int]]: """Returns a list of 4 (x,y) tuples of the 4 corners of the object. Corners are
      always returned in sorted clock-wise order starting from the top left.
"""
   def rect(self) -> tuple[int, int, int, int]: """Returns a rectangle tuple (x, y, w, h) for use with other `image` methods
      like `image.draw_rectangle()` of the qrcode's bounding box.
"""
   def x(self) -> int: """Returns the qrcode's bounding box x coordinate (int).

      You may also get this value doing ``[0]`` on the object."""

   def y(self) -> int: """Returns the qrcode's bounding box y coordinate (int).

      You may also get this value doing ``[1]`` on the object."""

   def w(self) -> int: """Returns the qrcode's bounding box w coordinate (int).

      You may also get this value doing ``[2]`` on the object."""

   def h(self) -> int: """Returns the qrcode's bounding box h coordinate (int).

      You may also get this value doing ``[3]`` on the object."""

   def payload(self) -> str: """Returns the payload string of the qrcode. E.g. the URL.

      You may also get this value doing ``[4]`` on the object."""

   def version(self) -> int: """Returns the version number of the qrcode (int).

      You may also get this value doing ``[5]`` on the object."""

   def ecc_level(self) -> int: """Returns the ecc_level of the qrcode (int).

      You may also get this value doing ``[6]`` on the object."""

   def mask(self) -> int: """Returns the mask of the qrcode (int).

      You may also get this value doing ``[7]`` on the object."""

   def data_type(self) -> int: """Returns the data type of the qrcode (int).

      You may also get this value doing ``[8]`` on the object."""

   def eci(self) -> int: """Returns the eci of the qrcode (int). The eci stores the encoding of data
      bytes in the QR Code. If you plan to handling QR Codes that contain more
      than just standard ASCII text you will need to look at this value.

      You may also get this value doing ``[9]`` on the object."""

   def is_numeric(self) -> bool: """Returns True if the data_type of the qrcode is numeric."""

   def is_alphanumeric(self) -> bool: """Returns True if the data_type of the qrcode is alpha numeric."""

   def is_binary(self) -> bool: """Returns True if the data_type of the qrcode is binary. If you are serious
      about handling all types of text you need to check the eci if this is True
      to determine the text encoding of the data. Usually, it's just standard
      ASCII, but, it could be UTF8 that has some 2-byte characters in it."""

   def is_kanji(self) -> bool: """Returns True if the data_type of the qrcode is alpha Kanji. If this is True
      then you'll need to decode the string yourself as Kanji symbols are 10-bits
      per character and MicroPython has no support to parse this kind of text. The
      payload in this case must be treated as just a large byte array."""

# class AprilTag -- AprilTag object
# ---------------------------------

# The apriltag object is returned by `image.find_apriltags()`.

# .. class:: image.apriltag()

#    Please call `image.find_apriltags()` to create this object.

#    .. method:: apriltag.corners()

#       Returns a list of 4 (x,y) tuples of the 4 corners of the object. Corners are
#       always returned in sorted clock-wise order starting from the top left.

#    .. method:: apriltag.rect()

#       Returns a rectangle tuple (x, y, w, h) for use with other `image` methods
#       like `image.draw_rectangle()` of the apriltag's bounding box.

#    .. method:: apriltag.x()

#       Returns the apriltag's bounding box x coordinate (int).

#       You may also get this value doing ``[0]`` on the object.

#    .. method:: apriltag.y()

#       Returns the apriltag's bounding box y coordinate (int).

#       You may also get this value doing ``[1]`` on the object.

#    .. method:: apriltag.w()

#       Returns the apriltag's bounding box w coordinate (int).

#       You may also get this value doing ``[2]`` on the object.

#    .. method:: apriltag.h()

#       Returns the apriltag's bounding box h coordinate (int).

#       You may also get this value doing ``[3]`` on the object.

#    .. method:: apriltag.id()

#       Returns the numeric id of the apriltag.

#         * TAG16H5 -> 0 to 29
#         * TAG25H7 -> 0 to 241
#         * TAG25H9 -> 0 to 34
#         * TAG36H10 -> 0 to 2319
#         * TAG36H11 -> 0 to 586
#         * ARTOOLKIT -> 0 to 511

#       You may also get this value doing ``[4]`` on the object.

#    .. method:: apriltag.family()

#       Returns the numeric family of the apriltag.

#         * image.TAG16H5
#         * image.TAG25H7
#         * image.TAG25H9
#         * image.TAG36H10
#         * image.TAG36H11
#         * image.ARTOOLKIT

#       You may also get this value doing ``[5]`` on the object.

#    .. method:: apriltag.cx()

#       Returns the centroid x position of the apriltag (int).

#       You may also get this value doing ``[6]`` on the object.

#    .. method:: apriltag.cy()

#       Returns the centroid y position of the apriltag (int).

#       You may also get this value doing ``[7]`` on the object.

#    .. method:: apriltag.rotation()

#       Returns the rotation of the apriltag in radians (float).

#       You may also get this value doing ``[8]`` on the object.

#    .. method:: apriltag.decision_margin()

#       Returns the quality of the apriltag match (0.0 - 1.0) where 1.0 is the best.

#       You may also get this value doing ``[9]`` on the object.

#    .. method:: apriltag.hamming()

#       Returns the number of accepted bit errors for this tag.

#         * TAG16H5 -> 0 bit errors will be accepted
#         * TAG25H7 -> up to 1 bit error may be accepted
#         * TAG25H9 -> up to 3 bit errors may be accepted
#         * TAG36H10 -> up to 3 bit errors may be accepted
#         * TAG36H11 -> up to 4 bit errors may be accepted
#         * ARTOOLKIT -> 0 bit errors will be accepted

#       You may also get this value doing ``[10]`` on the object.

#    .. method:: apriltag.goodness()

#       Returns the quality of the apriltag image (0.0 - 1.0) where 1.0 is the best.

#       Note
#       ----

#          This value is always 0.0 for now. We may enable a feature called "tag
#          refinement" in the future which will allow detection of small apriltags.
#          However, this feature currently drops the frame rate to less than 1 FPS.

#       You may also get this value doing ``[11]`` on the object.

#    .. method:: apriltag.x_translation()

#       Returns the translation in unknown units from the camera in the X direction.

#       This method is useful for determining the apriltag's location away from the
#       camera. However, the size of the apriltag, the lens you are using, etc. all
#       come into play as to actually determining what the X units are in. For ease
#       of use we recommend you use a lookup table to convert the output of this
#       method to something useful for your application.

#       Note that this is the left-to-right direction.

#       You may also get this value doing ``[12]`` on the object.

#    .. method:: apriltag.y_translation()

#       Returns the translation in unknown units from the camera in the Y direction.

#       This method is useful for determining the apriltag's location away from the
#       camera. However, the size of the apriltag, the lens you are using, etc. all
#       come into play as to actually determining what the Y units are in. For ease
#       of use we recommend you use a lookup table to convert the output of this
#       method to something useful for your application.

#       Note that this is the up-to-down direction.

#       You may also get this value doing ``[13]`` on the object.

#    .. method:: apriltag.z_translation()

#       Returns the translation in unknown units from the camera in the Z direction.

#       This method is useful for determining the apriltag's location away from the
#       camera. However, the size of the apriltag, the lens you are using, etc. all
#       come into play as to actually determining what the Z units are in. For ease
#       of use we recommend you use a lookup table to convert the output of this
#       method to something useful for your application.

#       Note that this is the front-to-back direction.

#       You may also get this value doing ``[14]`` on the object.

#    .. method:: apriltag.x_rotation()

#       Returns the rotation in radians of the apriltag in the X plane. E.g. moving
#       the camera left-to-right while looking at the tag.

#       You may also get this value doing ``[15]`` on the object.

#    .. method:: apriltag.y_rotation()

#       Returns the rotation in radians of the apriltag in the Y plane. E.g. moving
#       the camera up-to-down while looking at the tag.

#       You may also get this value doing ``[16]`` on the object.

#    .. method:: apriltag.z_rotation()

#       Returns the rotation in radians of the apriltag in the Z plane. E.g.
#       rotating the camera while looking directly at the tag.

#       Note that this is just a renamed version of `apriltag.rotation()`.

#       You may also get this value doing ``[17]`` on the object.

# class DataMatrix -- DataMatrix object
# -------------------------------------

# The datamatrix object is returned by `image.find_datamatrices()`.

# .. class:: image.datamatrix()

#    Please call `image.find_datamatrices()` to create this object.

#    .. method:: datamatrix.corners()

#       Returns a list of 4 (x,y) tuples of the 4 corners of the object. Corners are
#       always returned in sorted clock-wise order starting from the top left.

#    .. method:: datamatrix.rect()

#       Returns a rectangle tuple (x, y, w, h) for use with other `image` methods
#       like `image.draw_rectangle()` of the datamatrix's bounding box.

#    .. method:: datamatrix.x()

#       Returns the datamatrix's bounding box x coordinate (int).

#       You may also get this value doing ``[0]`` on the object.

#    .. method:: datamatrix.y()

#       Returns the datamatrix's bounding box y coordinate (int).

#       You may also get this value doing ``[1]`` on the object.

#    .. method:: datamatrix.w()

#       Returns the datamatrix's bounding box w coordinate (int).

#       You may also get this value doing ``[2]`` on the object.

#    .. method:: datamatrix.h()

#       Returns the datamatrix's bounding box h coordinate (int).

#       You may also get this value doing ``[3]`` on the object.

#    .. method:: datamatrix.payload()

#       Returns the payload string of the datamatrix. E.g. The string.

#       You may also get this value doing ``[4]`` on the object.

#    .. method:: datamatrix.rotation()

#       Returns the rotation of the datamatrix in radians (float).

#       You may also get this value doing ``[5]`` on the object.

#    .. method:: datamatrix.rows()

#       Returns the number of rows in the data matrix (int).

#       You may also get this value doing ``[6]`` on the object.

#    .. method:: datamatrix.columns()

#       Returns the number of columns in the data matrix (int).

#       You may also get this value doing ``[7]`` on the object.

#    .. method:: datamatrix.capacity()

#       Returns how many characters could fit in this data matrix.

#       You may also get this value doing ``[8]`` on the object.

#    .. method:: datamatrix.padding()

#       Returns how many unused characters are in this data matrix.

#       You may also get this value doing ``[9]`` on the object.

# class BarCode -- BarCode object
# -------------------------------

# The barcode object is returned by `image.find_barcodes()`.

# .. class:: image.barcode()

#    Please call `image.find_barcodes()` to create this object.

#    .. method:: barcode.corners()

#       Returns a list of 4 (x,y) tuples of the 4 corners of the object. Corners are
#       always returned in sorted clock-wise order starting from the top left.

#    .. method:: barcode.rect()

#       Returns a rectangle tuple (x, y, w, h) for use with other `image` methods
#       like `image.draw_rectangle()` of the barcode's bounding box.

#    .. method:: barcode.x()

#       Returns the barcode's bounding box x coordinate (int).

#       You may also get this value doing ``[0]`` on the object.

#    .. method:: barcode.y()

#       Returns the barcode's bounding box y coordinate (int).

#       You may also get this value doing ``[1]`` on the object.

#    .. method:: barcode.w()

#       Returns the barcode's bounding box w coordinate (int).

#       You may also get this value doing ``[2]`` on the object.

#    .. method:: barcode.h()

#       Returns the barcode's bounding box h coordinate (int).

#       You may also get this value doing ``[3]`` on the object.

#    .. method:: barcode.payload()

#       Returns the payload string of the barcode. E.g. The number.

#       You may also get this value doing ``[4]`` on the object.

#    .. method:: barcode.type()

#       Returns the type enumeration of the barcode (int).

#       You may also get this value doing ``[5]`` on the object.

#         * image.EAN2
#         * image.EAN5
#         * image.EAN8
#         * image.UPCE
#         * image.ISBN10
#         * image.UPCA
#         * image.EAN13
#         * image.ISBN13
#         * image.I25
#         * image.DATABAR
#         * image.DATABAR_EXP
#         * image.CODABAR
#         * image.CODE39
#         * image.PDF417 - Future (e.g. doesn't work right now).
#         * image.CODE93
#         * image.CODE128

#    .. method:: barcode.rotation()

#       Returns the rotation of the barcode in radians (float).

#       You may also get this value doing ``[6]`` on the object.

#    .. method:: barcode.quality()

#       Returns the number of times this barcode was detected in the image (int).

#       When scanning a barcode each new scanline can decode the same barcode. This
#       value increments for a barcode each time that happens...

#       You may also get this value doing ``[7]`` on the object.

# class Displacement -- Displacement object
# -----------------------------------------

# The displacement object is returned by `image.find_displacement()`.

# .. class:: image.displacement()

#    Please call `image.find_displacement()` to create this object.

#    .. method:: displacement.x_translation()

#       Returns the x translation in pixels between two images. This is sub pixel
#       accurate so it's a float.

#       You may also get this value doing ``[0]`` on the object.

#    .. method:: displacement.y_translation()

#       Returns the y translation in pixels between two images. This is sub pixel
#       accurate so it's a float.

#       You may also get this value doing ``[1]`` on the object.

#    .. method:: displacement.rotation()

#       Returns the rotation in radians between two images.

#       You may also get this value doing ``[2]`` on the object.

#    .. method:: displacement.scale()

#       Returns the scale change between two images.

#       You may also get this value doing ``[3]`` on the object.

#    .. method:: displacement.response()

#       Returns the quality of the results of displacement matching between two images.
#       Between 0-1. A ``displacement`` object with a response less than 0.1 is likely noise.

#       You may also get this value doing ``[4]`` on the object.

# class kptmatch -- Keypoint Object
# ---------------------------------

# The kptmatch object is returned by `image.match_descriptor()` for keypoint matches.

# .. class:: image.kptmatch()

#    Please call `image.match_descriptor()` to create this object.

#    .. method:: kptmatch.rect()

#       Returns a rectangle tuple (x, y, w, h) for use with other `image` methods
#       like `image.draw_rectangle()` of the kptmatch's bounding box.

#    .. method:: kptmatch.cx()

#       Returns the centroid x position of the kptmatch (int).

#       You may also get this value doing ``[0]`` on the object.

#    .. method:: kptmatch.cy()

#       Returns the centroid y position of the kptmatch (int).

#       You may also get this value doing ``[1]`` on the object.

#    .. method:: kptmatch.x()

#       Returns the kptmatch's bounding box x coordinate (int).

#       You may also get this value doing ``[2]`` on the object.

#    .. method:: kptmatch.y()

#       Returns the kptmatch's bounding box y coordinate (int).

#       You may also get this value doing ``[3]`` on the object.

#    .. method:: kptmatch.w()

#       Returns the kptmatch's bounding box w coordinate (int).

#       You may also get this value doing ``[4]`` on the object.

#    .. method:: kptmatch.h()

#       Returns the kptmatch's bounding box h coordinate (int).

#       You may also get this value doing ``[5]`` on the object.

#    .. method:: kptmatch.count()

#       Returns the number of keypoints matched (int).

#       You may also get this value doing ``[6]`` on the object.

#    .. method:: kptmatch.theta()

#       Returns the estimated angle of rotation for the keypoint (int).

#       You may also get this value doing ``[7]`` on the object.

#    .. method:: kptmatch.match()

#       Returns the list of (x,y) tuples of matching keypoints.

#       You may also get this value doing ``[8]`` on the object.

class ImageIO:
   """The ImageIO object allows you to read/write OpenMV Image objects in their native form to disk
   or to memory. This class provides fast read/write random access for loading/storing images."""

   def __init__(self, path: Union[str, tuple[int, int, int]], mode: str) -> None:"""Creates an ImageIO object.

   If ``path`` is a file name on disk then that file will be opened for reading if ``mode`` is ``'r'``
   or writing if ``mode`` is ``'w'``.

   ``path`` may also be a 3-value tuple (w, h, bpp) for in-memory storage of images. ``mode`` in
   this case is then the number of image buffers to store in memory. Note that the in-memory
   storage buffer is not allowed to grow in size after being allocated. Use a ``bpp`` value of
   0 for binary images, 1 for grayscale images, and 2 for rgb565 images."""

   def size(self) -> int: """Returns the number of bytes on disk or memory used by the ImageIO object."""

   def write(self, img: Image) -> ImageIO: """Writes a new image ``img`` to the ImageIO object. For on disk ImageIO objects the file will
      grow as new images are added. For in-memory ImageIO objects this just writes an image to the
      current pre-allocated slot before advancing to the next slot.

      Returns the ImageIO object."""

   def read(self, copy_to_fb: Optional[bool] = ..., loop: Optional[bool] = ..., pause: Optional[bool] = ...) -> Image: 
      """Returns an image object from the ImageIO object. If ``copy_to_fb`` is False then
      the new image is allocated on the MicroPython heap. However, the MicroPython heap is limited
      and may not have space to store the new image if exhausted. Instead, set ``copy_to_fb`` to
      True to set the frame buffer to the new image making this function work just like `sensor.snapshot()`.

      ``loop`` if True automatically causes the ImageIO object to seek to the beginning at the end
      of the stream of images.

      ``pause`` if True causes this method to pause for a previously recorded number of milliseconds
      by write in-order to match the original frame rate that captured the image data.

      ``copy_to_fb`` may also be another image object if you want to replace that image object's memory
      buffer, type, width, and height with new image data.

      Note
      ----

         Any use of ``copy_to_fb`` invalidates the previous image object it overwrites. Do not use
         any references to previous image objects anymore it overwrites. Either for an image object
         referencing the frame buffer, frame buffer stack, or an image on the MicroPython heap."""

   def seek(self, offset: int) -> Image: """Seeks to the image slot number ``offset`` in the ImageIO object.

      You may use this along with write and read to implement an image fifo."""

   def close(self) -> None: """Closes the ImageIO object. For in-memory objects this free's the allocated space and for
      on-disk files this closes the file and writes out all meta-data."""


class Image:
   "The image object is the basic object for machine vision operations."

   def __init__(self, path: str, copy_to_fb: Optional[bool] = ...) -> None:
      """Creates a new image object from a file at ``path``. Alternatively, you may
      pass a width, height, and either `sensor.BINARY`, `sensor.GRAYSCALE`, or
      `sensor.RGB565` to create new blank image object (initialized to 0 - black).

      Supports bmp/pgm/ppm/jpg/jpeg image files.

      ``copy_to_fb`` if True the image is loaded directly into the frame buffer
      allowing you to load up large images. If False, the image is loaded into
      MicroPython's heap which is much smaller than the frame buffer.

      You may also set ``copy_to_fb`` equal to another image object and that
      buffer will then be overwritten with the copied image changing the passed
      image object's pixel format and resolution.

      Note
      ----

         If ``copy_to_fb`` is set to True or another image object do not continue
         using the old image object passed to this method or the frame buffer
         image object. Use the new returned image object reference from this
         method as the old references are now stale.

      Images support "[]" notation. Do ``image[index] = 8/16-bit value`` to assign
      an image pixel or ``image[index]`` to get an image pixel which will be
      either an 8-bit value for grayscale images of a 16-bit RGB565 value for RGB
      images.

      For JPEG images the "[]" allows you to access the compressed JPEG image blob
      as a byte-array. Reading and writing to the data array is opaque however as
      JPEG images are compressed byte streams.

      Images also support read buffer operations. You can pass images to all sorts
      of MicroPython functions like as if the image were a byte-array object. In
      particular, if you'd like to transmit an image you can just pass it to the
      UART/SPI/I2C write functions to be transmitted automatically."""

   def width(self) -> int:"""Returns the image width in pixels."""

   def height(self) -> int:"""Returns the image height in pixels."""

   def format(self) -> Pixformat:"""Returns `sensor.GRAYSCALE` for grayscale images, `sensor.RGB565` for RGB565
      images, `sensor.BAYER` for bayer pattern images, and `sensor.JPEG` for JPEG
      images."""

   def size(self) -> int:"""Returns the image size in bytes."""

   def bytearray(self) -> bytearray:"""Returns a `bytearray` object that points to the image data for byte-level read/write access.

      Note
      ----

         Image objects are automatically cast as `bytes` objects when passed to MicroPython driver
         that requires a `bytes` like object. This is read-only access.
         Call `bytearray()` to get read/write access."""

   def get_pixel(self, x: int, y: int, rgbtuple: Optional[bool] = ...) -> Union[int, tuple[int, int, int], None]:
      """For grayscale images: Returns the grayscale pixel value at location (x, y).
      For RGB565 images: Returns the RGB888 pixel tuple (r, g, b) at location (x, y).
      For bayer pattern images: Returns the the pixel value at the location (x, y).

      Returns None if ``x`` or ``y`` is outside of the image.

      ``x`` and ``y`` may either be passed independently or as a tuple.

      ``rgbtuple`` if True causes this method to return an RGB888 tuple. Otherwise,
      this method returns the integer value of the underlying pixel. I.e. for RGB565
      images this method returns a RGB565 value. Defaults to True
      for RGB565 images and False otherwise.

      Not supported on compressed images.

      Note
      ----

         `image.get_pixel()` and `image.set_pixel()` are the only methods that allow
         you to manipulate bayer pattern images. Bayer pattern images are literal images
         where pixels in the image are R/G/R/G/etc. for even rows and G/B/G/B/etc. for
         odd rows. Each pixel is 8-bits. If you call this method with ``rgbtuple`` set then `image.get_pixel()`
         will debayer the source image at that pixel location and return a valid RGB888 tuple for the pixel location."""

   def set_pixel(self, x: int, y: int, pixel: Union[int, tuple[int, int, int]]) -> None:"""For grayscale images: Sets the pixel at location (x, y) to the grayscale value ``pixel``.
      For RGB565 images: Sets the pixel at location (x, y) to the RGB888 tuple (r, g, b) ``pixel``.
      For bayer pattern images: Sets the pixel value at the location (x, y) to the value ``pixel``.

      Returns the image object so you can call another method using ``.`` notation.

      ``x`` and ``y`` may either be passed independently or as a tuple.

      ``pixel`` may either be an RGB888 tuple (r, g, b) or the underlying pixel
      value (i.e. a RGB565 value for RGB565 images or an 8-bit value
      for grayscale images.

      Not supported on compressed images.

      Note
      ----

         `image.get_pixel()` and `image.set_pixel()` are the only methods that allow
         you to manipulate bayer pattern images. Bayer pattern images are literal images
         where pixels in the image are R/G/R/G/etc. for even rows and G/B/G/B/etc. for
         odd rows. Each pixel is 8-bits. If you call this method with an RGB888 tuple the grayscale
         value of that RGB888 tuple is extracted and set to the pixel location."""

   def mean_pool(self, x_div: int, y_div: int) -> Image:"""Finds the mean of ``x_div`` * ``y_div`` squares in the image and returns
      the modified image composed of the mean of each square.

      This method allows you to shrink an image down very quickly in-place.

      Not supported on compressed images or bayer images."""

   def mean_pooled(self, x_div: int, y_div: int) -> Image:"""Finds the mean of ``x_div`` * ``y_div`` squares in the image and returns
      a new image composed of the mean of each square.

      This method allows you to create a shrunken down image copy.

      Not supported on compressed images or bayer images."""

   def midpoint_pool(self, x_div: int, y_div: int, bias: Optional[float] = ...) -> Image:"""Finds the midpoint of ``x_div`` * ``y_div`` squares in the image and returns
      the modified image composed of the midpoint of each square.

      A ``bias`` of 0.0 returns the min of each area while a ``bias`` of 1.0 returns
      the max of each area.

      This method allows you to shrink an image down very quickly in-place.

      Not supported on compressed images or bayer images."""

   def midpoint_pooled(self, x_div: int, y_div: int, bias: Optional[float] = ...) -> Image:"""Finds the midpoint of ``x_div`` * ``y_div`` squares in the image and returns
      a new image composed of the midpoint of each square.

      A ``bias`` of 0.0 returns the min of each area while a ``bias`` of 1.0 returns
      the max of each area.

      This method allows you to create a shrunken down image copy.

      Not supported on compressed images or bayer images."""

   def to_bitmap(self, x_scale: Optional[float] = ..., y_scale: Optional[float] = ..., roi: Optional[tuple[int, int, int, int]] = ..., rgb_channel: Optional[int] = ..., alpha: Optional[int] = ..., color_palette: Color_palette = ..., alpha_palette: Optional[int] = ..., hint: Optional[Conversion_hints] = ..., x_size: Optional[int] = ..., y_size: Optional[int] = ..., copy: Optional[bool] = ...)-> Image:"""

      Converts an image to a bitmap image (1 bit per pixel). If ``copy`` is False
      this method will try to modify the image in-place. If ``copy`` is True then
      this method will return a new image copy allocated on the heap.

      ``copy`` may also be another image object, which in this case this method will try to
      re-use that image objects storage space and will return a new image object that uses
      the previous image objects storage space. After doing this do not use any references
      to the old image object anymore as they will be stale.

      ``x_scale`` controls how much the drawn image is scaled by in the x direction (float). If this
      value is negative the image will be flipped horizontally.

      ``y_scale`` controls how much the drawn image is scaled by in the y direction (float). If this
      value is negative the image will be flipped vertically.

      ``roi`` is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This
      allows you to extract just the pixels in the ROI to scale and draw on the destination image.

      ``rgb_channel`` is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed)
      and to render onto the destination image. For example, if you pass ``rgb_channel=1`` this will
      extract the green channel of the source RGB565 image and draw that in grayscale on the
      destination image.

      ``alpha`` controls how much of the source image to blend into the destination image. A value of
      256 draws an opaque source image while a value lower than 256 produces a blend between the source
      and destination image. 0 results in no modification to the destination image.

      ``color_palette`` if not ``-1`` can be `sensor.PALETTE_RAINBOW`, `sensor.PALETTE_IRONBOW`, or
      a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of
      whatever the source image is. This is applied after ``rgb_channel`` extraction if used.

      ``alpha_palette`` if not ``-1`` can be a 256 pixel in total GRAYSCALE image to use as a alpha
      palette which modulates the ``alpha`` value of the source image being drawn at a pixel pixel
      level allowing you to precisely control the alpha value of pixels based on their grayscale value.
      A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes
      more transparent until 0. This is applied after ``rgb_channel`` extraction if used.

      ``hint`` can be a logical OR of the flags:

         * `image.AREA`: Use area scaling when downscaling versus the default of nearest neighbor.
         * `image.BILINEAR`: Use bilinear scaling versus the default of nearest neighbor scaling.
         * `image.BICUBIC`: Use bicubic scaling versus the default of nearest neighbor scaling.
         * `image.CENTER`: Center the image image being draw on (x, y).
         * `image.EXTRACT_RGB_CHANNEL_FIRST`: Do rgb_channel extraction before scaling.
         * `image.APPLY_COLOR_PALETTE_FIRST`: Apply color palette before scaling.
         * `image.BLACK_BACKGROUND`: Assume the destination image is black. This speeds up drawing.

      ``x_size`` may be passed if ``x_scale`` is not passed to specify the size of the image to draw
      and ``x_scale`` will automatically be determined passed on the input image size. If neither
      ``y_scale`` or ``y_size`` are specified then ``y_scale`` internally will be set to be equal to
      ``x_size`` to maintain the aspect-ratio.

      ``y_size`` may be passed if ``y_scale`` is not passed to specify the size of the image to draw
      and ``y_scale`` will automatically be determined passed on the input image size. If neither
      ``x_scale`` or ``x_size`` are specified then ``x_scale`` internally will be set to be equal to
      ``y_size`` to maintain the aspect-ratio.

      Note
      ----

         Bitmap images are like grayscale images with only two pixels values - 0
         and 1. Additionally, bitmap images are packed such that they only store
         1 bit per pixel making them very small. The OpenMV image library allows
         bitmap images to be used in all places `sensor.GRAYSCALE` and `sensor.RGB565` images
         can be used. However, many operations when applied on bitmap images don't
         make any sense becuase bitmap images only have 2 values. OpenMV recommends
         using bitmap images for ``mask`` values in operations and such as they
         fit on the MicroPython heap quite easily. Finally, bitmap image pixel values
         0 and 1 are interpreted as black and white when being applied to `sensor.GRAYSCALE`
         or `sensor.RGB565` images. The library automatically handles conversion.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images."""

   def to_grayscale(self, x_scale: Optional[float] = ..., y_scale: Optional[float] = ..., roi: Optional[tuple[int, int, int, int]] = ..., rgb_channel: Optional[int] = ..., alpha: Optional[int] = ..., color_palette: Color_palette = ..., alpha_palette: Optional[int] = ..., hint: Optional[Conversion_hints] = ..., x_size: Optional[int] = ..., y_size: Optional[int] = ..., copy: Optional[bool] = ...) -> Image:"""

      Converts an image to a grayscale image (8-bits per pixel). If ``copy`` is False
      this method will try to modify the image in-place. If ``copy`` is True then
      this method will return a new image copy allocated on the heap.

      ``copy`` may also be another image object, which in this case this method will try to
      re-use that image objects storage space and will return a new image object that uses
      the previous image objects storage space. After doing this do not use any references
      to the old image object anymore as they will be stale.

      ``x_scale`` controls how much the drawn image is scaled by in the x direction (float). If this
      value is negative the image will be flipped horizontally.

      ``y_scale`` controls how much the drawn image is scaled by in the y direction (float). If this
      value is negative the image will be flipped vertically.

      ``roi`` is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This
      allows you to extract just the pixels in the ROI to scale and draw on the destination image.

      ``rgb_channel`` is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed)
      and to render onto the destination image. For example, if you pass ``rgb_channel=1`` this will
      extract the green channel of the source RGB565 image and draw that in grayscale on the
      destination image.

      ``alpha`` controls how much of the source image to blend into the destination image. A value of
      256 draws an opaque source image while a value lower than 256 produces a blend between the source
      and destination image. 0 results in no modification to the destination image.

      ``color_palette`` if not ``-1`` can be `sensor.PALETTE_RAINBOW`, `sensor.PALETTE_IRONBOW`, or
      a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of
      whatever the source image is. This is applied after ``rgb_channel`` extraction if used.

      ``alpha_palette`` if not ``-1`` can be a 256 pixel in total GRAYSCALE image to use as a alpha
      palette which modulates the ``alpha`` value of the source image being drawn at a pixel pixel
      level allowing you to precisely control the alpha value of pixels based on their grayscale value.
      A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes
      more transparent until 0. This is applied after ``rgb_channel`` extraction if used.

      ``hint`` can be a logical OR of the flags:

         * `image.AREA`: Use area scaling when downscaling versus the default of nearest neighbor.
         * `image.BILINEAR`: Use bilinear scaling versus the default of nearest neighbor scaling.
         * `image.BICUBIC`: Use bicubic scaling versus the default of nearest neighbor scaling.
         * `image.CENTER`: Center the image image being draw on (x, y).
         * `image.EXTRACT_RGB_CHANNEL_FIRST`: Do rgb_channel extraction before scaling.
         * `image.APPLY_COLOR_PALETTE_FIRST`: Apply color palette before scaling.
         * `image.BLACK_BACKGROUND`: Assume the destination image is black. This speeds up drawing.

      ``x_size`` may be passed if ``x_scale`` is not passed to specify the size of the image to draw
      and ``x_scale`` will automatically be determined passed on the input image size. If neither
      ``y_scale`` or ``y_size`` are specified then ``y_scale`` internally will be set to be equal to
      ``x_size`` to maintain the aspect-ratio.

      ``y_size`` may be passed if ``y_scale`` is not passed to specify the size of the image to draw
      and ``y_scale`` will automatically be determined passed on the input image size. If neither
      ``x_scale`` or ``x_size`` are specified then ``x_scale`` internally will be set to be equal to
      ``y_size`` to maintain the aspect-ratio.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images."""

   def to_rgb565(self, x_scale: Optional[float] = ..., y_scale: Optional[float] = ..., roi: Optional[tuple[int, int, int, int]] = ..., rgb_channel: Optional[int] = ..., alpha: Optional[int] = ..., color_palette: Color_palette = ..., alpha_palette: Optional[int] = ..., hint: Optional[Conversion_hints] = ..., x_size: Optional[int] = ..., y_size: Optional[int] = ..., copy: Optional[bool] = ...) -> Image:
      """Converts an image to an RGB565 image (16-bits per pixel). If ``copy`` is False
      this method will try to modify the image in-place. If ``copy`` is True then
      this method will return a new image copy allocated on the heap.

      ``copy`` may also be another image object, which in this case this method will try to
      re-use that image objects storage space and will return a new image object that uses
      the previous image objects storage space. After doing this do not use any references
      to the old image object anymore as they will be stale.

      ``x_scale`` controls how much the drawn image is scaled by in the x direction (float). If this
      value is negative the image will be flipped horizontally.

      ``y_scale`` controls how much the drawn image is scaled by in the y direction (float). If this
      value is negative the image will be flipped vertically.

      ``roi`` is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This
      allows you to extract just the pixels in the ROI to scale and draw on the destination image.

      ``rgb_channel`` is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed)
      and to render onto the destination image. For example, if you pass ``rgb_channel=1`` this will
      extract the green channel of the source RGB565 image and draw that in grayscale on the
      destination image.

      ``alpha`` controls how much of the source image to blend into the destination image. A value of
      256 draws an opaque source image while a value lower than 256 produces a blend between the source
      and destination image. 0 results in no modification to the destination image.

      ``color_palette`` if not ``-1`` can be `sensor.PALETTE_RAINBOW`, `sensor.PALETTE_IRONBOW`, or
      a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of
      whatever the source image is. This is applied after ``rgb_channel`` extraction if used.

      ``alpha_palette`` if not ``-1`` can be a 256 pixel in total GRAYSCALE image to use as a alpha
      palette which modulates the ``alpha`` value of the source image being drawn at a pixel pixel
      level allowing you to precisely control the alpha value of pixels based on their grayscale value.
      A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes
      more transparent until 0. This is applied after ``rgb_channel`` extraction if used.

      ``hint`` can be a logical OR of the flags:

         * `image.AREA`: Use area scaling when downscaling versus the default of nearest neighbor.
         * `image.BILINEAR`: Use bilinear scaling versus the default of nearest neighbor scaling.
         * `image.BICUBIC`: Use bicubic scaling versus the default of nearest neighbor scaling.
         * `image.CENTER`: Center the image image being draw on (x, y).
         * `image.EXTRACT_RGB_CHANNEL_FIRST`: Do rgb_channel extraction before scaling.
         * `image.APPLY_COLOR_PALETTE_FIRST`: Apply color palette before scaling.
         * `image.BLACK_BACKGROUND`: Assume the destination image is black. This speeds up drawing.

      ``x_size`` may be passed if ``x_scale`` is not passed to specify the size of the image to draw
      and ``x_scale`` will automatically be determined passed on the input image size. If neither
      ``y_scale`` or ``y_size`` are specified then ``y_scale`` internally will be set to be equal to
      ``x_size`` to maintain the aspect-ratio.

      ``y_size`` may be passed if ``y_scale`` is not passed to specify the size of the image to draw
      and ``y_scale`` will automatically be determined passed on the input image size. If neither
      ``x_scale`` or ``x_size`` are specified then ``x_scale`` internally will be set to be equal to
      ``y_size`` to maintain the aspect-ratio.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images."""

   def to_rainbow(self, x_scale: Optional[float] = ..., y_scale: Optional[float] = ..., roi: Optional[tuple[int, int, int, int]] = ..., rgb_channel: Optional[int] = ..., alpha: Optional[int] = ..., color_palette: Color_palette = ..., alpha_palette: Optional[int] = ..., hint: Optional[Conversion_hints] = ..., x_size: Optional[int] = ..., y_size: Optional[int] = ..., copy: Optional[bool] = ...) -> Image:
      """
      Converts an image to an RGB565 rainbow image (16-bits per pixel). If ``copy`` is False
      this method will try to modify the image in-place. If ``copy`` is True then
      this method will return a new image copy allocated on the heap.

      ``copy`` may also be another image object, which in this case this method will try to
      re-use that image objects storage space and will return a new image object that uses
      the previous image objects storage space. After doing this do not use any references
      to the old image object anymore as they will be stale.

      ``x_scale`` controls how much the drawn image is scaled by in the x direction (float). If this
      value is negative the image will be flipped horizontally.

      ``y_scale`` controls how much the drawn image is scaled by in the y direction (float). If this
      value is negative the image will be flipped vertically.

      ``roi`` is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This
      allows you to extract just the pixels in the ROI to scale and draw on the destination image.

      ``rgb_channel`` is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed)
      and to render onto the destination image. For example, if you pass ``rgb_channel=1`` this will
      extract the green channel of the source RGB565 image and draw that in grayscale on the
      destination image.

      ``alpha`` controls how much of the source image to blend into the destination image. A value of
      256 draws an opaque source image while a value lower than 256 produces a blend between the source
      and destination image. 0 results in no modification to the destination image.

      ``color_palette`` if not ``-1`` can be `sensor.PALETTE_RAINBOW`, `sensor.PALETTE_IRONBOW`, or
      a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of
      whatever the source image is. This is applied after ``rgb_channel`` extraction if used.

      ``alpha_palette`` if not ``-1`` can be a 256 pixel in total GRAYSCALE image to use as a alpha
      palette which modulates the ``alpha`` value of the source image being drawn at a pixel pixel
      level allowing you to precisely control the alpha value of pixels based on their grayscale value.
      A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes
      more transparent until 0. This is applied after ``rgb_channel`` extraction if used.

      ``hint`` can be a logical OR of the flags:

         * `image.AREA`: Use area scaling when downscaling versus the default of nearest neighbor.
         * `image.BILINEAR`: Use bilinear scaling versus the default of nearest neighbor scaling.
         * `image.BICUBIC`: Use bicubic scaling versus the default of nearest neighbor scaling.
         * `image.CENTER`: Center the image image being draw on (x, y).
         * `image.EXTRACT_RGB_CHANNEL_FIRST`: Do rgb_channel extraction before scaling.
         * `image.APPLY_COLOR_PALETTE_FIRST`: Apply color palette before scaling.
         * `image.BLACK_BACKGROUND`: Assume the destination image is black. This speeds up drawing.

      ``x_size`` may be passed if ``x_scale`` is not passed to specify the size of the image to draw
      and ``x_scale`` will automatically be determined passed on the input image size. If neither
      ``y_scale`` or ``y_size`` are specified then ``y_scale`` internally will be set to be equal to
      ``x_size`` to maintain the aspect-ratio.

      ``y_size`` may be passed if ``y_scale`` is not passed to specify the size of the image to draw
      and ``y_scale`` will automatically be determined passed on the input image size. If neither
      ``x_scale`` or ``x_size`` are specified then ``x_scale`` internally will be set to be equal to
      ``y_size`` to maintain the aspect-ratio.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images."""

   def compress(self, quality: int) -> Image:"""JPEG compresses the image in place. Use this method versus `image.compressed()`
      to save heap space and to use a higher ``quality`` for compression at the
      cost of destroying the original image.

      Returns the image object so you can call another method using ``.`` notation.

      ``quality`` is the compression quality (0-100) (int).

      Returns the compressed image if called on a compressed image."""

   def compress_for_ide(self, quality: int) -> Image:"""JPEG compresses the image in place. Use this method versus `image.compressed()`
      to save heap space and to use a higher ``quality`` for compression at the
      cost of destroying the original image.

      This method JPEG compresses the image and then formats the JPEG data for
      transmission to OpenMV IDE to display by encoding every 6-bits as a byte
      valued between 128-191. This is done to prevent JPEG data from being
      misinterpreted as other text data in the byte stream.

      You need to use this method to format image data for display to terminal
      windows created via "Open Terminal" in OpenMV IDE.

      Returns the image object so you can call another method using ``.`` notation.

      ``quality`` is the compression quality (0-100) (int).

      Returns the image compressed for the IDE if called on a compressed image.
      Do not call this on an image already compressed for the IDE."""

   def compressed(self, quality: int) -> Image:"""Returns a JPEG compressed image - the original image is untouched. However,
      this method requires a somewhat large allocation of heap space so the image
      compression quality must be lower and the image resolution must be lower
      than what you could do with `image.compress()`.

      ``quality`` is the compression quality (0-100) (int).

      Returns a compressed image copy if called on a compressed image."""

   def compressed_for_ide(self, quality: int) -> Image:"""Returns a JPEG compressed image - the original image is untouched. However,
      this method requires a somewhat large allocation of heap space so the image
      compression quality must be lower and the image resolution must be lower
      than what you could do with `image.compress()`.

      This method JPEG compresses the image and then formats the JPEG data for
      transmission to OpenMV IDE to display by encoding every 6-bits as a byte
      valued between 128-191. This is done to prevent JPEG data from being
      misinterpreted as other text data in the byte stream.

      You need to use this method to format image data for display to terminal
      windows created via "Open Terminal" in OpenMV IDE.

      ``quality`` is the compression quality (0-100) (int).

      Returns a image compressed for the IDE copy if called on a compressed image.
      Do not call this on an image already compressed for the IDE."""

   def jpeg_encode_for_ide(self) -> Image:"""This formats the JPEG data for transmission to OpenMV IDE to display by
         encoding every 6-bits as a byte valued between 128-191. This is done to
         prevent JPEG data from being misinterpreted as other text data in the byte
         stream. This method does the formatting in-place destroying the original
         JPEG image and returns the encoded jpeg image.

         You need to use this method to format image data for display to terminal
         windows created via "Open Terminal" in OpenMV IDE.

         Returns the image object so you can call another method using ``.`` notation.

         Only works on JPEG images."""

   def jpeg_encoded_for_ide(self) -> Image:"""This formats the JPEG data for transmission to OpenMV IDE to display by
      encoding every 6-bits as a byte valued between 128-191. This is done to
      prevent JPEG data from being misinterpreted as other text data in the byte
      stream. This method does the formatting out-of-place preserving the original
      JPEG image and returns a new encoded jpeg image.

      You need to use this method to format image data for display to terminal
      windows created via "Open Terminal" in OpenMV IDE.

      Returns the image object so you can call another method using ``.`` notation.

      Only works on JPEG images."""

   def copy(self, x_scale: Optional[float] = ..., y_scale: Optional[float] = ..., roi: Optional[tuple[int, int, int, int]] = ..., rgb_channel: Optional[int] = ..., alpha: Optional[int] = ..., color_palette: Color_palette = ..., alpha_palette: Optional[int] = ..., hint: Optional[Conversion_hints] = ..., x_size: Optional[int] = ..., y_size: Optional[int] = ..., copy_to_fb: Optional[bool] = ...) -> Image:
      """
      Creates a deep copy of the image object. If ``copy_to_fb`` is False then
      the new image is allocated on the MicroPython heap. However, the MicroPython heap is limited
      and may not have space to store the new image if exhausted. Instead, set ``copy_to_fb`` to
      True to set the frame buffer to the new image making this function work just like `sensor.snapshot()`.

      ``x_scale`` controls how much the drawn image is scaled by in the x direction (float). If this
      value is negative the image will be flipped horizontally.

      ``y_scale`` controls how much the drawn image is scaled by in the y direction (float). If this
      value is negative the image will be flipped vertically.

      ``roi`` is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This
      allows you to extract just the pixels in the ROI to scale and draw on the destination image.

      ``rgb_channel`` is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed)
      and to render onto the destination image. For example, if you pass ``rgb_channel=1`` this will
      extract the green channel of the source RGB565 image and draw that in grayscale on the
      destination image.

      ``alpha`` controls how much of the source image to blend into the destination image. A value of
      256 draws an opaque source image while a value lower than 256 produces a blend between the source
      and destination image. 0 results in no modification to the destination image.

      ``color_palette`` if not ``-1`` can be `sensor.PALETTE_RAINBOW`, `sensor.PALETTE_IRONBOW`, or
      a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of
      whatever the source image is. This is applied after ``rgb_channel`` extraction if used.

      ``alpha_palette`` if not ``-1`` can be a 256 pixel in total GRAYSCALE image to use as a alpha
      palette which modulates the ``alpha`` value of the source image being drawn at a pixel pixel
      level allowing you to precisely control the alpha value of pixels based on their grayscale value.
      A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes
      more transparent until 0. This is applied after ``rgb_channel`` extraction if used.

      ``hint`` can be a logical OR of the flags:

         * `image.AREA`: Use area scaling when downscaling versus the default of nearest neighbor.
         * `image.BILINEAR`: Use bilinear scaling versus the default of nearest neighbor scaling.
         * `image.BICUBIC`: Use bicubic scaling versus the default of nearest neighbor scaling.
         * `image.CENTER`: Center the image image being draw on (x, y).
         * `image.EXTRACT_RGB_CHANNEL_FIRST`: Do rgb_channel extraction before scaling.
         * `image.APPLY_COLOR_PALETTE_FIRST`: Apply color palette before scaling.
         * `image.BLACK_BACKGROUND`: Assume the destination image is black. This speeds up drawing.

      ``x_size`` may be passed if ``x_scale`` is not passed to specify the size of the image to draw
      and ``x_scale`` will automatically be determined passed on the input image size. If neither
      ``y_scale`` or ``y_size`` are specified then ``y_scale`` internally will be set to be equal to
      ``x_size`` to maintain the aspect-ratio.

      ``y_size`` may be passed if ``y_scale`` is not passed to specify the size of the image to draw
      and ``y_scale`` will automatically be determined passed on the input image size. If neither
      ``x_scale`` or ``x_size`` are specified then ``x_scale`` internally will be set to be equal to
      ``y_size`` to maintain the aspect-ratio.

      ``copy_to_fb`` may also be another image object if you want to replace that image object's memory
      buffer, type, width, and height with new image data.

      Note
      ----

         Any use of ``copy_to_fb`` invalidates the previous image object it overwrites. Do not use
         any references to previous image objects anymore it overwrites. Either for an image object
         referencing the frame buffer, frame buffer stack, or an image on the MicroPython heap.

      Returns the new image object.

      Not supported on compressed images."""

   def crop(self, x_scale: Optional[float] = ..., y_scale: Optional[float] = ..., roi: Optional[tuple[int, int, int, int]] = ..., rgb_channel: Optional[int] = ..., alpha: Optional[int] = ..., color_palette: Color_palette = ..., alpha_palette: Optional[int] = ..., hint: Optional[Conversion_hints] = ..., x_size: Optional[int] = ..., y_size: Optional[int] = ..., copy: Optional[bool] = ...) -> Image:
      """

      Modifies an image in-place without changing the underlying image type. If ``copy`` is False
      this method will try to modify the image in-place. If ``copy`` is True then
      this method will return a new image copy allocated on the heap.

      ``copy`` may also be another image object, which in this case this method will try to
      re-use that image objects storage space and will return a new image object that uses
      the previous image objects storage space. After doing this do not use any references
      to the old image object anymore as they will be stale.

      ``x_scale`` controls how much the drawn image is scaled by in the x direction (float). If this
      value is negative the image will be flipped horizontally.

      ``y_scale`` controls how much the drawn image is scaled by in the y direction (float). If this
      value is negative the image will be flipped vertically.

      ``roi`` is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This
      allows you to extract just the pixels in the ROI to scale and draw on the destination image.

      ``rgb_channel`` is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed)
      and to render onto the destination image. For example, if you pass ``rgb_channel=1`` this will
      extract the green channel of the source RGB565 image and draw that in grayscale on the
      destination image.

      ``alpha`` controls how much of the source image to blend into the destination image. A value of
      256 draws an opaque source image while a value lower than 256 produces a blend between the source
      and destination image. 0 results in no modification to the destination image.

      ``color_palette`` if not ``-1`` can be `sensor.PALETTE_RAINBOW`, `sensor.PALETTE_IRONBOW`, or
      a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of
      whatever the source image is. This is applied after ``rgb_channel`` extraction if used.

      ``alpha_palette`` if not ``-1`` can be a 256 pixel in total GRAYSCALE image to use as a alpha
      palette which modulates the ``alpha`` value of the source image being drawn at a pixel pixel
      level allowing you to precisely control the alpha value of pixels based on their grayscale value.
      A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes
      more transparent until 0. This is applied after ``rgb_channel`` extraction if used.

      ``hint`` can be a logical OR of the flags:

         * `image.AREA`: Use area scaling when downscaling versus the default of nearest neighbor.
         * `image.BILINEAR`: Use bilinear scaling versus the default of nearest neighbor scaling.
         * `image.BICUBIC`: Use bicubic scaling versus the default of nearest neighbor scaling.
         * `image.CENTER`: Center the image image being draw on (x, y).
         * `image.EXTRACT_RGB_CHANNEL_FIRST`: Do rgb_channel extraction before scaling.
         * `image.APPLY_COLOR_PALETTE_FIRST`: Apply color palette before scaling.
         * `image.BLACK_BACKGROUND`: Assume the destination image is black. This speeds up drawing.

      ``x_size`` may be passed if ``x_scale`` is not passed to specify the size of the image to draw
      and ``x_scale`` will automatically be determined passed on the input image size. If neither
      ``y_scale`` or ``y_size`` are specified then ``y_scale`` internally will be set to be equal to
      ``x_size`` to maintain the aspect-ratio.

      ``y_size`` may be passed if ``y_scale`` is not passed to specify the size of the image to draw
      and ``y_scale`` will automatically be determined passed on the input image size. If neither
      ``x_scale`` or ``x_size`` are specified then ``x_scale`` internally will be set to be equal to
      ``y_size`` to maintain the aspect-ratio.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images."""

   def scale(self, x_scale: Optional[float] = ..., y_scale: Optional[float] = ..., roi: Optional[tuple[int, int, int, int]] = ..., rgb_channel: Optional[int] = ..., alpha: Optional[int] = ..., color_palette: Color_palette = ..., alpha_palette: Optional[int] = ..., hint: Optional[Conversion_hints] = ..., x_size: Optional[int] = ..., y_size: Optional[int] = ..., copy_to_fb: Optional[bool] = ...) -> Image:
      """

      Modifies an image in-place without changing the underlying image type. If ``copy`` is False
      this method will try to modify the image in-place. If ``copy`` is True then
      this method will return a new image copy allocated on the heap.

      ``copy`` may also be another image object, which in this case this method will try to
      re-use that image objects storage space and will return a new image object that uses
      the previous image objects storage space. After doing this do not use any references
      to the old image object anymore as they will be stale.

      ``x_scale`` controls how much the drawn image is scaled by in the x direction (float). If this
      value is negative the image will be flipped horizontally.

      ``y_scale`` controls how much the drawn image is scaled by in the y direction (float). If this
      value is negative the image will be flipped vertically.

      ``roi`` is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This
      allows you to extract just the pixels in the ROI to scale and draw on the destination image.

      ``rgb_channel`` is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed)
      and to render onto the destination image. For example, if you pass ``rgb_channel=1`` this will
      extract the green channel of the source RGB565 image and draw that in grayscale on the
      destination image.

      ``alpha`` controls how much of the source image to blend into the destination image. A value of
      256 draws an opaque source image while a value lower than 256 produces a blend between the source
      and destination image. 0 results in no modification to the destination image.

      ``color_palette`` if not ``-1`` can be `sensor.PALETTE_RAINBOW`, `sensor.PALETTE_IRONBOW`, or
      a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of
      whatever the source image is. This is applied after ``rgb_channel`` extraction if used.

      ``alpha_palette`` if not ``-1`` can be a 256 pixel in total GRAYSCALE image to use as a alpha
      palette which modulates the ``alpha`` value of the source image being drawn at a pixel pixel
      level allowing you to precisely control the alpha value of pixels based on their grayscale value.
      A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes
      more transparent until 0. This is applied after ``rgb_channel`` extraction if used.

      ``hint`` can be a logical OR of the flags:

         * `image.AREA`: Use area scaling when downscaling versus the default of nearest neighbor.
         * `image.BILINEAR`: Use bilinear scaling versus the default of nearest neighbor scaling.
         * `image.BICUBIC`: Use bicubic scaling versus the default of nearest neighbor scaling.
         * `image.CENTER`: Center the image image being draw on (x, y).
         * `image.EXTRACT_RGB_CHANNEL_FIRST`: Do rgb_channel extraction before scaling.
         * `image.APPLY_COLOR_PALETTE_FIRST`: Apply color palette before scaling.
         * `image.BLACK_BACKGROUND`: Assume the destination image is black. This speeds up drawing.

      ``x_size`` may be passed if ``x_scale`` is not passed to specify the size of the image to draw
      and ``x_scale`` will automatically be determined passed on the input image size. If neither
      ``y_scale`` or ``y_size`` are specified then ``y_scale`` internally will be set to be equal to
      ``x_size`` to maintain the aspect-ratio.

      ``y_size`` may be passed if ``y_scale`` is not passed to specify the size of the image to draw
      and ``y_scale`` will automatically be determined passed on the input image size. If neither
      ``x_scale`` or ``x_size`` are specified then ``x_scale`` internally will be set to be equal to
      ``y_size`` to maintain the aspect-ratio.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images."""

   def save(self, path: str, roi: Optional[tuple[int, int, int, int]] = ..., quality: Optional[int] = ...) -> Image:"""Saves a copy of the image to the filesystem at ``path``.

      Supports bmp/pgm/ppm/jpg/jpeg image files. Note that you cannot save jpeg
      compressed images to an uncompressed format.

      ``roi`` is the region-of-interest rectangle (x, y, w, h) to save from.
      If not specified, it is equal to the image rectangle which copies the entire
      image. This argument is not applicable for JPEG images.

      ``quality`` is the jpeg compression quality to use to save the image to jpeg
      format if the image is not already compressed (0-100) (int).

      Returns the image object so you can call another method using ``.`` notation."""

   def flush(self) -> None:"""Updates the frame buffer in the IDE with the image in the frame buffer on the camera."""

   def clear(self, mask: Optional[Image] = ...) -> Image:"""Sets all pixels in the image to zero (very fast).

      ``mask`` is another image to use as a pixel level mask for the operation.
      The mask should be an image with just black or white pixels and should be the
      same size as the image being operated on. Only pixels set in the mask are
      modified.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images."""

   def draw_line(self, x0:int, y0:int, x1:int, y1:int, color: Optional[Union[int, tuple[int, int, int]]] = ..., thickness: Optional[int] = ...) -> Image:"""Draws a line from (x0, y0) to (x1, y1) on the image. You may either
      pass x0, y0, x1, y1 separately or as a tuple (x0, y0, x1, y1).

      ``color`` is an RGB888 tuple for Grayscale or RGB565 images. Defaults to
      white. However, you may also pass the underlying pixel value (0-255) for
      grayscale images or a RGB565 value for RGB565 images.

      ``thickness`` controls how thick the line is in pixels.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images or bayer images."""

   def draw_rectangle(self, xywh_tuple_or_x: Union[int, tuple[int, int, int, int]], y:int=..., w:int=..., h:int=..., color: Optional[Union[int, tuple[int, int, int]]] = ..., thickness: Optional[int] = ..., fill:Optional[bool] = ...) -> Image:"""Draws a rectangle on the image. You may either pass x, y, w, h separately
      or as a tuple (x, y, w, h).

      ``color`` is an RGB888 tuple for Grayscale or RGB565 images. Defaults to
      white. However, you may also pass the underlying pixel value (0-255) for
      grayscale images or a RGB565 value for RGB565 images.

      ``thickness`` controls how thick the lines are in pixels.

      Pass ``fill`` set to True to fill the rectangle.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images or bayer images."""

   def draw_circle(self, x: int, y: int, radius: int, color: Optional[Union[int, tuple[int, int, int]]] = ..., thickness: Optional[int] = ..., fill:Optional[bool] = ...) -> Image:"""Draws a circle on the image. You may either pass x, y, radius separately or
      as a tuple (x, y, radius).

      ``color`` is an RGB888 tuple for Grayscale or RGB565 images. Defaults to
      white. However, you may also pass the underlying pixel value (0-255) for
      grayscale images or a RGB565 value for RGB565 images.

      ``thickness`` controls how thick the edges are in pixels.

      Pass ``fill`` set to True to fill the circle.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images or bayer images."""

   def draw_ellipse(self, cx:int, cy:int, rx:int, ry:int, rotation:int, color: Optional[Union[int, tuple[int, int, int]]] = ..., thickness: Optional[int] = ..., fill:Optional[bool] = ...) -> Image:"""Draws an ellipse on the image. You may either pass cx, cy, rx, ry, and the
      rotation (in degrees) separately or as a tuple (cx, yc, rx, ry, rotation).

      ``color`` is an RGB888 tuple for Grayscale or RGB565 images. Defaults to
      white. However, you may also pass the underlying pixel value (0-255) for
      grayscale images or a RGB565 value for RGB565 images.

      ``thickness`` controls how thick the edges are in pixels.

      Pass ``fill`` set to True to fill the ellipse.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images or bayer images."""

   def draw_string(self, xytuple_or_x:Union[tuple[int, int],int], y:int=..., text:str=..., color: Optional[Union[int, tuple[int, int, int]]] = ..., scale:int=..., x_spacing:int=..., y_spacing:int=..., mono_space:bool=..., char_rotation:int=..., char_hmirror:bool=..., char_vflip:bool=..., string_rotation:int=..., string_hmirror:bool=..., string_vflip:bool=...) -> Image:

      """Draws 8x10 text starting at location (x, y) in the image. You may either pass
      x, y separately or as a tuple (x, y).

      ``text`` is a string to write to the image. ``\n``, ``\r``, and ``\r\n``
      line endings move the cursor to the next line.

      ``color`` is an RGB888 tuple for Grayscale or RGB565 images. Defaults to
      white. However, you may also pass the underlying pixel value (0-255) for
      grayscale images or a RGB565 value for RGB565 images.

      ``scale`` may be increased to increase/decrease the size of the text on the
      image. You can pass greater than 0 integer or floating point values.

      ``x_spacing`` allows you to add (if positive) or subtract (if negative) x
      pixels between cahracters.

      ``y_spacing`` allows you to add (if positive) or subtract (if negative) y
      pixels between cahracters (for multi-line text).

      ``mono_space`` defaults to True which forces text to be fixed spaced. For
      large text scales this looks terrible. Set the False to get non-fixed width
      character spacing which looks A LOT better.

      ``char_rotation`` may be 0, 90, 180, 270 to rotate each character in the
      string by this amount.

      ``char_hmirror`` if True horizontally mirrors all characters in the string.

      ``char_vflip`` if True vertically flips all characters in the string.

      ``string_rotation`` may be 0, 90, 180, 270 to rotate the string by this
      amount.

      ``string_hmirror`` if True horizontally mirrors the string.

      ``string_vflip`` if True vertically flips the string.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images or bayer images."""

   def draw_cross(self, xytuple_or_x:Union[tuple[int, int],int], y:int=..., color:Union[tuple[int, int, int], int]=..., size:int=..., thickness:int=...) -> Image:"""Draws a cross at location x, y. You may either pass x, y separately or as a
      tuple (x, y).

      ``color`` is an RGB888 tuple for Grayscale or RGB565 images. Defaults to
      white. However, you may also pass the underlying pixel value (0-255) for
      grayscale images or a RGB565 value for RGB565 images.

      ``size`` controls how long the lines of the cross extend.

      ``thickness`` controls how thick the edges are in pixels.

      Returns the image object so you can call another method using ``.`` notation.

      Not supported on compressed images or bayer images."""

   # def draw_arrow(self, x0, y0, x1, y1, [color, [thickness=1]]) -> Image:"""Draws an arrow from (x0, y0) to (x1, y1) on the image. You may
   #    either pass x0, y0, x1, y1 separately or as a tuple (x0, y0, x1, y1).

   #    ``color`` is an RGB888 tuple for Grayscale or RGB565 images. Defaults to
   #    white. However, you may also pass the underlying pixel value (0-255) for
   #    grayscale images or a RGB565 value for RGB565 images.

   #    ``thickness`` controls how thick the line is in pixels.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def draw_edges(self, image, corners, [color, [size=0, [thickness=1, [fill=False]]]]) -> Image:"""Draws line edges between a corner list returned by methods like `blob.corners`. Coners is
   #    a four valued tuple of two valued x/y tuples. E.g. [(x1,y1),(x2,y2),(x3,y3),(x4,y4)].

   #    ``color`` is an RGB888 tuple for Grayscale or RGB565 images. Defaults to
   #    white. However, you may also pass the underlying pixel value (0-255) for
   #    grayscale images or a RGB565 value for RGB565 images.

   #    ``size`` if greater than 0 causes the corners to be drawn as circles of radius ``size``.

   #    ``thickness`` controls how thick the line is in pixels.

   #    Pass ``fill`` set to True to fill the corner circles if drawn.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def draw_image(self, image, x:int, y:int, [x_scale=1.0, [y_scale=1.0, [roi=None, [rgb_channel=-1, [alpha=256, [color_palette=None, [alpha_palette=None, [hint=0, [x_size=None,  -> Image:"""None]]]]]]]]]])

   #    Draws an ``image`` whose top-left corner starts at location x, y. You may either pass x, y
   #    separately or as a tuple (x, y). This method automatically handles rendering the image passed
   #    into the correct pixel format for the destination image while also handling clipping seamlessly.

   #    ``x_scale`` controls how much the drawn image is scaled by in the x direction (float). If this
   #    value is negative the image will be flipped horizontally.

   #    ``y_scale`` controls how much the drawn image is scaled by in the y direction (float). If this
   #    value is negative the image will be flipped vertically.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This
   #    allows you to extract just the pixels in the ROI to scale and draw on the destination image.

   #    ``rgb_channel`` is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed)
   #    and to render onto the destination image. For example, if you pass ``rgb_channel=1`` this will
   #    extract the green channel of the source RGB565 image and draw that in grayscale on the
   #    destination image.

   #    ``alpha`` controls how much of the source image to blend into the destination image. A value of
   #    256 draws an opaque source image while a value lower than 256 produces a blend between the source
   #    and destination image. 0 results in no modification to the destination image.

   #    ``color_palette`` if not ``-1`` can be `sensor.PALETTE_RAINBOW`, `sensor.PALETTE_IRONBOW`, or
   #    a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of
   #    whatever the source image is. This is applied after ``rgb_channel`` extraction if used.

   #    ``alpha_palette`` if not ``-1`` can be a 256 pixel in total GRAYSCALE image to use as a alpha
   #    palette which modulates the ``alpha`` value of the source image being drawn at a pixel pixel
   #    level allowing you to precisely control the alpha value of pixels based on their grayscale value.
   #    A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes
   #    more transparent until 0. This is applied after ``rgb_channel`` extraction if used.

   #    ``hint`` can be a logical OR of the flags:

   #       * `image.AREA`: Use area scaling when downscaling versus the default of nearest neighbor.
   #       * `image.BILINEAR`: Use bilinear scaling versus the default of nearest neighbor scaling.
   #       * `image.BICUBIC`: Use bicubic scaling versus the default of nearest neighbor scaling.
   #       * `image.CENTER`: Center the image image being draw on (x, y).
   #       * `image.EXTRACT_RGB_CHANNEL_FIRST`: Do rgb_channel extraction before scaling.
   #       * `image.APPLY_COLOR_PALETTE_FIRST`: Apply color palette before scaling.
   #       * `image.BLACK_BACKGROUND`: Assume the destination image is black. This speeds up drawing.

   #    ``x_size`` may be passed if ``x_scale`` is not passed to specify the size of the image to draw
   #    and ``x_scale`` will automatically be determined passed on the input image size. If neither
   #    ``y_scale`` or ``y_size`` are specified then ``y_scale`` internally will be set to be equal to
   #    ``x_size`` to maintain the aspect-ratio.

   #    ``y_size`` may be passed if ``y_scale`` is not passed to specify the size of the image to draw
   #    and ``y_scale`` will automatically be determined passed on the input image size. If neither
   #    ``x_scale`` or ``x_size`` are specified then ``x_scale`` internally will be set to be equal to
   #    ``y_size`` to maintain the aspect-ratio.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images."""

   # def draw_keypoints(self, keypoints, [color, [size=10, [thickness=1, [fill=False]]]]) -> Image:"""Draws the keypoints of a keypoints object on the image. You may also pass a
   #    list of three value tuples containing the (x, y, rotation_angle_in_degrees) to
   #    re-use this method for drawing keypoint glyphs which are a cirle with a line
   #    pointing in a particular direction.

   #    ``color`` is an RGB888 tuple for Grayscale or RGB565 images. Defaults to
   #    white. However, you may also pass the underlying pixel value (0-255) for
   #    grayscale images or a RGB565 value for RGB565 images.

   #    ``size`` controls how large the keypoints are.

   #    ``thickness`` controls how thick the line is in pixels.

   #    Pass ``fill`` set to True to fill the keypoints.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def flood_fill(self, x:int, y:int, [seed_threshold=0.05, [floating_threshold=0.05, [color, [invert=False, [clear_background=False, [mask=None]]]]]]) -> Image:"""Flood fills a region of the image starting from location x, y. You may either
   #    pass x, y separately or as a tuple (x, y).

   #    ``seed_threshold`` controls how different any pixel in the fill area may be
   #    from the original starting pixel.

   #    ``floating_threshold`` controls how different any pixel in the fill area may
   #    be from any neighbor pixels.

   #    ``color`` is an RGB888 tuple for Grayscale or RGB565 images. Defaults to
   #    white. However, you may also pass the underlying pixel value (0-255) for
   #    grayscale images or a RGB565 value for RGB565 images.

   #    Pass ``invert`` as True to re-color everything outside of the flood-fill
   #    connected area.

   #    Pass ``clear_background`` as True to zero the rest of the pixels that
   #    flood-fill did not re-color.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    evaluated when flood filling.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def mask_rectange(self, [x, y, w, h]) -> Image:"""Zeros a rectangular part of the image. If no arguments are supplied this
   #    method zeros the center of the image.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def mask_circle(self, [x, y, radius]) -> Image:"""Zeros a circular part of the image. If no arguments are supplied this
   #    method zeros the center of the image.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def mask_ellipse(self, [x, y, radius_x, radius_y, rotation_angle_in_degrees]) -> Image:"""Zeros an ellipsed shaped part of the image. If no arguments are supplied this
   #    method zeros the center of the image.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def binary(self, thresholds, [invert=False, [zero=False, [mask=None, [to_bitmap=False, [copy=False]]]]]) -> Image:"""Sets all pixels in the image to black or white depending on if the pixel
   #    is inside of a threshold in the threshold list ``thresholds`` or not.

   #    ``thresholds`` must be a list of tuples ``[(lo, hi), (lo, hi), ..., (lo, hi)]``
   #    defining the ranges of color you want to track. For grayscale images each tuple
   #    needs to contain two values - a min grayscale value and a max grayscale value.
   #    Only pixel regions that fall between these thresholds will be considered.
   #    For RGB565 images each tuple needs to have six values (l_lo, l_hi, a_lo, a_hi, b_lo, b_hi)
   #    - which are minimums and maximums for the LAB L, A, and B channels respectively.
   #    For easy usage this function will automatically fix swapped min and max values.
   #    Additionally, if a tuple is larger than six values the rest are ignored.
   #    Conversely, if the tuple is too short the rest of the thresholds are assumed
   #    to be at maximum range.

   #    Note
   #    ----

   #       To get the thresholds for the object you want to track just select (click
   #       and drag) on the object you want to track in the IDE frame buffer. The
   #       histogram will then update to just be in that area. Then just write down
   #       where the color distribution starts and falls off in each histogram channel.
   #       These will be your low and high values for ``thresholds``. It's best to
   #       manually determine the thresholds versus using the upper and lower
   #       quartile statistics because they are too tight.

   #       You may also determine color thresholds by going into
   #       ``Tools->Machine Vision->Threshold Editor`` in OpenMV IDE and selecting
   #       thresholds from the GUI slider window.

   #    ``invert`` inverts the thresholding operation such that instead of matching
   #    pixels inside of some known color bounds pixels are matched that are outside
   #    of the known color bounds.

   #    Set ``zero`` to True to instead zero thresholded pixels and leave pixels
   #    not in the threshold list untouched.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    ``to_bitmap`` turns the image data into a binary bitmap image where each
   #    pixel is stored in 1 bit. For very small images the new bitmap image may
   #    not fit inside of the original image requiring an out-of-place operation
   #    using ``copy``.

   #    ``copy`` if True creates a copy of the binarized image on the heap versus
   #    modifying the source image.

   #    Note
   #    ----

   #       Bitmap images are like grayscale images with only two pixels values - 0
   #       and 1. Additionally, bitmap images are packed such that they only store
   #       1 bit per pixel making them very small. The OpenMV image library allows
   #       bitmap images to be used in all places `sensor.GRAYSCALE` and `sensor.RGB565` images
   #       can be used. However, many operations when applied on bitmap images don't
   #       make any sense becuase bitmap images only have 2 values. OpenMV recommends
   #       using bitmap images for ``mask`` values in operations and such as they
   #       fit on the MicroPython heap quite easily. Finally, bitmap image pixel values
   #       0 and 1 are interpreted as black and white when being applied to `sensor.GRAYSCALE`
   #       or `sensor.RGB565` images. The library automatically handles conversion.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def invert(self, ) -> Image:"""Flips (binary inverts) all pixels values in a binary image very quickly.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def b_and(self, image, [mask=None]) -> Image:"""Logically ANDs this image with another image.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def b_nand(self, image, [mask=None]) -> Image:"""Logically NANDs this image with another image.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def b_or(self, image, [mask=None]) -> Image:"""Logically ORs this image with another image.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def b_nor(self, image, [mask=None]) -> Image:"""Logically NORs this image with another image.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def b_xor(self, image, [mask=None]) -> Image:"""Logically XORs this image with another image.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def b_xnor(self, image, [mask=None]) -> Image:"""Logically XNORs this image with another image.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def erode(self, size, [threshold, [mask=None]]) -> Image:"""Removes pixels from the edges of segmented areas.

   #    This method works by convolving a kernel of ((size*2)+1)x((size*2)+1) pixels
   #    across the image and zeroing the center pixel of the kernel if the sum of
   #    the neighbour pixels set is not greater than ``threshold``.

   #    This method works like the standard erode method if threshold is not set. If
   #    ``threshold`` is set then you can specify erode to only erode pixels that
   #    have, for example, less than 2 pixels set around them with a threshold of 2.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def dilate(self, size, [threshold, [mask=None]]) -> Image:"""Adds pixels to the edges of segmented areas.

   #    This method works by convolving a kernel of ((size*2)+1)x((size*2)+1) pixels
   #    across the image and setting the center pixel of the kernel if the sum of
   #    the neighbour pixels set is greater than ``threshold``.

   #    This method works like the standard dilate method if threshold is not set.
   #    If ``threshold`` is set then you can specify dilate to only dilate pixels
   #    that have, for example, more than 2 pixels set around them with a threshold
   #    of 2.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def open(self, size, [threshold, [mask=None]]) -> Image:"""Performs erosion and dilation on an image in order. Please see `image.erode()`
   #    and `image.dilate()` for more information.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def close(self, size, [threshold, [mask=None]]) -> Image:"""Performs dilation and erosion on an image in order. Please see `image.dilate()`
   #    and `image.erode()` for more information.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def top_hat(self, size, [threshold, [mask=None]]) -> Image:"""Returns the image difference of the image and `image.open()`'ed image.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Not supported on compressed images or bayer images."""

   # def black_hat(self, size, [threshold, [mask=None]]) -> Image:"""Returns the image difference of the image and `image.close()`'ed image.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Not supported on compressed images or bayer images."""

   # def gamma_corr(self, [gamma=1.0, [contrast=1.0, [brightness=0.0]) -> Image:"""Quickly changes the image gamma, contrast, and brightness. Please use this
   #    method instead of `image.mul` or `image.div` which are meant for blending to
   #    adjust pixels values.

   #    ``gamma`` with values greater than 1.0 makes the image darker in a non-linear
   #    manner while less than 1.0 makes the image brighter. The gamma value is applied
   #    to the image by scaling all pixel color channels to be between [0:1) and then
   #    doing a remapping of ``pow(pixel, 1/gamma)`` on all pixels before scaling back.

   #    ``contrast`` with values greater than 1.0 makes the image brighter in a linear
   #    manner while less than 1.0 makes the image darker. The contrast value is applied
   #    to the image by scaling all pixel color channels to be between [0:1) and then
   #    doing a remapping of ``pixel * contrast`` on all pixels before scaling back.

   #    ``brightness`` with values greater than 0.0 makes the image brighter in a constant
   #    manner while less than 0.0 makes the image darker. The brightness value is applied
   #    to the image by scaling all pixel color channels to be between [0:1) and then
   #    doing a remapping of ``pixel + brightness`` on all pixels before scaling back.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def negate(self, ) -> Image:"""Flips (numerically inverts) all pixels values in an image very quickly. E.g.
   #    for GRAYSCALE images this method changes all pixels from ``pixel`` to ``255 - pixel``.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def replace(self, image, [hmirror=False, [vflip=False, [transpose=False, [mask=None]]]]) -> Image:"""Replaces all pixels in the image object with a new image.

   #    ``image`` can either be another image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    Set ``hmirror`` to True to horizontally mirror the replacing image.

   #    Set ``vflip`` to True to vertically flip the replacing image.

   #    Set ``transpose`` to True to flip the image along the diagonal (this changes
   #    the image image width/height if the image is non-square).

   #    If you want to rotate an image by multiples of 90 degrees pass the following:

   #       * vflip=False, hmirror=False, transpose=False -> 0 degree rotation
   #       * vflip=True,  hmirror=False, transpose=True  -> 90 degree rotation
   #       * vflip=True,  hmirror=True,  transpose=False -> 180 degree rotation
   #       * vflip=False, hmirror=True,  transpose=True  -> 270 degree rotation

   #    Note
   #    ----

   #       If you don't pass an ``image`` this method will operate on the underlying
   #       image that you were going to replace by applying the ``hmirror``, ``vflip``,
   #       and ``transpose`` options to rotate the image around. E.g. if you want
   #       to do ``img.replace(img, etc...)`` you just need to do ``img.replace(etc..)``.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified. Note that the mask is applied on the image before hmirror/vflip/transpose
   #    so the mask should be the same width/height of the initial unmodifed image.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def assign(self, image, [hmirror=False, [vflip=False, [transpose=False, [mask=None]]]]) -> Image:"""Alias for `image.replace`."""

   # def set(self, image, [hmirror=False, [vflip=False, [transpose=False, [mask=None]]]]) -> Image:"""Alias for `image.replace`."""

   # def add(self, image, [mask=None]) -> Image:"""Adds an image pixel-wise to this one.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def sub(self, image, [reverse=False, [mask=None]]) -> Image:"""Subtracts an image pixel-wise to this one.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    Set ``reverse`` to True to reverse the subtraction operation from
   #    ``this_image-image`` to ``image-this_image``.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def mul(self, image, [invert=False, [mask=None]]) -> Image:"""Multiplies two images pixel-wise with each other.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    Set ``invert`` to True to change the multiplication operation from ``a*b``
   #    to ``1/((1/a)*(1/b))``. In particular, this lightens the image instead of
   #    darkening it (e.g. multiply versus burn operations).

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images.

   #    Note
   #    ----

   #       This method is meant for image blending and cannot multiply the pixels in
   #       the image by a scalar like ``2``. Use `image.gamma_corr` for that."""

   # def div(self, image, [invert=False, [mod=False, [mask=None]]]) -> Image:"""Divides this image by another one.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    Set ``invert`` to True to change the division direction from ``a/b`` to
   #    ``b/a``.

   #    Set ``mod`` to True to change the division operation to the modulus operation.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images.

   #    Note
   #    ----

   #       This method is meant for image blending and cannot divide the pixels in
   #       the image by a scalar like ``2``. Use `image.gamma_corr` for that."""

   # def min(self, image, [mask=None]) -> Image:"""Returns the minimum image of two images pixel-wise.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def max(self, image, [mask=None]) -> Image:"""Returns the maximum image of two images pixel-wise.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def difference(self, image, [mask=None]) -> Image:"""Returns the absolute difference image between two images (e.g. ||a-b||).

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def blend(self, image, [alpha=128, [mask=None]]) -> Image:"""Alpha blends two images with each other.

   #    ``image`` can either be an image object, a path to an uncompressed image
   #    file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can
   #    either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale
   #    for grayscale images or a RGB565 value for RGB images).

   #    ``alpha`` controls how much of the other image to blend into this image.
   #    ``alpha`` should be an integer value between 0 and 256. A value closer to
   #    zero blends more of the other image into this image and a value closer to
   #    256 does the opposite.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def histeq(self, [adaptive=False, [clip_limit=-1, [mask=None]]]) -> Image:"""Runs the histogram equalization algorithm on the image. Histogram
   #    equalization normalizes the contrast and brightness in the image.

   #    If you pass ``adaptive`` as True then an adaptive histogram equalization
   #    method will be run on the image instead which as generally better results
   #    than non-adaptive histogram qualization but a longer run time.

   #    ``clip_limit`` provides a way to limit the contrast of the adaptive histogram
   #    qualization. Use a small value for this, like 10, to produce good histogram
   #    equalized contrast limited images.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def mean(self, size, [threshold=False, [offset=0, [invert=False, [mask=None]]]]]) -> Image:"""Standard mean blurring filter using a box filter.

   #    ``size`` is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.

   #    If you'd like to adaptive threshold the image on the output of the filter
   #    you can pass ``threshold=True`` which will enable adaptive thresholding of the
   #    image which sets pixels to one or zero based on a pixel's brightness in relation
   #    to the brightness of the kernel of pixels around them. A negative ``offset``
   #    value sets more pixels to 1 as you make it more negative while a positive
   #    value only sets the sharpest contrast changes to 1. Set ``invert`` to invert
   #    the binary image resulting output.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def size,self,  [percentile=0.5, [threshold=False, [offset=0, [invert=False, [mask=None]]]]]) -> Image:"""Runs the median filter on the image. The median filter is the best filter
   #    for smoothing surfaces while preserving edges but it is very slow.

   #    ``size`` is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.

   #    ``percentile`` controls the percentile of the value used in the kernel. By
   #    default each pixel is replaced with the 50th percentile (center) of its
   #    neighbors. You can set this to 0 for a min filter, 0.25 for a lower quartile
   #    filter, 0.75 for an upper quartile filter, and 1.0 for a max filter.

   #    If you'd like to adaptive threshold the image on the output of the filter
   #    you can pass ``threshold=True`` which will enable adaptive thresholding of the
   #    image which sets pixels to one or zero based on a pixel's brightness in relation
   #    to the brightness of the kernel of pixels around them. A negative ``offset``
   #    value sets more pixels to 1 as you make it more negative while a positive
   #    value only sets the sharpest contrast changes to 1. Set ``invert`` to invert
   #    the binary image resulting output.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def mode(self, size, [threshold=False, [offset=0, [invert=False, [mask=None]]]]]) -> Image:"""Runs the mode filter on the image by replacing each pixel with the mode of
   #    their neighbors. This method works great on grayscale images. However, on
   #    RGB images it creates a lot of artifacts on edges because of the non-linear
   #    nature of the operation.

   #    ``size`` is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.

   #    If you'd like to adaptive threshold the image on the output of the filter
   #    you can pass ``threshold=True`` which will enable adaptive thresholding of the
   #    image which sets pixels to one or zero based on a pixel's brightness in relation
   #    to the brightness of the kernel of pixels around them. A negative ``offset``
   #    value sets more pixels to 1 as you make it more negative while a positive
   #    value only sets the sharpest contrast changes to 1. Set ``invert`` to invert
   #    the binary image resulting output.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def midpoint(self, size, [bias=0.5, [threshold=False, [offset=0, [invert=False, [mask=None]]]]]) -> Image:"""Runs the midpoint filter on the image. This filter finds the midpoint
   #    ((max-min)/2) of each pixel neighborhood in the image.

   #    ``size`` is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.

   #    ``bias`` controls the min/max mixing. 0 for min filtering only, 1.0 for max
   #    filtering only. By using the ``bias`` you can min/max filter the image.

   #    If you'd like to adaptive threshold the image on the output of the filter
   #    you can pass ``threshold=True`` which will enable adaptive thresholding of the
   #    image which sets pixels to one or zero based on a pixel's brightness in relation
   #    to the brightness of the kernel of pixels around them. A negative ``offset``
   #    value sets more pixels to 1 as you make it more negative while a positive
   #    value only sets the sharpest contrast changes to 1. Set ``invert`` to invert
   #    the binary image resulting output.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def morph(self, size, kernel, [mul, [add=0, [threshold=False, [offset=0, [invert=False, [mask=None]]]]]]) -> Image:"""Convolves the image by a filter kernel. This allows you to do general purpose
   #    convolutions on an image.

   #    ``size`` controls the size of the kernel which must be
   #    ((size*2)+1)x((size*2)+1) elements big.

   #    ``kernel`` is the kernel to convolve the image by. It can either be a tuple
   #    or a list of integer values.

   #    ``mul`` is number to multiply the convolution pixel results by. When not set
   #    it defaults to a value that will prevent scaling in the convolution output.

   #    ``add`` is a value to add to each convolution pixel result.

   #    ``mul`` basically allows you to do a global contrast adjustment and ``add``
   #    allows you to do a global brightness adjustment. Pixels that go outside of
   #    the image mins and maxes for color channels will be clipped.

   #    If you'd like to adaptive threshold the image on the output of the filter
   #    you can pass ``threshold=True`` which will enable adaptive thresholding of the
   #    image which sets pixels to one or zero based on a pixel's brightness in relation
   #    to the brightness of the kernel of pixels around them. A negative ``offset``
   #    value sets more pixels to 1 as you make it more negative while a positive
   #    value only sets the sharpest contrast changes to 1. Set ``invert`` to invert
   #    the binary image resulting output.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def gaussian(self, size, [unsharp=False, [mul, [add=0, [threshold=False, [offset=0, [invert=False, [mask=None]]]]]]]) -> Image:"""Convolves the image by a smoothing guassian kernel.

   #    ``size`` is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.

   #    If ``unsharp`` is set to the True then instead of doing just a guassian
   #    filtering operation this method will perform an unsharp mask operation which
   #    improves image sharpness on edges.

   #    ``mul`` is number to multiply the convolution pixel results by. When not set
   #    it defaults to a value that will prevent scaling in the convolution output.

   #    ``add`` is a value to add to each convolution pixel result.

   #    ``mul`` basically allows you to do a global contrast adjustment and ``add``
   #    allows you to do a global brightness adjustment. Pixels that go outside of
   #    the image mins and maxes for color channels will be clipped.

   #    If you'd like to adaptive threshold the image on the output of the filter
   #    you can pass ``threshold=True`` which will enable adaptive thresholding of the
   #    image which sets pixels to one or zero based on a pixel's brightness in relation
   #    to the brightness of the kernel of pixels around them. A negative ``offset``
   #    value sets more pixels to 1 as you make it more negative while a positive
   #    value only sets the sharpest contrast changes to 1. Set ``invert`` to invert
   #    the binary image resulting output.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # def laplacian(self, size, [sharpen=False, [mul, [add=0, [threshold=False, [offset=0, [invert=False, [mask=None]]]]]]]) -> Image:"""Convolves the image by a edge detecting laplacian kernel.

   #    ``size`` is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.

   #    If ``sharpen`` is set to the True then instead of just outputting an
   #    unthresholded edge detection image this method will instead sharpen the
   #    image. Increase the kernel size then to increase the image sharpness.

   #    ``mul`` is number to multiply the convolution pixel results by. When not set
   #    it defaults to a value that will prevent scaling in the convolution output.

   #    ``add`` is a value to add to each convolution pixel result.

   #    ``mul`` basically allows you to do a global contrast adjustment and ``add``
   #    allows you to do a global brightness adjustment. Pixels that go outside of
   #    the image mins and maxes for color channels will be clipped.

   #    If you'd like to adaptive threshold the image on the output of the filter
   #    you can pass ``threshold=True`` which will enable adaptive thresholding of the
   #    image which sets pixels to one or zero based on a pixel's brightness in relation
   #    to the brightness of the kernel of pixels around them. A negative ``offset``
   #    value sets more pixels to 1 as you make it more negative while a positive
   #    value only sets the sharpest contrast changes to 1. Set ``invert`` to invert
   #    the binary image resulting output.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def bilateral(self, size, [color_sigma=0.1, [space_sigma=1, [threshold=False, [offset=0, [invert=False, [mask=None]]]]]]) -> Image:"""Convolves the image by a bilateral filter. The bilateral filter smooths the
   #    image while keeping edges in the image.

   #    ``size`` is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.

   #    ``color_sigma`` controls how closely colors are matched using the bilateral
   #    filter. Increase this to increase color blurring.

   #    ``space_sigma`` controls how closely pixels space-wise are blurred with
   #    each other. Increase this to increase pixel blurring.

   #    If you'd like to adaptive threshold the image on the output of the filter
   #    you can pass ``threshold=True`` which will enable adaptive thresholding of the
   #    image which sets pixels to one or zero based on a pixel's brightness in relation
   #    to the brightness of the kernel of pixels around them. A negative ``offset``
   #    value sets more pixels to 1 as you make it more negative while a positive
   #    value only sets the sharpest contrast changes to 1. Set ``invert`` to invert
   #    the binary image resulting output.

   #    ``mask`` is another image to use as a pixel level mask for the operation.
   #    The mask should be an image with just black or white pixels and should be the
   #    same size as the image being operated on. Only pixels set in the mask are
   #    modified.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def linpolar(self, [reverse=False]) -> Image:"""Re-project's and image from cartessian coordinates to linear polar coordinates.

   #    Set ``reverse=True`` to re-project in the opposite direction.

   #    Linear polar re-projection turns rotation of an image into x-translation.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def logpolar(self, [reverse=False]) -> Image:"""Re-project's and image from cartessian coordinates to log polar coordinates.

   #    Set ``reverse=True`` to re-project in the opposite direction.

   #    Log polar re-projection turns rotation of an image into x-translation
   #    and scaling/zooming into y-translation.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def lens_corr(self, [strength=1.8, [zoom=1.0, [x_corr=0.0, [y_corr=0.0]]]]) -> Image:"""Performs lens correction to un-fisheye the image due to the lens distortion.

   #    ``strength`` is a float defining how much to un-fisheye the image. Try 1.8
   #    out by default and then increase or decrease from there until the image
   #    looks good.

   #    ``zoom`` is the amount to zoom in on the image by. 1.0 by default.

   #    ``x_corr`` floating point pixel offset from center. Can be negative or positive.

   #    ``y_corr`` floating point pixel offset from center. Can be negative or positive.

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images."""

   # .. def [x_rotation=self, 0.0, [y_rotation=0.0, [z_rotation=0.0, [x_translation=0.0, [y_translation=0.0, [zoom=1.0, [fov=60.0, [corners]]]]]]]]) -> Image:"""Corrects perspective issues in the image by doing a 3D rotation of the frame buffer.

   #    ``x_rotation`` is the number of degrees to rotation the image in the frame buffer
   #    around the x axis (i.e. this spins the image up and down).

   #    ``y_rotation`` is the number of degrees to rotation the image in the frame buffer
   #    around the y axis (i.e. this spins the image left and right).

   #    ``z_rotation`` is the number of degrees to rotation the image in the frame buffer
   #    around the z axis (i.e. this spins the image in place).

   #    ``x_translation`` is the number of units to move the image to the left or right
   #    after rotation. Because this translation is applied in 3D space the units aren't pixels...

   #    ``y_translation`` is the number of units to move the image to the up or down
   #    after rotation. Because this translation is applied in 3D space the units aren't pixels...

   #    ``zoom`` is the amount to zoom in on the image by. 1.0 by default.

   #    ``fov`` is the field-of-view to use internally when doing 2D->3D projection before
   #    rotating the image in 3D space. As this value approaches 0 the image is placed at infinity away
   #    from the viewport. As this value approaches 180 the image is placed within the viewport. Typically,
   #    you should not change this value but you can modify it to change the 2D->3D mapping effect.

   #    ``corners`` is a list of four (x,y) tuples representing four corners used to create a 4-point
   #    correspondence homography that will map the first corner to (0, 0), the second corner to
   #    (image_width-1, 0), the third corner to (image_width-1, image_height-1), and the fourth corner
   #    to (0, image_height-1). The 3D rotation is then applied after the image is re-mapped. This
   #    argument lets you use `rotation_corr` to do things like birds-eye-view transforms. E.g::

   #        top_tilt = 10 # if the difference between top/bottom_tilt become to large this method will stop working
   #        bottom_tilt = 0

   #        points = [(tilt, 0), (img.width()-tilt, 0), (img.width()-1-bottom_tilt, img.height()-1), (bottom_tilt, img.height()-1)]

   #        img.rotation_corr(corners=points)

   #    Returns the image object so you can call another method using ``.`` notation.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   def get_histogram(self, thresholds: Optional[list[tuple[int, int]]] = ..., invert: bool = ..., roi: tuple[int, int, int, int] = ..., bins: int = ..., l_bins: int = ..., a_bins: int = ..., b_bins: int = ..., difference: Image = ...) -> histogram:"""Computes the normalized histogram on all color channels for an ``roi`` and
      returns a `image.histogram` object. Please see the `image.histogram` object for more
      information. You can also invoke this method by using ``image.get_hist()`` or
      ``image.histogram()``. If you pass a list of ``thresholds`` then the histogram
      information will only be computed from pixels within the threshold list.

      ``thresholds`` must be a list of tuples
      ``[(lo, hi), (lo, hi), ..., (lo, hi)]`` defining the ranges of color you
      want to track. For
      grayscale images each tuple needs to contain two values - a min grayscale
      value and a max grayscale value. Only pixel regions that fall between these
      thresholds will be considered. For RGB565 images each tuple needs to have
      six values (l_lo, l_hi, a_lo, a_hi, b_lo, b_hi) - which are minimums and
      maximums for the LAB L, A, and B channels respectively. For easy usage this
      function will automatically fix swapped min and max values. Additionally,
      if a tuple is larger than six values the rest are ignored. Conversely, if the
      tuple is too short the rest of the thresholds are assumed to be at maximum
      range.

      Note
      ----

         To get the thresholds for the object you want to track just select (click
         and drag) on the object you want to track in the IDE frame buffer. The
         histogram will then update to just be in that area. Then just write down
         where the color distribution starts and falls off in each histogram channel.
         These will be your low and high values for ``thresholds``. It's best to
         manually determine the thresholds versus using the upper and lower
         quartile statistics because they are too tight.

         You may also determine color thresholds by going into
         ``Tools->Machine Vision->Threshold Editor`` in OpenMV IDE and selecting
         thresholds from the GUI slider window.

      ``invert`` inverts the thresholding operation such that instead of matching
      pixels inside of some known color bounds pixels are matched that are outside
      of the known color bounds.

      Unless you need to do something advanced with color statistics just use the
      `image.get_statistics()` method instead of this method for looking at pixel
      areas in an image.

      ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
      specified, it is equal to the image rectangle. Only pixels within the
      ``roi`` are operated on.

      ``bins`` and others are the number of bins to use for the histogram
      channels. For grayscale images use ``bins`` and for RGB565 images use
      the others for each channel. The bin counts must be greater than 2 for each
      channel. Additionally, it makes no sense to set the bin count larger than
      the number of unique pixel values for each channel. By default, the historgram
      will have the maximum number of bins per channel.

      ``difference`` may be set to an image object to cause this method to operate
      on the difference image between the current image and the ``difference`` image
      object. This saves having to use a separate buffer.

      Not supported on compressed images or bayer images."""

   # def get_statistics(self, [thresholds, [invert=False, [roi: tuple[int, int, int, int], [bins, [l_bins, [a_bins, [b_bins, [difference]]]]]]]]) -> Image:"""Computes the mean, median, mode, standard deviation, min, max, lower
   #    quartile, and upper quartile for all color channels for an ``roi`` and
   #    returns a `image.statistics` object. Please see the `image.statistics`
   #    object for more information. You can also invoke this method by using
   #    ``image.get_stats`` or ``image.statistics``. If you pass a list of
   #    ``thresholds`` then the histogram information will only be computed from
   #    pixels within the threshold list.

   #    ``thresholds`` must be a list of tuples
   #    ``[(lo, hi), (lo, hi), ..., (lo, hi)]`` defining the ranges of color you
   #    want to track. For
   #    grayscale images each tuple needs to contain two values - a min grayscale
   #    value and a max grayscale value. Only pixel regions that fall between these
   #    thresholds will be considered. For RGB565 images each tuple needs to have
   #    six values (l_lo, l_hi, a_lo, a_hi, b_lo, b_hi) - which are minimums and
   #    maximums for the LAB L, A, and B channels respectively. For easy usage this
   #    function will automatically fix swapped min and max values. Additionally,
   #    if a tuple is larger than six values the rest are ignored. Conversely, if the
   #    tuple is too short the rest of the thresholds are assumed to be at maximum
   #    range.

   #    Note
   #    ----

   #       To get the thresholds for the object you want to track just select (click
   #       and drag) on the object you want to track in the IDE frame buffer. The
   #       histogram will then update to just be in that area. Then just write down
   #       where the color distribution starts and falls off in each histogram channel.
   #       These will be your low and high values for ``thresholds``. It's best to
   #       manually determine the thresholds versus using the upper and lower
   #       quartile statistics because they are too tight.

   #       You may also determine color thresholds by going into
   #       ``Tools->Machine Vision->Threshold Editor`` in OpenMV IDE and selecting
   #       thresholds from the GUI slider window.

   #    ``invert`` inverts the thresholding operation such that instead of matching
   #    pixels inside of some known color bounds pixels are matched that are outside
   #    of the known color bounds.

   #    You'll want to use this method any time you need to get information about
   #    the values of an area of pixels in an image. For example, after if you're
   #    trying to detect motion using frame differencing you'll want to use this
   #    method to determine a change in the color channels of the image to trigger
   #    your motion detection threshold.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    ``bins`` and others are the number of bins to use for the histogram
   #    channels. For grayscale images use ``bins`` and for RGB565 images use
   #    the others for each channel. The bin counts must be greater than 2 for each
   #    channel. Additionally, it makes no sense to set the bin count larger than
   #    the number of unique pixel values for each channel. By default, the historgram
   #    will have the maximum number of bins per channel.

   #    ``difference`` may be set to an image object to cause this method to operate
   #    on the difference image between the current image and the ``difference`` image
   #    object. This saves having to use a separate buffer.

   #    Not supported on compressed images or bayer images."""

   # def get_regression(self, thresholds, [invert=False, [roi: tuple[int, int, int, int], [x_stride=2, [y_stride=1, [area_threshold=10, [pixels_threshold=10, [robust=False]]]]]]]) -> Image:"""Computes a linear regression on all the thresholded pixels in the image. The
   #    linear regression is computed using least-squares normally which is fast but
   #    cannot handle any outliers. If ``robust`` is True then the Theil–Sen linear
   #    regression is used instead which computes the median of all slopes between
   #    all thresholded pixels in the image. This is an N^2 operation which may drops
   #    your FPS down to below 5 even on an 80x60 image if too many pixels are set
   #    after thresholding. However, as long as the number of pixels set after
   #    thresholding remains low the linear regression will be valid even in the case
   #    of up to 30% of the thresholded pixels being outliers (e.g. it's robust).

   #    This method returns a `image.line` object. See this blog post on how to use the
   #    line object easily: https://openmv.io/blogs/news/linear-regression-line-following

   #    ``thresholds`` must be a list of tuples
   #    ``[(lo, hi), (lo, hi), ..., (lo, hi)]`` defining the ranges of color you
   #    want to track. For
   #    grayscale images each tuple needs to contain two values - a min grayscale
   #    value and a max grayscale value. Only pixel regions that fall between these
   #    thresholds will be considered. For RGB565 images each tuple needs to have
   #    six values (l_lo, l_hi, a_lo, a_hi, b_lo, b_hi) - which are minimums and
   #    maximums for the LAB L, A, and B channels respectively. For easy usage this
   #    function will automatically fix swapped min and max values. Additionally,
   #    if a tuple is larger than six values the rest are ignored. Conversely, if the
   #    tuple is too short the rest of the thresholds are assumed to be at maximum
   #    range.

   #    Note
   #    ----

   #       To get the thresholds for the object you want to track just select (click
   #       and drag) on the object you want to track in the IDE frame buffer. The
   #       histogram will then update to just be in that area. Then just write down
   #       where the color distribution starts and falls off in each histogram channel.
   #       These will be your low and high values for ``thresholds``. It's best to
   #       manually determine the thresholds versus using the upper and lower
   #       quartile statistics because they are too tight.

   #       You may also determine color thresholds by going into
   #       ``Tools->Machine Vision->Threshold Editor`` in OpenMV IDE and selecting
   #       thresholds from the GUI slider window.

   #    ``invert`` inverts the thresholding operation such that instead of matching
   #    pixels inside of some known color bounds pixels are matched that are outside
   #    of the known color bounds.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    ``x_stride`` is the number of x pixels to skip over when evaluating the image.

   #    ``y_stride`` is the number of y pixels to skip over when evaluating the image.

   #    If the regression's bounding box area is less than ``area_threshold`` then None is returned.

   #    If the regression's pixel count is less than ``pixels_threshold`` then None is returned.

   #    Not supported on compressed images or bayer images."""

   def find_blobs(self, thresholds: Union[list[tuple[int, int]], list[tuple[int, int, int, int, int, int]]], invert:bool=..., roi:tuple[int, int, int, int]=..., x_stride:int=..., y_stride:int=..., area_threshold:int=..., pixels_threshold:int=..., merge:int=..., margin:int=..., threshold_cb:Callable[[blob], bool]=..., merge_cb:Callable[[blob], bool]=..., x_hist_bins_max:int=..., y_hist_bins_max:int=...) -> blob:

      """Finds all blobs (connected pixel regions that pass a threshold test) in the
      image and returns a list of `image.blob` objects which describe each blob.
      Please see the `image.blob` object more more information.

      ``thresholds`` must be a list of tuples
      ``[(lo, hi), (lo, hi), ..., (lo, hi)]`` defining the ranges of color you
      want to track. You may pass up to 32 threshold tuples in one call. For
      grayscale images each tuple needs to contain two values - a min grayscale
      value and a max grayscale value. Only pixel regions that fall between these
      thresholds will be considered. For RGB565 images each tuple needs to have
      six values (l_lo, l_hi, a_lo, a_hi, b_lo, b_hi) - which are minimums and
      maximums for the LAB L, A, and B channels respectively. For easy usage this
      function will automatically fix swapped min and max values. Additionally,
      if a tuple is larger than six values the rest are ignored. Conversely, if the
      tuple is too short the rest of the thresholds are assumed to be at maximum
      range.

      Note
      ----

         To get the thresholds for the object you want to track just select (click
         and drag) on the object you want to track in the IDE frame buffer. The
         histogram will then update to just be in that area. Then just write down
         where the color distribution starts and falls off in each histogram channel.
         These will be your low and high values for ``thresholds``. It's best to
         manually determine the thresholds versus using the upper and lower
         quartile statistics because they are too tight.

         You may also determine color thresholds by going into
         ``Tools->Machine Vision->Threshold Editor`` in OpenMV IDE and selecting
         thresholds from the GUI slider window.

      ``invert`` inverts the thresholding operation such that instead of matching
      pixels inside of some known color bounds pixels are matched that are outside
      of the known color bounds.

      ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
      specified, it is equal to the image rectangle. Only pixels within the
      ``roi`` are operated on.

      ``x_stride`` is the number of x pixels to skip when searching for a blob.
      Once a blob is found the line fill algorithm will be pixel accurate.
      Increase ``x_stride`` to speed up finding blobs if blobs are known to be large.

      ``y_stride`` is the number of y pixels to skip when searching for a blob.
      Once a blob is found the line fill algorithm will be pixel accurate.
      Increase ``y_stride`` to speed up finding blobs if blobs are known to be large.

      If a blob's bounding box area is less than ``area_threshold`` it is filtered
      out.

      If a blob's pixel count is less than ``pixels_threshold`` it is filtered out.

      ``merge`` if True merges all not filtered out blobs whos bounding
      rectangles intersect each other. ``margin`` can be used to increase or
      decrease the size of the bounding rectangles for blobs during the
      intersection test. For example, with a margin of 1 blobs whos bounding
      rectangles are 1 pixel away from each other will be merged.

      Merging blobs allows you to implement color code tracking. Each blob object
      has a ``code`` value which is a bit vector made up of 1s for each color
      threshold. For example, if you pass `image.find_blobs` two color
      thresholds then the first threshold has a code of 1 and the second 2 (a
      third threshold would be 4 and a fourth would be 8 and so on). Merged blobs
      logically OR all their codes together so that you know what colors produced
      them. This allows you to then track two colors if you get a blob object
      back with two colors then you know it might be a color code.

      You might also want to merge blobs if you are using tight color bounds which
      do not fully track all the pixels of an object you are trying to follow.

      Finally, if you want to merge blobs, but, don't want two color thresholds to
      be merged then just call `image.find_blobs` twice with separate thresholds
      so that blobs aren't merged.

      ``threshold_cb`` may be set to the function to call on every blob after its
      been thresholded to filter it from the list of blobs to be merged. The call
      back function will receive one argument - the blob object to be filtered.
      The call back then must return True to keep the blob and False to filter it.

      ``merge_cb`` may be set to the function to call on every two blobs about to
      be merged to prevent or allow the merge. The call back function will receive
      two arguments - the two blob objects to be merged. The call back then must
      return True to merge the blobs or False to prevent merging the blobs.

      ``x_hist_bins_max`` if set to non-zero populates a histogram buffer in each
      blob object with an x_histogram projection of all columns in the object. This
      value then sets the number of bins for that projection.

      ``y_hist_bins_max`` if set to non-zero populates a histogram buffer in each
      blob object with an y_histogram projection of all rows in the object. This
      value then sets the number of bins for that projection.

      Not supported on compressed images or bayer images."""

   # def find_lines(self, [roi: tuple[int, int, int, int], [x_stride=2, [y_stride=1, [threshold=1000, [theta_margin=25, [rho_margin=25]]]]]]) -> Image:"""Finds all infinite lines in the image using the hough transform. Returns a list
   #    of `image.line` objects.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    ``x_stride`` is the number of x pixels to skip when doing the hough transform.
   #    Only increase this if lines you are searching for are large and bulky.

   #    ``y_stride`` is the number of y pixels to skip when doing the hough transform.
   #    Only increase this if lines you are searching for are large and bulky.

   #    ``threshold`` controls what lines are detected from the hough transform. Only
   #    lines with a magnitude greater than or equal to ``threshold`` are returned. The
   #    right value of ``threshold`` for your application is image dependent. Note that
   #    the magnitude of a line is the sum of all sobel filter magnitudes of pixels
   #    that make up that line.

   #    ``theta_margin`` controls the merging of detected lines. Lines which are
   #    ``theta_margin`` degrees apart and ``rho_margin`` rho apart are merged.

   #    ``rho_margin`` controls the merging of detected lines. Lines which are
   #    ``theta_margin`` degrees apart and ``rho_margin`` rho apart are merged.

   #    This method working by running the sobel filter over the image and taking
   #    the magnitude and gradient responses from the sobel filter to feed a hough
   #    transform. It does not require any preprocessing on the image first. However,
   #    my cleaning up the image using filtering you may get more stable results.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def find_line_segments(self, [roi: tuple[int, int, int, int], [merge_distance=0, [max_theta_difference=15]]]) -> Image:"""Finds line segments in the image using the hough transform. Returns a list
   #    of `image.line` objects .

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    ``merge_distance`` specifies the maximum number of pixels two line segements
   #    can be seperated by each other (at any point on one line) to be merged.

   #    ``max_theta_difference`` is the maximum theta difference in degrees two line
   #    segements that are ``merge_distance`` apart to be merged.

   #    This method uses the LSD library (also used by OpenCV) to find line segements
   #    in the image. It's somewhat slow but very accurate and lines don't jump around.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   def find_circles(self, roi: tuple[int, int, int, int] = ..., x_stride=2, y_stride=1, threshold=2000, x_margin=10, y_margin=10, r_margin=10, r_min=2, r_max = ..., r_step=2) -> circle:"""Finds circles in the image using the hough transform. Returns a list of
      `image.circle` objects.

      ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
      specified, it is equal to the image rectangle. Only pixels within the
      ``roi`` are operated on.

      ``x_stride`` is the number of x pixels to skip when doing the hough transform.
      Only increase this if circles you are searching for are large and bulky.

      ``y_stride`` is the number of y pixels to skip when doing the hough transform.
      Only increase this if circles you are searching for are large and bulky.

      ``threshold`` controls what circles are detected from the hough transform. Only
      circles with a magnitude greater than or equal to ``threshold`` are returned. The
      right value of ``threshold`` for your application is image dependent. Note that
      the magnitude of a circle is the sum of all sobel filter magnitudes of pixels
      that make up that circle.

      ``x_margin`` controls the merging of detected circles. Circles which are
      ``x_margin``, ``y_margin``, and ``r_margin`` pixels apart are merged.

      ``y_margin`` controls the merging of detected circles. Circles which are
      ``x_margin``, ``y_margin``, and ``r_margin`` pixels apart are merged.

      ``r_margin`` controls the merging of detected circles. Circles which are
      ``x_margin``, ``y_margin``, and ``r_margin`` pixels apart are merged.

      ``r_min`` controls the minimum circle radius detected. Increase this to speed
      up the algorithm. Defaults to 2.

      ``r_max`` controls the maximum circle radius detected. Decrease this to speed
      up the algorithm. Defaults to min(roi.w/2, roi.h/2).

      ``r_step`` controls how to step the radius detection by. Defaults to 2.

      Not supported on compressed images or bayer images.

      This method is not available on the OpenMV Cam M4."""

   # def find_rects(self, [roi: tuple[int, int, int, int]=Auto, [threshold=10000]]) -> Image:"""Find rectangles in the image using the same quad detection algorithm used to
   #    find apriltags. Works best of rectangles that have good contrast against the
   #    background. The apriltag quad detection algorithm can handle any
   #    scale/rotation/shear on rectangles. Returns a list of `image.rect` objects.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    Rectangles which have an edge magnitude (which is computed by sliding the
   #    sobel operator across all pixels on the edges of the rectangle and summing
   #    their values) less than ``threshold`` are filtered out of the returned list.
   #    The correct value of ``threshold`` is depended on your application/scene.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def find_qrcodes(self, [roi: tuple[int, int, int, int]]) -> Image:"""Finds all qrcodes within the ``roi`` and returns a list of `image.qrcode`
   #    objects. Please see the `image.qrcode` object for more information.

   #    QR Codes need to be relatively flat in the image for this method to work.
   #    You can achieve a flatter image that is not effected by lens distortion by
   #    either using the `sensor.set_windowing()` function to zoom in the on the
   #    center of the lens, `image.lens_corr()` to undo lens barrel distortion, or
   #    by just changing out the lens for something with a narrower fields of view.
   #    There are machine vision lenses available which do not cause barrel
   #    distortion but they are much more expensive to than the standard lenses
   #    supplied by OpenMV.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def find_apriltags(self, [roi: tuple[int, int, int, int], [families=image.TAG36H11, [fx, [fy, [cx, [cy]]]]]]) -> Image:"""Finds all apriltags within the ``roi`` and returns a list of `image.apriltag`
   #    objects. Please see the `image.apriltag` object for more information.

   #    Unlike QR Codes, AprilTags can be detected at much farther distances, worse
   #    lighting, in warped images, etc. AprilTags are robust too all kinds of
   #    image distortion issues that QR Codes are not to. That said, AprilTags
   #    can only encode a numeric ID as their payload.

   #    AprilTags can also be used for localization purposes. Each `image.apriltag`
   #    object returns its translation and rotation from the camera. The units
   #    of the translation are determined by ``fx``, ``fy``, ``cx``, and ``cy``
   #    which are the focal lengths and center points of the image in the X and
   #    Y directions respectively.

   #    Note
   #    ----

   #       To create AprilTags use the tag generator tool built-in to OpenMV IDE.
   #       The tag generator can create printable 8.5"x11" AprilTags.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    ``families`` is bitmask of tag families to decode. It is the logical OR of:

   #      * `image.TAG16H5`
   #      * `image.TAG25H7`
   #      * `image.TAG25H9`
   #      * `image.TAG36H10`
   #      * `image.TAG36H11`
   #      * `image.ARTOOLKIT`

   #    By default it is just `image.TAG36H11` which is the best tag family to
   #    use. Note that `image.find_apriltags()` slows down per enabled tag family.

   #    ``fx`` is the camera X focal length in pixels. For the standard OpenMV Cam
   #    this is (2.8 / 3.984) * 656. Which is the lens focal length in mm, divided
   #    by the camera sensor length in the X direction multiplied by the number of
   #    camera sensor pixels in the X direction (for the OV7725 camera).

   #    ``fx`` is the camera Y focal length in pixels. For the standard OpenMV Cam
   #    this is (2.8 / 2.952) * 488. Which is the lens focal length in mm, divided
   #    by the camera sensor length in the Y direction multiplied by the number of
   #    camera sensor pixels in the Y direction (for the OV7725 camera).

   #    ``cx`` is the image center which is just ``image.width()/2``. This is not
   #    ``roi.w()/2``.

   #    ``cy`` is the image center which is just ``image.height()/2``. This is not
   #    ``roi.h()/2``.

   #    Not supported on compressed images.

   #    This method is not available on the OpenMV Cam M4."""

   # def find_datamatrices(self, [roi: tuple[int, int, int, int], [effort=200]]) -> Image:"""Finds all datamatrices within the ``roi`` and returns a list of `image.datamatrix`
   #    objects. Please see the `image.datamatrix` object for more information.

   #    Data Matrices need to be relatively flat in the image for this method to work.
   #    You can achieve a flatter image that is not effected by lens distortion by
   #    either using the `sensor.set_windowing()` function to zoom in the on the
   #    center of the lens, `image.lens_corr()` to undo lens barrel distortion, or
   #    by just changing out the lens for something with a narrower fields of view.
   #    There are machine vision lenses available which do not cause barrel
   #    distortion but they are much more expensive to than the standard lenses
   #    supplied by OpenMV.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    ``effort`` controls how much time to spend trying to find data matrix matches.
   #    The default value of 200 should be good for all use-cases. However, you may
   #    increase the effort, at a cost of the frame rate, to increase detection. You
   #    may also lower the effort to increase the frame rate, but, at a cost of
   #    detections... note that when ``effort`` is set to below 160 or so you will
   #    not detect anything anymore. Also note that you can make ``effort`` as high
   #    as you like. But, any values above 240 or so do not result in much increase
   #    in the detection rate.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def find_barcodes(self, [roi: tuple[int, int, int, int]]) -> Image:"""Finds all 1D barcodes within the ``roi`` and returns a list of `image.barcode`
   #    objects. Please see the `image.barcode` object for more information.

   #    For best results use a 640 by 40/80/160 window. The lower the vertical res
   #    the faster everything will run. Since bar codes are linear 1D images you
   #    just need a lot of resolution in one direction and just a little resolution
   #    in the other direction. Note that this function scans both horizontally and
   #    vertically so you can use a 40/80/160 by 480 window if you want. Finally,
   #    make sure to adjust your lens so that the bar code is positioned where the
   #    focal length produces the sharpest image. Blurry bar codes can't be decoded.

   #    This function supports all these 1D barcodes (basically all barcodes):

   #      * `image.EAN2`
   #      * `image.EAN5`
   #      * `image.EAN8`
   #      * `image.UPCE`
   #      * `image.ISBN10`
   #      * `image.UPCA`
   #      * `image.EAN13`
   #      * `image.ISBN13`
   #      * `image.I25`
   #      * `image.DATABAR` (RSS-14)
   #      * `image.DATABAR_EXP` (RSS-Expanded)
   #      * `image.CODABAR`
   #      * `image.CODE39`
   #      * `image.PDF417`
   #      * `image.CODE93`
   #      * `image.CODE128`

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def find_displacement(self, template, [roi: tuple[int, int, int, int], [template_roi, [logpolar=False]]]) -> Image:"""Find the translation offset of the this image from the template. This
   #    method can be used to do optical flow. This method returns a `image.displacement`
   #    object with the results of the displacement calculation using phase correlation.

   #    ``roi`` is the region-of-interest rectangle (x, y, w, h) to work in.
   #    If not specified, it is equal to the image rectangle.

   #    ``template_roi`` is the region-of-interest rectangle (x, y, w, h) to work in.
   #    If not specified, it is equal to the image rectangle.

   #    ``roi`` and ``template`` roi must have the same w/h but may have any x/y
   #    location in the image. You may slide smaller rois arround a larger image to
   #    get an optical flow gradient image...

   #    `image.find_displacement()` normally computes the x/y translation between two
   #    images. However, if you pass ``logpolar=True`` it will instead find rotation
   #    and scale changes between the two images. The same `image.displacement` object
   #    result encodes both possible repsonses.

   #    Not supported on compressed images or bayer images.

   #    Note
   #    ----

   #       Please use this method on power-of-2 image sizes (e.g. `sensor.B64X64`).

   #    Not supported on compressed images or bayer images.

   #    This method is not available on the OpenMV Cam M4."""

   # def find_template(self, template, threshold, [roi: tuple[int, int, int, int], [step=2, [search=image.SEARCH_EX]]]) -> Image:"""Tries to find the first location in the image where template matches using
   #    Normalized Cross Correlation. Returns a bounding box tuple (x, y, w, h) for
   #    the matching location otherwise None.

   #    ``template`` is a small image object that is matched against this image
   #    object. Note that both images must be grayscale.

   #    ``threshold`` is floating point number (0.0-1.0) where a higher threshold
   #    prevents false positives while lowering the detection rate while a lower
   #    threshold does the opposite.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    ``step`` is the number of pixels to skip past while looking for the
   #    template. Skipping pixels considerably speeds the algorithm up. This only
   #    affects the algorithm in SERACH_EX mode.

   #    ``search`` can be either ``image.SEARCH_DS`` or ``image.SEARCH_EX``.
   #    ``image.SEARCH_DS`` searches for the template using as faster algorithm
   #    than ``image.SEARCH_EX`` but may not find the template if it's near the
   #    edges of the image. ``image.SEARCH_EX`` does an exhaustive search for the
   #    image but can be much slower than ``image.SEARCH_DS``.

   #    Only works on grayscale images."""

   # def find_features(self, cascade, [threshold=0.5, [scale=1.5, [roi: tuple[int, int, int, int]]]]) -> Image:"""This method searches the image for all areas that match the passed in Haar
   #    Cascade and returns a list of bounding box rectangles tuples (x, y, w, h)
   #    around those features. Returns an empty list if no features are found.

   #    ``cascade`` is a Haar Cascade object. See `image.HaarCascade()` for more
   #    details.

   #    ``threshold`` is a threshold (0.0-1.0) where a smaller value increase the
   #    detection rate while raising the false positive rate. Conversely, a higher
   #    value decreases the detection rate while lowering the false positive rate.

   #    ``scale`` is a float that must be greater than 1.0. A higher scale
   #    factor will run faster but will have much poorer image matches. A good
   #    value is between 1.35 and 1.5.

   #    ``roi: tuple[int, int, int, int]`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi: tuple[int, int, int, int]`` are operated on."""

   # def find_eye(self, roi: tuple[int, int, int, int]) -> Image:"""Searches for the pupil in a region-of-interest (x, y, w, h) tuple around an
   #    eye. Returns a tuple with the (x, y) location of the pupil in the image.
   #    Returns (0,0) if no pupils are found.

   #    To use this function first use `image.find_features()` with the
   #    ``frontalface`` HaarCascade to find someone's face. Then use
   #    `image.find_features()` with the ``eye`` HaarCascade to find the eyes on the
   #    face. Finally, call this method on the eye ROI returned by
   #    `image.find_features()` to get the pupil coordinates.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    Only works on grayscale images."""

   # def find_lbp(self, roi: tuple[int, int, int, int]) -> Image:"""Extracts LBP (local-binary-patterns) keypoints from the region-of-interest
   #    (x, y, w, h) tuple. You can then use then use the `image.match_descriptor()`
   #    function to compare two sets of keypoints to get the matching distance.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    Only works on grayscale images."""

   # def find_keypoints(self, [roi: tuple[int, int, int, int], [threshold=20, [normalized=False, [scale_factor=1.5, [max_keypoints=100, [corner_detector=image.CORNER_AGAST]]]]]]) -> Image:"""Extracts ORB keypoints from the region-of-interest (x, y, w, h) tuple. You
   #    can then use then use the `image.match_descriptor()` function to compare
   #    two sets of keypoints to get the matching areas. Returns None if no
   #    keypoints were found.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    ``threshold`` is a number (between 0 - 255) which controls the number of
   #    extracted corners. For the default AGAST corner detector this should be
   #    around 20. FOr the FAST corner detector this should be around 60-80. The
   #    lower the threshold the more extracted corners you get.

   #    ``normalized`` is a boolean value that if True turns off extracting
   #    keypoints at multiple resolutions. Set this to true if you don't care
   #    about dealing with scaling issues and want the algorithm to run faster.

   #    ``scale_factor`` is a float that must be greater than 1.0. A higher scale
   #    factor will run faster but will have much poorer image matches. A good
   #    value is between 1.35 and 1.5.

   #    ``max_keypoints`` is the maximum number of keypoints a keypoint object may
   #    hold. If keypoint objects are too big and causing out of RAM issues then
   #    decrease this value.

   #    ``corner_detector`` is the corner detector algorithm to use which extracts
   #    keypoints from the image. It can be either `image.CORNER_FAST` or
   #    `image.CORNER_AGAST`. The FAST corner detector is faster but much less accurate.

   #    Only works on grayscale images."""

   # def find_edges(self, edge_type, [threshold]) -> Image:"""Turns the image to black and white leaving only the edges as white pixels.

   #       * image.EDGE_SIMPLE - Simple thresholded high pass filter algorithm.
   #       * image.EDGE_CANNY - Canny edge detection algorithm.

   #    ``threshold`` is a two valued tuple containing a low threshold and high
   #    threshold. You can control the quality of edges by adjusting these values.
   #    It defaults to (100, 200).

   #    Only works on grayscale images."""

   # def [roi,self,  [size=8]]) -> Image:"""Replaces the pixels in the ROI with HOG (histogram of orientated graidients)
   #    lines.

   #    ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
   #    specified, it is equal to the image rectangle. Only pixels within the
   #    ``roi`` are operated on.

   #    Only works on grayscale images.

   #    This method is not available on the OpenMV Cam M4.

# Constants
# ---------

# .. data:: image.BINARY

#    BINARY (bitmap) pixel format. Each pixel is 1-bit.

# .. data:: image.GRAYSCALE

#    GRAYSCALE pixel format. Each pixel is 8-bits, 1-byte.

# .. data:: image.RGB565

#    RGB565 pixel format. Each pixel is 16-bits, 2-bytes. 5-bits are used for red,
#    6-bits are used for green, and 5-bits are used for blue.

# .. data:: image.BAYER

#    RAW BAYER image pixel format. If you try to make the frame size too big
#    to fit in the frame buffer your OpenMV Cam will set the pixel format
#    to BAYER so that you can capture images but no image processing methods
#    will be operational.

# .. data:: image.JPEG

#    A JPEG image.

# .. data:: image.AREA

#    Use area scaling when downscaling an image (Nearest Neighbor is used for upscaling).

#    You should use area scaling when downscaling for the highest visual quality.

# .. data:: image.BILINEAR

#    Use bilinear scaling when upscaling an image. This produces a good quality scaled image output
#    and is fast.

#    When downscaling an image this method will subsample the input image to produce the downscaled
#    image. Use `image.AREA` for the higest quality downscaling if speed is not an issue.

# .. data:: image.BICUBIC

#    Use bicubic scaling when upscaling an image. This produces a high quality scaled image output,
#    but is slow.

#    When downscaling an image this method will subsample the input image to produce the downscaled
#    image. Use `image.AREA` for the higest quality downscaling if speed is not an issue.

# .. data:: image.CENTER

#    Anchor the image being drawn with `draw_image` in the center versus the top left hand corner.

# .. data:: image.EXTRACT_RGB_CHANNEL_FIRST

#    When extracting an RGB channel from an RGB image using `draw_image` extract the channel first
#    before scaling versus afterwards to prevent any artifacts.

# .. data:: image.APPLY_COLOR_PALETTE_FIRST

#    When applying a color lookup table to an image using `draw_image` apply the color look table
#    first before scaling versus afterwards to prevent any artifacts.

# .. data:: image.BLACK_BACKGROUND

#    Speeds up `draw_image` when drawing on a black destination image when using alpha effects that
#    require reading both source and destination pixels. This skips reading the destination pixel.

# .. data:: image.SEARCH_EX

#    Exhaustive template matching search.

# .. data:: image.SEARCH_DS

#    Faster template matching search.

# .. data:: image.EDGE_CANNY

#    Use the canny edge detection algorithm for doing edge detection on an image.

# .. data:: image.EDGE_SIMPLE

#    Use a simple thresholded high pass filter algorithm for doing edge detection
#    on an image.

CORNER_FAST: int
"Faster and less accurate corner detection algorithm for ORB keypoints."

CORNER_AGAST: int
"Slower and more accurate corner detection algorithm for ORB keypoints."

TAG16H5: int
"TAG1H5 tag family bit mask enum. Used for AprilTags."

TAG25H7: int
"TAG25H7 tag family bit mask enum. Used for AprilTags."

TAG25H9: int
"TAG25H9 tag family bit mask enum. Used for AprilTags."

TAG36H10: int
"TAG36H10 tag family bit mask enum. Used for AprilTags."

TAG36H11: int
"TAG36H11 tag family bit mask enum. Used for AprilTags."

ARTOOLKIT: int
"ARTOOLKIT tag family bit mask enum. Used for AprilTags."

EAN2: int
"EAN2 barcode type enum."

EAN5: int
"EAN5 barcode type enum."

EAN8: int
"EAN8 barcode type enum."

UPCE: int
"UPCE barcode type enum."

ISBN10: int
"ISBN10 barcode type enum."

UPCA: int
"UPCA barcode type enum."

EAN13: int
"EAN13 barcode type enum."

ISBN13: int
"ISBN13 barcode type enum."

I25: int
"I25 barcode type enum."

DATABAR: int
"DATABAR barcode type enum."

DATABAR_EXP: int
"DATABAR_EXP barcode type enum."

CODABAR: int
"CODABAR barcode type enum."

CODE39: int
"CODE39 barcode type enum."

PDF417: int
"PDF417 barcode type enum - Future (e.g. doesn't work right now)."

CODE93: int
"CODE93 barcode type enum."

CODE128: int
"CODE128 barcode type enum."
