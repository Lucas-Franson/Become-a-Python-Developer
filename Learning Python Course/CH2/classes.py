# 
# Example file for working with classes
#

class myClass():
    def method(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2" + someString)

class anotherClass(myClass):
    def method(self):
        myClass.method(self)
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherClass method2" + someString)

def main():
    c = myClass()
    c.method()
    c.method2("This is a string")


if __name__ == "__main__":
    main()