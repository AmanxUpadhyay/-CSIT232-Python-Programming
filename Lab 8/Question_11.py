# Below are the notes used in music:
# C C# D D# E F F# G G# A A# B
# The notes for the C major chord are C, E, G. A mathematical way to get this is that E is 4 steps past C and G is 7 steps past C. 
# This works for any base. For example, the notes for D major
# are D, F#, A. 
# We can represent the major chord steps as a list with two elements: [4,7]. 
# The corresponding lists for some other chord types are shown below:
# Minor [3,7] Dominant seventh [4,7,10]
# Augmented fifth [4,8] Minor seventh [3,7,10]
# Minor fifth [4,6] Major seventh [4,7,11]
# Major sixth [4,7,9] Diminished seventh [3,6,10]
# Minor sixth [3,7,9]
# Write a program that asks the user for the key and the chord type and prints out the notes of the chord. Use a dictionary whose keys are the (musical) keys and whose values are the lists of steps.

def main():
    key_dict = {'C':[0,4,7], 'C#':[1,5,8], 'D':[2,6,9], 'D#':[3,7,10], 'E':[4,8,11], 'F':[5,9,0], 'F#':[6,-10], 'G':[7,11,2], 'G#':[8], 'A':[9], 'A#':[10], 'B':[11]}
    chord_dict = {"Major":[4 ,7], "Minor":[3,7], "Dominant seventh":[4 ,7], "Augmented fifth":[5,8], "Minor seventh":[3,7], "Minor fifth":[4,6], "Major seventh":[4 ,7], "Major sixth":[4,7,9], "Diminished seventh":[3,6,10], "Minor sixth":[3,7,9]}
    key = input("Enter key: ")
    chord = input("Enter chord: ")
    print(key_dict[key])
    print(chord_dict[chord])
    print(key_dict[key][0] + chord_dict[chord][0], key_dict[key][1] + chord_dict[chord][1], key_dict[key][2] + chord_dict[chord][2])

main()