"""Implementation of DIN ISO 1328 - Cylindrical gears – ISO system of flank tolerance classification.

See https://github.com/hanslhansl/din3962."""

from enum import IntEnum

class FlankToleranceClass(IntEnum):
    ISO1 = 1
    ISO2 = 2
    ISO3 = 3
    ISO4 = 4
    ISO5 = 5
    ISO6 = 6
    ISO7 = 7
    ISO8 = 8
    ISO9 = 9
    ISO10 = 10
    ISO11 = 11
    
from .diniso1328_1 import *
from .diniso1328_2 import *