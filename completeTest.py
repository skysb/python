class MyClass:

    #My comment to define a method
    def a_method(a,b):
        res = 0
        for i in range(0,5):
            res += a + b
        return res

if __name__ == '__main__':
    print(MyClass.a_method(1,2))
    