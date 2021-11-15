#%%
#based on the exercise from https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces
def scope_test():
    def do_local():
        spam = "local spam"
        print("In local scope, after local assignment:", spam)

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    print("Test spam: variable initialized as a", spam)
    do_local()
    print("In nonlocal scope, after local assignment:", spam)
    do_nonlocal()
    print("In nonlocal scope, after nonlocal assignment:", spam)
    do_global()
    print("In nonlocal scope, after global assignment:", spam)

scope_test()

print("In global scope, after global assignment:", spam)