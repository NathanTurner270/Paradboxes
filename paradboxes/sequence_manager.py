"""
Module DocString
"""

class CubeSequence:
    """
    DocString
    """

    def __init__(self, sequence_format, cubes):
        pass

    def __repr__(self):
        # Ugly string representation
        pass

    def __str__(self):
        # Nice string representation
        pass


class SequenceFormat:
    """
    DocString
    """

    def __init__(self, type=SquenceType.DEFAULT, cube_order=None, led_sequence=None, timeout=None, string_sequence=None):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass


class SequenceType():
    """
    DocString
    """

    # Bounce randomly
    BOUNCE = 1
    DEFAULT = 2
    ROTATE_NON_NUMERICALLY = 3
    CUSTOM = 4
