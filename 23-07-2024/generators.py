# list1=[1,2,3,4,5,6]
# def gen():
#     a=0
#     b=1
#     c=a+b
#     yield c

# gen_items=gen()
# for i in gen_items:

#     print(gen_items)

#generator uses yield statement same as return statement
def simple_generator():
    list1=[1,2,3,4]
    yield list1

gen = simple_generator()
for value in gen:
    print(value)

def gen(n):
    yield n
#generator
for i in range(4):

    gen_val=gen(4)
    print(next(gen_val))