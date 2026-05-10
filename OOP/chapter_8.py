# Exception handling ===================================
orders = ["first", "second", "third"]

def handle(args):
    try:
        if isinstance(args, list):
            print("it is a list ")
            print(args[3])
        elif isinstance(args, dict):
            print("It is dictionary")
            print(args["name"])
        else:
            raise ValueError("some error")
    except IndexError:
        print("Error", IndexError)
    except KeyError:
        print("Key not exists", KeyError)
    except Exception as e:
        print(e)
handle(orders)    
handle({})
handle({10,2,30})