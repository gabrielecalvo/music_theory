from music_theory.music_types import IntervalType, ChordType, ScaleType

NOTES_SHARPS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
NOTES_FLATS = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
VALID_NOTES = NOTES_SHARPS + NOTES_FLATS

CHORD_INTERVALS = {
    ChordType.major_triad: [IntervalType.root, IntervalType.major_third, IntervalType.perfect_fifth],
    ChordType.minor_triad: [IntervalType.root, IntervalType.minor_third, IntervalType.perfect_fifth],
    ChordType.augmented_triad: [IntervalType.root, IntervalType.major_third, IntervalType.minor_sixth],
    ChordType.diminished_triad: [IntervalType.root, IntervalType.minor_third, IntervalType.triton],
    ChordType.major7: [IntervalType.root, IntervalType.major_third, IntervalType.perfect_fifth, IntervalType.major_seventh],
    ChordType.dominant7: [IntervalType.root, IntervalType.major_third, IntervalType.perfect_fifth, IntervalType.minor_seventh],
    ChordType.half_diminished_7: [IntervalType.root, IntervalType.minor_third, IntervalType.triton, IntervalType.minor_seventh],
}
CHORD_SUFFIXES = [
    ('m', ChordType.minor_triad),
    ('aug', ChordType.augmented_triad),
    ('dim', ChordType.diminished_triad),
    ('maj7', ChordType.major7),
    ('7', ChordType.dominant7),
    ('m7b5', ChordType.half_diminished_7),
]

TONES_SEQUENCES = {
    ScaleType.major: [2, 2, 1, 2, 2, 2],
    ScaleType.natural_minor: [2, 1, 2, 2, 1, 2],
    ScaleType.harmonic_minor: [2, 1, 2, 2, 1, 3],
    ScaleType.melodic_minor_ascending: [2, 1, 2, 2, 2, 2],
    ScaleType.melodic_minor_descending: [2, 1, 2, 2, 1, 2],
    ScaleType.diminished: [2, 1, 2, 1, 2, 1, 2],
}


class Note(object):
    def __init__(self, note_id):
        assert note_id in VALID_NOTES
        self.all_notes = NOTES_SHARPS if note_id in NOTES_SHARPS else NOTES_FLATS
        self.name = note_id
        self.idx = self.all_notes.index(note_id)

    def __repr__(self):
        return str(self.name)

    def get_scale(self, scale_type):
        return Scale(root_note=self, scale_type=scale_type)

    def get_note_from_interval(self, interval):
        interval = IntervalType(interval)
        duplicated_all_notes = self.all_notes * 2
        semitones = interval.value
        new_note_id = duplicated_all_notes[self.idx + semitones]
        return Note(note_id=new_note_id)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Chord(object):
    def __init__(self, root_note, chord_type=ChordType.major_triad, inversion=0):
        """
        :param root_note: either note_id (e.g. A#) or instance of Note
        :param chord_type: either integer or ChordType
        :param inversion: either integer or InversionType
        """

        if not isinstance(root_note, Note):
            root_note = Note(root_note)
        self.root_note = root_note
        self.type = ChordType(chord_type)
        self.intervals = [i for i in CHORD_INTERVALS[self.type]]
        self.inversion = inversion
        root_position_chord = [root_note.get_note_from_interval(i) for i in self.intervals]
        self.notes = self.shift(l=root_position_chord, shift=self.inversion)

    def __repr__(self):
        return str("{} {}: {}".format(self.root_note, self.type.name, self.notes))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @staticmethod
    def shift(l, shift):
        return l[shift:] + l[:shift]

    @classmethod
    def from_chord_name(cls, chord_name):
        assert isinstance(chord_name, str)
        searching = sorted(CHORD_SUFFIXES, key=lambda k: len(k[0]), reverse=True)
        for suffix, chord_type in searching:
            if chord_name.endswith(suffix):
                return cls(root_note=chord_name[:-len(suffix)], chord_type=chord_type)
        return cls(root_note=chord_name)

    def short_name(self):
        mapping = {v: k for k, v in CHORD_SUFFIXES}
        type_str = mapping.get(self.type, '')
        return '{}{}'.format(self.root_note, type_str)


class Scale(object):
    def __init__(self, root_note, scale_type=ScaleType.major):
        """
        :param root_note: either note_id (e.g. A#) or instance of Note
        :param scale_type: either integer or ScaleType
        """
        if not isinstance(root_note, Note):
            root_note = Note(root_note)
        self.root_note = root_note
        self.type = ScaleType(scale_type)
        scale_relative_indexes = self.parse_seq_to_indexes(TONES_SEQUENCES[self.type])
        duplicated_all_notes = root_note.all_notes * 2
        self.notes_idx = [root_note.idx + i for i in scale_relative_indexes]
        self.notes = [Note(duplicated_all_notes[i]) for i in self.notes_idx]

    def __repr__(self):
        return 'Scale {} {}'.format(self.root_note, self.type.name)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @staticmethod
    def parse_seq_to_indexes(seq):
        r = [0]
        for n in seq:
            r.append(r[-1] + n)
        return r

    def get_chords(self):
        if self.type == ScaleType.major:
            chord_types = [ChordType.major_triad, ChordType.minor_triad, ChordType.minor_triad, ChordType.major_triad,
                           ChordType.major_triad, ChordType.minor_triad, ChordType.diminished_triad]
            chords = [Chord(root_note=self.notes[i], chord_type=ct) for i, ct in enumerate(chord_types)]
        elif self.type == ScaleType.natural_minor:
            chord_types = [ChordType.minor_triad, ChordType.diminished_triad, ChordType.major_triad,
                           ChordType.minor_triad, ChordType.minor_triad, ChordType.major_triad, ChordType.major_triad]
            chords = [Chord(root_note=self.notes[i], chord_type=ct) for i, ct in enumerate(chord_types)]
        else:
            raise ValueError("Sorry, currently only major and natural_minor are implemented in this method.")
        return chords

    def score_against_chords(self, chords, counts=None):
        ensured_chords = [(Chord.from_chord_name(c) if isinstance(c, str) else c) for c in chords]

        if counts is None:
            counts = [1]*len(ensured_chords)

        scale_chords = self.get_chords()
        score = 0
        for cnt, chord in zip(counts, ensured_chords):
            if chord in scale_chords:
                score += cnt
        return score/sum(counts)
