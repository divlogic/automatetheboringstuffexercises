def spam():
    eggs = 99
    def bacon():
        ham = 101
        eggs = 0
        print('ham is ' + str(ham))
    bacon()
    print (eggs)


spam()