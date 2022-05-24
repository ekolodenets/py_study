'''
Expand the packed usernames
Boltabek starts his first day at the new job. He is going to refactor some data structures created by his ancestor
on this position, who seems to be not known about the data normalization.
The first task is rather easy, write a function that expands the usernames packed in the one string:
Input:
[
  ['Marek,Honza',2], ['Petr',4], ['Marija,Daniel',8], ['Mr. Karasek,Lukáš,Jan',16], ['Igor',32], ['Petra,Evgeniy',64], ['Karel',128],
]

[
    ['Marek', 2], ['Honza', 2], ['Petr', 4], ['Marija', 8], ['Daniel', 8], ['Mr. Karasek', 16],
    ['Lukáš', 16], ['Jan', 16], ['Igor', 32], ['Petra',64], ['Evgeniy',64], ['Karel',128],
]
Usernames
Usernames are separated by commas and can contain any characters. Username should be trimmed from the start/end.

[[',,,   John,,Boris  ,,     ,,', 64]] → [['John',64], ['Boris',64]]
'''

def expand_usernames(data):
    t = []
    [[t.append([j.strip(), i[1]]) if j.strip() else 0 for j in i[0].split(',') if j] for i in data]
    return t


input = [
            ['Marek,Honza',2],
            ['Petr',4],
            ['Marija,Daniel',8],
            ['Mr. Karasek,Lukáš,Jan',16],
            ['Igor',32]
            ]
# print(expand_usernames(input))
# print(expand_usernames([[',,,,John,,Boris,,,,', 64]]))
# print(expand_usernames([[',,,,, ,,', 64]]))
# print(expand_usernames([[',#,   , Ivan ,,Vladimir  ,#$%@#$%@!,&*()*&,+_)()(*&,!@#$!$^$%#&', 128]]))


# assert expand_usernames([[',,,,John,,Boris,,,,', 64]]) == [['John',64], ['Boris',64]]
# assert expand_usernames([[',,,,, ,,', 64]]) == []
# assert expand_usernames([[',#,   , Ivan ,,Vladimir  ,#$%@#$%@!,&*()*&,+_)()(*&,!@#$!$^$%#&', 128]]) == [['#', 128], ['Ivan', 128], ['Vladimir', 128], ['#$%@#$%@!', 128], ['&*()*&', 128], ['+_)()(*&', 128], ['!@#$!$^$%#&', 128]]