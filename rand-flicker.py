from random import randint
from moviepy.editor import *

# create list of frames

array = []
for x in range(0, NUMBER_OF_FRAMES):
    array.append(int(x))
frameArray = []

# prepare flexible lengths for list

orig_length = len(array)
length = orig_length
print(orig_length)

# pick a number either from sequence or randomly with less randomness over time and remove the from the original list

for y in range(0, orig_length):
    number = randint(0, 101)
    probability = int(90 + (-80 * y / orig_length))
    if number < probability:
         index = randint(0,length-1)
    else:
        index = 0
    i = int(array[index]+20901)
    poz = str(i)
    if i < 10: # fix image numbers
        poz = '0000' + poz
    elif i < 100:
        poz = '000' + poz
    elif i < 1000:
        poz = '00' + poz
    elif i < 10000:
        poz = '0' + poz

    frameArray.append(‘/FOLDER/' + poz + '.png') #poz should reflect the number of a frame
    array.remove(array[index])
    length -= 1

result = ImageSequenceClip(frameArray, fps=25)
result = result.to_videofile(‘/FOLDER/result.mp4', fps=25) # many options available
