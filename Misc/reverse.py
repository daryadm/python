def reverse(text):
    tlist = []
    nlist = []
    word = ""
    for char in str(text):
        tlist.append(char)


    for i in range(len(tlist)):


        nlist.append(tlist[len(tlist) -1 - i])
    for char in nlist:
        word += char
    print(word)



reverse("Python!")
reverse("dasha")
reverse("abcd")


#codeacademy
# def reverse(text):
#     word = ""
#     l = len(text) - 1
#     while l >= 0:
#         word = word + text[l]
#         l -= 1
#     return word
#