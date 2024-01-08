import random

# START OF SCAN
def SCAN(requestArray, headPosition, cylinderNum):
 
    seek_count = 0
    max_seek = 0
    distance, currentTrack = 0, 0
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
        currentTrack = right[i]
             
        seek_sequence.append(currentTrack)
 
        distance = abs(currentTrack - headPosition)
 
        seek_count += distance

        max_seek = max(max_seek, distance)
 
        headPosition = currentTrack
         
    # Scanning left
    for i in range(len(left) - 1, -1, -1):
        currentTrack = left[i]
 
        seek_sequence.append(currentTrack)
 
        # Calculate absolute distance
        distance = abs(currentTrack - headPosition)
 
        seek_count += distance

        max_seek = max(max_seek, distance)
 
        headPosition = currentTrack
    
    print('SCAN:')
    print("\tTotal seek time =", 
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
    distance, currentTrack = 0, 0
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
        currentTrack = right[i]
 
        seek_sequence.append(currentTrack)
 
        distance = abs(currentTrack - headPosition)
 
        seek_count += distance

        max_seek = max(max_seek, distance)
 
        headPosition = currentTrack
 
    # Consider the return seek time from right to left
    max_seek = max(max_seek, headPosition);
    headPosition = 0
 
    seek_count += (cylinderNum - 1)
 

    for i in range(len(left)):
        currentTrack = left[i]
 

        seek_sequence.append(currentTrack)
 
        distance = abs(currentTrack - headPosition)
 
        seek_count += distance

        max_seek = max(max_seek, distance)
 

        headPosition = currentTrack
    
    print('\n\nC-SCAN:')
    print("\tTotal seek time =", 
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
    distance, currentTrack = 0, 0
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
        currentTrack = right[i]
 
        seek_sequence.append(currentTrack)
 
        distance = abs(currentTrack - headPosition)
 
        seek_count += distance

        max_seek = max(max_seek, distance)
 
        headPosition = currentTrack
 
    if len(left) != 0:
        seek_count += abs(headPosition - left[0])
        max_seek = max(max_seek, abs(headPosition - left[0]));
        headPosition = left[0]

    for i in range(len(left)):
        currentTrack = left[i]
 
        # Appending current track to seek sequence
        seek_sequence.append(currentTrack)
 
        # to find absolute distance
        distance = abs(currentTrack - headPosition)
 
        # to increase the total count
        seek_count += distance

        # to check if this distance is the max seek
        max_seek = max(max_seek, distance)
 
        # make the currently accessed track the new headPosition
        headPosition = currentTrack

    
    print('\n\nC-LOOK:')
    print("\tTotal seek time =", 
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
