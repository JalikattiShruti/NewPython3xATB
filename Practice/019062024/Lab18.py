# def outer_function():
  #  var1 = 30

   # def inner_function():
       # print(var1)

    # inner_function()


# outer_function()



def outer_function():
    var1 = 30

    def inner_function():
      inner_function()


    def inner_function_1():
        print(var1)
    inner_function_1()


outer_function()


outer_function()












