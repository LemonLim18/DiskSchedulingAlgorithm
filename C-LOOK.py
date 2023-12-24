import random

def CLOOK(arr, head):
 
    seek_count = 0
    max_seek = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []
 
    for i in range(len(arr)):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])
 
    # Sorting left and right vectors
    left.sort()
    right.sort()
 
    # First service the requests
    # on the right side of the
    # head
    for i in range(len(right)):
        cur_track = right[i]
 
        # Appending current track
        # to seek sequence
        seek_sequence.append(cur_track)
 
        # Calculate absolute distance
        distance = abs(cur_track - head)
 
        # Increase the total count
        seek_count += distance

        # Check if this distance is the max seek
        max_seek = max(max_seek, distance)
 
        # Accessed track is now new head
        head = cur_track
 
    # Once reached the right end
    # jump to the nearest track that
    # is needed to be serviced in
    # left direction
    if len(left) != 0:
        seek_count += abs(head - left[0])
        head = left[0]
 
    # Now service the requests again
    # which are left
    for i in range(len(left)):
        cur_track = left[i]
 
        # Appending current track
        # to seek sequence
        seek_sequence.append(cur_track)
 
        # Calculate absolute distance
        distance = abs(cur_track - head)
 
        # Increase the total count
        seek_count += distance

        # Check if this distance is the max seek
        max_seek = max(max_seek, distance)
 
        # Accessed track is now the new head
        head = cur_track
 
    print("Total number of seek operations =", 
          seek_count)
 
    print("Average seek time =", seek_count / len(arr))

    print("Worst-case seek time =", max_seek)
 
    print("Seek Sequence is: ", end="")
    print(*seek_sequence, sep=", ")
 

# request array
head = 50
# size = int(input("Enter the number of I/O requests: "))
size = 8
# arr = random.sample(range(disk_size), size)

# For testing purposes, use the following array:
arr = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
print("Array generated: ", end="")
print(*arr, sep=", ")
CLOOK(arr, head)
