from enum import Enum


class ScaleType(Enum):
    major = 0
    natural_minor = 1
    harmonic_minor = 2
    melodic_minor_ascending = 3
    melodic_minor_descending = 4
    diminished = 5


class IntervalType(Enum):
    root = 0
    minor_second = 1
    major_second = 2
    minor_third = 3
    major_third = 4
    perfect_forth = 5
    triton = 6
    perfect_fifth = 7
    minor_sixth = 8
    major_sixth = 9
    minor_seventh = 10
    major_seventh = 11
    octave = 12


class ChordType(Enum):
    major_triad = 0
    minor_triad = 1
    augmented_triad = 2
    diminished_triad = 3
    major7 = 4
    dominant7 = 5
    half_diminished_7 = 6
