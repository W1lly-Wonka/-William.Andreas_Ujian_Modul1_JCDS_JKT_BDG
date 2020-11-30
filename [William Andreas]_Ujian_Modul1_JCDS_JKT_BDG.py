'''
soal no 1
Buatlah suatu fungsi yang mengembalikan panjang terpendek dari suatu string kata yang terpisahkan oleh spasi (20 Point) 
Note: Kembalikan panjang atau len dari kata yang terpendek, bukan katanya yang dikembalikan.
'''

# def find_short(text):
#     kalimat, d = text.split(), {}
#     for i in kalimat:
#         d[i] = len(i)
#     print (f"The shortest word has {min(d.values())} char(s)")

# find_short("Many people get up early in the morning") # The shortest word has 2 char(s)
# find_short("Every office would getting newest monitor") # The shortest word has 5 char(s)
# find_short("Create new file after this morning") # The shortest word has 3 char(s)


'''
soal no 2

Buatlah suatu fungsi yang menerima parameter angka positif, dan mengembalikan total berapa kali harus dikalikan digit dari angka tersebut hingga mencapai 1 digit. Yang harus diperhatikan:

    Jika user menginput value kurang dari nol atau negatif, maka akan di print "Please input positive number only"
'''

# def persistence(no):
#     counter=0
#     if no > 0:
#         while no > 9:
#             counter+=1
#             no_str=str(no)
#             total=1
#             for i in no_str:
#                 total=total* int(i)
#             no=total
#         print (counter)
#     else:
#         print ("Please input positive number only")

# persistence(39)
# persistence(999)
# persistence(4)
# persistence(-12)
