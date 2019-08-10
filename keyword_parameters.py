''' This is a greeting function '''

def say_hi(name="user"):
    return (f"hi {name}")

def give_chocolates(n,name='user'):
    print(f"{name}, you get {n} chocolate")

if __name__ == '__main__':
    #say_hi()
    #ay_hi("Ag")
    give_chocolates(5,'Ag')
    give_chocolates(5)
