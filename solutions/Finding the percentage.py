if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total=0
    for i in range(3):  
       total+=student_marks[query_name][i]
    
    percentage=total/3
    print(f"{percentage:.2f}")