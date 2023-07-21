# cook your dish here
for i in range(int(input())):
    DqDSA, DqTOC, DqDM = map(int,input().split(" "))
    SqDSA, SqTOC, SqDM = map(int,input().split(" "))
    DqSUM = DqDSA+DqTOC+DqDM
    SqSUM = SqDSA+SqTOC+SqDM

    if (DqSUM > SqSUM)or(DqSUM == SqSUM and DqDSA > SqDSA)or(DqSUM == SqSUM and DqDSA == SqDSA and DqTOC > SqTOC):
        print("DRAGON")

    elif (SqSUM > DqSUM)or(SqSUM == DqSUM and SqDSA > DqDSA)or(SqSUM == DqSUM and SqDSA == DqDSA and SqTOC > DqTOC):
        print("SLOTH")

    else:
        print("TIE")
