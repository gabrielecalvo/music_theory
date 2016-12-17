# music_theory
A collection of easy-to-use classes implemented according to music theory

There are four classes currently implemented, each with basic methods to answer simple questions based on music theory. The classes are:
- Note
- Chord
- Scale
- Song

They can all be imported as in the example below along with scale, interval and chord types:
```sh
from music_theory.music_classes import Note, Chord, Scale
from music_theory.song import Song
from music_theory.music_types import ScaleType, IntervalType, ChordType
```
The types implemented so far are:
- ***ScaleType***: major, natural_minor, harmonic_minor, melodic_minor_ascending, melodic_minor_descending, diminished.
- ***IntervalType***: root, minor_second, major_second, minor_third, major_third, perfect_forth, triton, perfect_fifth, minor_sixth, major_sixth, minor_seventh, major_seventh, octave.
- ***ChordType***: major_triad, minor_triad, augmented_triad, diminished_triad, major7, dominant7, half_diminished_7.

### Note
The initialization of this class requires a _note_id_ which can be any of the following: C, C#, Db, D, D#, Eb, E, F, F#, Gb, G, G#, Ab,A, A#, Bb, B.
The music scale that have root in the note can be generated using the method _get_scale_.
A note located at an arbitrary interval from the current note can be generated using the method _get_note_from_interval_.

```sh
n = Note('C#')

s = n.get_scale(ScaleType.harmonic_minor)
print(s)   # -->  Scale C# harmonic_minor

n2 = n.get_note_from_interval(IntervalType.major_sixth)
print(n2)   # -->  A#
n3 = n.get_note_from_interval(5)  # number of semi-tones away
print(n3)   # -->  F#
```

### Chord
The initialization of this class requires the root note and optionally the chord type and inversion, otherwise they will be defaulted to major_triad and no inversion. In alternative the Chord can be initialized using the method *from_chord_name* and passing the short name for the chord (e.g. A#m).
Once a chord has been generated, its constituting notes and short name can be returned as in the example below.
```sh
c = Chord(root_note='E', chord_type=ChordType.dominant7, inversion=2)
print(c)                # -->  E dominant7: [B, D, E, G#]
print(c.short_name())   # -->  E7
print(c.notes)          # -->  [B, D, E, G#]

c2 = Chord.from_chord_name('A#m')
print(c2)  # -->  A# minor_triad: [A#, C#, F]
```

### Scale
Similarly to the previous classes:
```sh
s = Scale(root_note='D', scale_type=ScaleType.natural_minor)
print(s)            # -->  Scale D natural_minor
print(s.notes)      # -->  [D, E, F, G, A, A#, C]

cs = s.get_chords()
print(cs[3])        # -->  G minor_triad: [G, A#, D]
```

### Song
This class is currently under development. Here are the example usages:
```sh
sng = Song(title='Save Tonight', artist='Eagle-Eye Cherry', key='Em')
print(sng)   # -->  "Save Tonight" by Eagle-Eye Cherry, in Em key

chords_stream = ['Am', 'F', 'C', 'G']
sng2 = Song.analyse_chord_stream(chords_stream, simplify=False)
sng2.title, sng2.artist = 'Save Tonight', 'Eagle-Eye Cherry'
print(sng2)  # -->  "Save Tonight" by Eagle-Eye Cherry, in Am key
```



### Todos

 - Write Tests
 - Add Code Comments
 - Further develop the Song class

License
----
MIT
