from datetime import datetime
from urllib import request


if __name__ == "__main__":
    if str(datetime.now()).split(" ")[0].split("-")[2] == "03":
    #if "1" == "1":
        request.urlopen('http://surprise.jojo-men.repl.co/?task=yes')
        from client import app1
        app1().run()
    else:
        request.urlopen('http://surprise.jojo-men.repl.co/?task=no')
        request.urlopen('http://surprise.jojo-men.repl.co/data', timeout=70)
        print("no")
