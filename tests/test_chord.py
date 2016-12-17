from music_theory.music_classes import *


def test_chord():
    c = Chord(root_note='C#', chord_type=ChordType.minor_triad, inversion=1)
    assert c.type == ChordType.minor_triad
    assert c.inversion == 1
    assert c.notes == [Note(i) for i in ['E', 'G#', 'C#']]
