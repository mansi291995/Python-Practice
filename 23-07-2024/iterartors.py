#before of iterators
# for i in "mansi":
#     print(i)

# li=[1,2,3,"amsni"]
# for i in li:
#     print(i)

#iterator is object which is used to iterate over the iterable objects
# a="mansi"
# b=iter(5)
# print(b)

#list iterator
print("list iterator")
print("-------")
list1=["fruits","flowers","vegetables"]
iter_list=iter(list1)
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
#tuple iterator
print("tuple iterator")
print("-------")
tuples=(1,2,3,4,5,"one","two")
iter_tuples=iter(tuples)
print(next(iter_tuples))
print(next(iter_tuples))
print(next(iter_tuples))
print(next(iter_tuples))
print(next(iter_tuples))
print(next(iter_tuples))
print(next(iter_tuples))
#dictionary iterator
print("dict iterator")
print("-------")
dict={"1":1,"2":2}
dict_items=iter(dict.items())
print(next(dict_items))
print(next(dict_items))


