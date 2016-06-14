import inspect

def currying(fun, *args, **kwargs):
    fun_name = fun.__name__
    f_agruments = inspect.getargspec(f)
    print(f_agruments)
    f_arguments_values = inspect.getargvalues(f)
    print(f_arguments_values)
    
