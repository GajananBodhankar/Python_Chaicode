# file handling using exception
# file= open("D:\GenerativeAndAgenticAIPython\OOP\order.txt", 'w')
# try:
#     file.write("Hello from gajanan")
# except:
#     print("error occured")
# finally:
#     file.close()

with open("D:\GenerativeAndAgenticAIPython\OOP\order.txt", 'w') as file:
    file.write("hello")