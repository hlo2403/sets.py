import sys
def happiness_calculator(input_score):
    n,m=map(int,input_score[0].split())
    array=list(map(int,input_score[1].split()))
    a=set(map(int,input_score[2].split()))
    b=set(map(int,input_score[3].split()))
    happiness=0
    for x in array:
        if x in a:
            happiness+=1
        elif x in b:
            happiness-=1
            
    print(happiness)
        
if __name__=="__main__":
    input_score=sys.stdin.read().splitlines()
    happiness_calculator(input_score)