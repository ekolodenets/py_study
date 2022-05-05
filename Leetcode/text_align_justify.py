'''
Text align justify

Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and
the expected justification width. The longest word will never be greater than this width.

Here are the rules:

-Use spaces to fill in the gaps between words.
-Each line should contain as many words as possible.
-Use '\n' to separate lines.
-Gap between words can't differ by more than one space.
-Lines should end with a word not a space.
-'\n' is not included in the length of a line.
-Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
-Last line should not be justified, use only one space between words.
-Last line should not contain '\n'
-Strings with one word do not need gaps ('somelongword\n').

Example with width=30:

Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
'''




def increase(temp, e):
    while True:
        if len(temp) == 1:
            return temp
        for i in range(len(temp)):
            if isinstance(temp[i], int):
                temp[i] += 1
                e -= 1
                if e == 0:
                    break
        if e == 0:
            break
    return temp

def justify(text, width):
    words = text.replace(' ', '  ').split(' ')                              # replace ' ' with '  '
    x = [1 if i == '' else i for i in words]                                # replace '' with 1
    l = []
    temp = []
    counter = 0

    for index, word in enumerate(x):
        if index == len(x)-1 or len(str(x[index + 1]))+counter+1 > width:     # if the next word is longer than the width
            temp.append(word)
            counter += len(str(word))
            if temp[-1] == 1:                                               # if the last word is 1
                temp.pop(-1)
                counter -= 1
            if width-counter > 0:                                           # if the width is greater than 0
                increase(temp, width-counter)
            temp[-1] = temp[-1] + '\n'                                      # add a new line
            for i in range(len(temp)):                                      # convert numbers into spaces
                if isinstance(temp[i], int):
                    temp[i] = temp[i] * ' '
            a = ''.join(temp)
            l.append(a)
            temp = []
            counter = 0
        else:
            temp.append(word)
            if temp[0] == 1:
                temp.pop(0)
                counter -= 1
            counter += len(str(word))
    l[-1] = l[-1][:-1]                                                     # remove the last new line
    l[-1] = ' '.join(''.join(l[-1]).split())                               # remove additional the spaces from the last line
    return ''.join(l)


# t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris,"

t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris," \
    " at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit " \
    "amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus " \
    "tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, " \
    "non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus " \
    "felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. " \
    "In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend " \
    "tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta " \
    "lacus, ut elementum justo nulla et dolor."

print(justify(t, 30))
