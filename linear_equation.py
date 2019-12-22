def solve(a,b,y):
    x=-100
    while x<101:
        if a*x+b==y:
            print(x)
            return
        
        x+=1
    print("Brak rozwiązania")

solve(2,5,13)
        
