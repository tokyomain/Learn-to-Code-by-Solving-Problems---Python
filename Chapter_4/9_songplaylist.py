# CCC '08 J2 - Do the Shuffle / Song Playlist
# https://dmoj.ca/problem/ccc08j2

# Input :
# b > int > (1 <= b => 4)  number of button
# n > int > (1 <= n => 10) times to press that button

# b1 > x Z Z Z Z > Z Z Z Z x
# b2 > Z Z Z Z x > x Z Z Z Z
# b3 > x y Z Z Z > y x Z Z Z 

# Output : Order of songs in the playlist after all button presses.
# Must be on one line, with a space separating each pair of songs.
# ex : B C D A E

songs = "ABCDE"
button = 0

while button != 4:
    # Read button
    button = int(input())
    # Read number of presses
    presses = int(input())

    # Process button presses 
    for i in range(presses):
        if button == 1:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:-1]
        elif button == 3:
            songs = songs[1] + songs[0] + songs[2:]

output = ''

for song in songs:
    output += song + ' '

print(output[:-1])