from one import count, add

def test_count():
    answer = count()
    right_answer = [1,2,3,4,5]
    if answer == right_answer:
        print("Count is good!")
        return True
    else:
        print("Count is bad! Expected {}, but got {}".format(
            right_answer, answer))
        return False

def test_add():
    for a in range(100):
        for b in range(100):
            answer = add(a,b)
            right_answer = a+b
            if answer != right_answer:
                print("Add is bad! Expected {}, but got {}".format(
                right_answer, answer))
                return False
