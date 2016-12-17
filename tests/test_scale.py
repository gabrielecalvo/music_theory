from music_theory.music_classes import *


def test_scale():
    s = Scale(root_note='C#', scale_type=ScaleType.natural_minor)
    assert s.type == ScaleType.natural_minor
    assert s.notes == [Note(i) for i in ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']]

    s = Scale(root_note='C', scale_type=ScaleType.major)
    assert s.notes == [Note(i) for i in ['C', 'D', 'E', 'F', 'G', 'A', 'B']]
    assert s.get_chords() == [Chord.from_chord_name(i) for i in ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim']]
    assert Scale(root_note='F#', scale_type=ScaleType.major).notes == \
           [Note(i) for i in ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F']]
    assert Scale(root_note='Gb', scale_type=ScaleType.major).notes == \
           [Note(i) for i in ['Gb', 'Ab', 'Bb', 'B', 'Db', 'Eb', 'F']]
    assert Scale(root_note='A', scale_type=ScaleType.natural_minor).notes == \
           [Note(i) for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G']]
    assert Scale(root_note='D#', scale_type=ScaleType.natural_minor).notes == \
           [Note(i) for i in ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'C#']]
    assert Scale(root_note='Eb', scale_type=ScaleType.natural_minor).notes == \
           [Note(i) for i in ['Eb', 'F', 'Gb', 'Ab', 'Bb', 'B', 'Db']]
