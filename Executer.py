filename = input("link source : ") + ".py"
while True:
    input("Press Enter to execute code")
    f = open(filename,'rt')
    code = compile(f.read(), filename, 'exec')
    try:
        exec(code)
    except:
        print("ERROR")
    f.close()
