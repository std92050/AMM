def eval_loop():
    print('key in done when done')
    while True:
        X=input('type something  ')
        if X=="done":
            break
        eval(X)
        print(eval(X))
       
            
