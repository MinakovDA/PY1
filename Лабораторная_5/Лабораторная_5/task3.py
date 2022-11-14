from random import randint

def throw_me_some_numbers(start = -10,stop = 10,list_size = 15) -> list[int]:

    uni = []
    while len(uni) != list_size:
        random = randint(start, stop)
        if random not in uni:
            uni.append(random)
    return uni


some_numbers = throw_me_some_numbers()
print(some_numbers)
print(len(some_numbers) == len(set(some_numbers)))
