# rand-flicker
## description
A ready-made sequence of video frames gets reorganized based on the following formula: 
chance of randomness of specific frame = 100 - (number of specific frame * 100 / overall number of yet unused frames)

The randomness of picking frames declines with duration and the available pool of unused frames, i.e. the sequence gets more organized over time. The result of this is that the 0th frame has a 100% chance of being randomly picked from the pool. The last frame has 0% chance of being random.
## instructions
Specify folder with prepared frames named [0.png, 1.png, 2.png, ...].
## dependencies
moviepy, NumPy
