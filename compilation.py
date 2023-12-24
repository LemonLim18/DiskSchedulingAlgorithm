import random

# START OF SCAN
def SCAN(requestArray, headPosition, cylinderNum):
 
    seek_count = 0
    max_seek = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []
 
    right.append(cylinderNum - 1)
 
    for i in range(size):
        if (requestArray[i] < headPosition):
            left.append(requestArray[i])
        if (requestArray[i] > headPosition):
            right.append(requestArray[i])
 

    left.sort()
    right.sort()
 

    for i in range(len(right)):
        cur_track = right[i]
             
        seek_sequence.append(cur_track)
 
        distance = abs(cur_track - headPosition)
 
        seek_count += distance

        max_seek = max(max_seek, distance)
 
        headPosition = cur_track
         
    # Scanning left
    for i in range(len(left) - 1, -1, -1):
        cur_track = left[i]
 
        seek_sequence.append(cur_track)
 
        # Calculate absolute distance
        distance = abs(cur_track - headPosition)
 
        seek_count += distance

        max_seek = max(max_seek, distance)
 
        headPosition = cur_track
    
    print('SCAN:')
    print("\tTotal number of seek operations =", 
          seek_count)
 
    print("\tAverage seek time =", seek_count / size)

    print("\tWorst-case seek time =", max_seek)
 
    print("\tSeek sequence: ", end="")
    print("\t" + ", ".join(map(str, seek_sequence)))
# END OF SCAN
 

# START OF CSCAN
def CSCAN(requestArray, headPosition, cylinderNum):
 
    seek_count = 0
    max_seek = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []
 
    left.append(0)
    right.append(cylinderNum - 1)
 
    for i in range(size):
        if (requestArray[i] < headPosition):
            left.append(requestArray[i])
        if (requestArray[i] > headPosition):
            right.append(requestArray[i])
 
    left.sort()
    right.sort()
 
    for i in range(len(right)):
        cur_track = right[i]
 
        seek_sequence.append(cur_track)
 
        distance = abs(cur_track - headPosition)
 
        seek_count += distance

        max_seek = max(max_seek, distance)
 
        headPosition = cur_track
 

    headPosition = 0
 
    seek_count += (cylinderNum - 1)
 

    for i in range(len(left)):
        cur_track = left[i]
 

        seek_sequence.append(cur_track)
 
        distance = abs(cur_track - headPosition)
 
        seek_count += distance

        max_seek = max(max_seek, distance)
 

        headPosition = cur_track
    
    print('\n\nC-SCAN:')
    print("\tTotal number of seek operations =", 
          seek_count)
 
    print("\tAverage seek time =", seek_count / size)

    print("\tWorst-case seek time =", max_seek)
 
    print("\tSeek sequence: ", end="")
    print("\t" + ", ".join(map(str, seek_sequence)))
# END OF CSCAN

# START OF CLOOK
def CLOOK(requestArray, headPosition):
 
    seek_count = 0
    max_seek = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []
 
    for i in range(len(requestArray)):
        if (requestArray[i] < headPosition):
            left.append(requestArray[i])
        if (requestArray[i] > headPosition):
            right.append(requestArray[i])
 

    left.sort()
    right.sort()
 

    for i in range(len(right)):
        cur_track = right[i]
 
        seek_sequence.append(cur_track)
 
        distance = abs(cur_track - headPosition)
 
        seek_count += distance

        max_seek = max(max_seek, distance)
 
        headPosition = cur_track
 
    if len(left) != 0:
        seek_count += abs(headPosition - left[0])
        headPosition = left[0]

    for i in range(len(left)):
        cur_track = left[i]
 
        # Appending current track
        # to seek sequence
        seek_sequence.append(cur_track)
 
        # Calculate absolute distance
        distance = abs(cur_track - headPosition)
 
        # Increase the total count
        seek_count += distance

        # Check if this distance is the max seek
        max_seek = max(max_seek, distance)
 
        # Accessed track is now the new headPosition
        headPosition = cur_track
    
    print('\n\nC-LOOK:')
    print("\tTotal number of seek operations =", 
          seek_count)
 
    print("\tAverage seek time =", seek_count / len(requestArray))

    print("\tWorst-case seek time =", max_seek)
 
    print("\tSeek sequence: ", end="")
    # to prevent the first comma to appear before the first element
    print("\t" + ", ".join(map(str, seek_sequence)))
    print('\n\n')
# END OF CLOOK

# Parameter value
print('\n\n')
headPosition = 50
cylinderNum = 200
size = int(input("Enter the number of I/O requests: "))
# size = 8
requestArray = random.sample(range(cylinderNum), size)

# For testing purposes, use the following requestArrayay:
# requestArray = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
print("Random Request Array generated: ", end="")
print(", ".join(map(str, requestArray)))
print('\n')

SCAN(requestArray, headPosition, cylinderNum)
CSCAN(requestArray, headPosition, cylinderNum)
CLOOK(requestArray, headPosition)
