# # n=[1,2,3,'mansi','ekbote',4,5]
# # # for i in n:
# # #     print(i)

# # a=[i for i in n]
# # print(a)
# # b=[i**2 for i in n]
# # print(b)
# # numbers = [1, 2, 3, 4, 5]
# # print([num ** 2 for num in numbers])
num=["h.pdf","hello.py"]
a=([i.split('.')[-1]for i in num])
print(a)


file_name = ["doc1.ppt", "doc2.pdf", "doc3.jpg", "doc4.py"]

print([file.split(".")[-1] for file in file_name])
list=["abc@gmail.com","xyz@gmail.com","hello"]
print([email for email in list if email.endswith("@gmail.com")])
