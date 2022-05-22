star = "*"
space = " "
fn_in = 6
for i in range(fn_in):
    for j in range(fn_in-1):
        print(space, end = "")
    print(star*i)
    i+=1
    fn_in-=1
    