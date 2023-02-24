if __name__=="__main__":
    import sys  
    file = open("/etc/hosts","rt")
    content = file.readlines()
    file.close()
    found = False

    for x in range(len(content)):
        line = content[x]
        if (sys.argv[1] in line):
            content[x] = sys.argv[1] + " " + sys.argv[2] + "\n"
            found = True

    if (not found):
        content.append(sys.argv[1] + " " + sys.argv[2] + "\n") 

    file = open("/etc/hosts","wt")
    file.write("".join(content))
    file.close()
    exit(0)
    