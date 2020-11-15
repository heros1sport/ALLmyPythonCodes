Paragraph = """               Humpty Dumpty __ on a wall.
               Humpty Dumpty had a great ___.
               All the king's ___,
               And all the king's ___,
               could not ___ Humpty Dumpty,
               Together again.



                                           -- Written by Nobody"""
print("Let's make a story")

list1 = []
a = ""
a = input("""Give me a past tense verb
""")
list1.append(a)
a = input("""Give me a common noun or a simple present tense verb
""")
list1.append(a)

a = input("""Give me a plural common noun
""")
list1.append(a)
a = input("""Give me a another plural common noun
""")
list1.append(a)
a = input("""Give me a simple present tense verb
""")
list1.append(a)
print("Your story is...")
print("Humpty Dumpty " + list1[0] + """ on a wall.
Humpty Dumpty had a great """  + list1[1] + """ .
All the king's """  + list1[2] + """
And all the kings """ + list1[3] + """
could not """ + list1[4] + """ Humpty Dumpty
together again. """)
