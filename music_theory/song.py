from collections import Counter
from music_theory.music_classes import Chord, Scale, Note
from music_theory.music_types import ChordType, ScaleType


class Song(object):
    def __init__(self, title='unknown', artist='unknown', key=None, chords=None):
        self.title = title
        self.artist = artist
        self.key = Chord.from_chord_name(key) if isinstance(key, str) else key
        self.key_confidence = 0
        self.chords = chords if chords else []

    def __repr__(self):
        key_info = ', in {} key'.format(self.key.short_name()) if self.key else ''
        return '"{}" by {}{}'.format(self.title, self.artist, key_info)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @classmethod
    def analyse_chord_stream(cls, chord_stream, simplify=True):
        sng = cls()
        stream = [sng.simplify_chord(i) for i in chord_stream] if simplify else chord_stream
        sng.key, sng.key_confidence = sng.detect_key_from_chord_stream(chord_stream=stream)
        sng.detect_chord_succession_from_stream(chord_stream=stream)
        return sng

    @staticmethod
    def detect_key_from_chord_stream(chord_stream):
        count_dict = Counter(chord_stream)
        unique_chords = count_dict.keys()
        unique_counts = count_dict.values()

        best_key_scale = (None, 0)
        for c in unique_chords:
            i_chord = Chord.from_chord_name(chord_name=c)
            i_scale_type = ScaleType.natural_minor if i_chord.type == ChordType.minor_triad else ScaleType.major
            i_scale = Scale(root_note=i_chord.root_note, scale_type=i_scale_type)
            score = i_scale.score_against_chords(chords=unique_chords, counts=unique_counts)
            if c == chord_stream[0]:
                score += 1

            if score > best_key_scale[1]:
                best_key_scale = (i_scale, score)

        best_key = best_key_scale[0].get_chords()[0]
        return best_key, score

    @staticmethod
    def detect_chord_succession_from_stream(chord_stream):
        # TODO
        pass

    @staticmethod
    def simplify_chord(chord):
        chord = chord.replace('maj', '')
        chord = chord.replace('m#', '#m')
        chord = chord[:3]
        if len(chord) > 1:
            if chord[1] not in ['#', 'b', 'm']:
                chord = chord[0]
            elif len(chord) > 2:
                if chord[2] != 'm':
                    chord = chord[:2]
        return chord
