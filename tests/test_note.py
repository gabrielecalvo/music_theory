from music_theory.music_classes import *


def test_note_init():
    n = Note('C#')
    assert n.all_notes == NOTES_SHARPS
    assert n.name == 'C#'
    assert n.idx == 1


def test_note_get_scale():
    n = Note('C#')
    actual = n.get_scale(ScaleType.harmonic_minor)
    expected = Scale('C#', ScaleType.harmonic_minor)
    assert actual == expected
