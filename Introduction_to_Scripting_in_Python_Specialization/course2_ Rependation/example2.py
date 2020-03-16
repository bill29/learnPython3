def list_minium(numbers):
    """compute minium of a list of numbers"""
    minium = numbers[0]
    for num in numbers:
        if num <= minium:
            minium = num
    return minium
def example_minium_list():
    alist = list(range(20,1000,50))
    return list_minium(alist)
print(example_minium_list())
    