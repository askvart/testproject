#Декораторы

def uppercase(func):
    def wrapper():
        original_result = func()
        modify_result = original_result.upper()
        return modify_result
    return wrapper


@uppercase
def one():
    return 'I love you'



a = one()
print(a)
