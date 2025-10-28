def ticket(n,line):
    late = 0
    serve = 0
    for student in line:
        if student == 'TAKE':
            late = late + 1
            serve = serve + 1
        elif student == 'SERVE':
            serve = serve - 1
        elif student == "CLOSE":
            n = n+late
            print(f"{late} {serve} {n}")
            late = 0
            serve = 0
ticket(23,['TAKE','TAKE','SERVE','TAKE','SERVE','SERVE','CLOSE','TAKE','TAKE','TAKE','SERVE','CLOSE','TAKE','SERVE','TAKE','SERVE','TAKE','TAKE','TAKE','TAKE','TAKE','TAKE','SERVE','CLOSE','EOF'])