if __name__ == "__main__":
    int_x = 10
    print(f'The variable int_x is of the type {type(int_x)}')

    float_y = 2345.67
    print(f'The variable float_y is of the type {type(float_y)}')

    complex_var = 3 + 20j
    print(f'The variable complex_var is of the type {type(complex_var)}')

    myList = [1,2,3, "hello", 43.26, complex_var]
    print(f'The variable myList is of the type {type(myList)}')

    myTuple = ("abcd", int_x, float_y, myList)
    print(f'The variable myTuple is of the type {type(myTuple)}')

    myDict = {
        "James": "SCT211-5454-1970",
        "Peter": "SOB445-0001-2005",
        "Annette": "ADT399-999-2028",
    }
    print(f'The variable myDict is of the type {type(myDict)}')

    mySet = {complex_var, "Name", 399}
    print(f'The variable mySet is of the type {type(mySet)}')

    is_learning = False
    print(f'The variable is_learning is of the type {type(is_learning)}')

    print("Conversion or casting of float to int and vice versa")
    print(f'Variable float_y which was a float is now of type {type(int(float_y))} using the int() casting function')
    print(f'Variable int_x which was an int is now of type {type(float(int_x))} using the float() casting function')

