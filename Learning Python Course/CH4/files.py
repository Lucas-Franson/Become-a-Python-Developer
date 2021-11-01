



def main():
    f = open("textfile.txt", "r") # w+, a, r


    # for i in range(10):
    #     f.write("This is line " + str(i) + "\r\n")

    if f.mode == 'r':
        # contents = f.read()
        fl = f.readlines()
        for x in fl:
            print(x)
        
        # print(contents)


    f.close()

if __name__  == "__main__":
    main()