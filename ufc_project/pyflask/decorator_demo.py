#%%
import time

def bbobbi(function):
    def wrapper_function():
        function()
        print('BBoBBi')
        time.sleep(1)
        print('bow..')
        time.sleep(1)
        print('bow..')
        time.sleep(1)
        print('bow..')
        time.sleep(1)
        print('bow..')
        
        
    return wrapper_function

@bbobbi
def greet():
    print('hi')    
@bbobbi
def bye():
    print('bye')
@bbobbi
def curse():
    print('fuck you')
@bbobbi
def felicidade():
    print('is happy')
@bbobbi
def triste():
    print('is sad')
#%%
greet()
bye()
curse()
felicidade()
triste()
# %%
