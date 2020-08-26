"""Linear Regression with one variable"""
#Taking data from csv file
data_file=open("Linear_Regression_one_variable.csv",'r')
data_dic={} #dictionary containing the data
x=[] #Size of the houses
y=[] #price of the houses
for lin in data_file:
    a=lin.strip().split(",")
    data_dic[a[0]]=a[1]
    if a[0].isnumeric():
        x.append(a[0])
        y.append(a[1])
m=len(x)
def hypo(xi,o0,o1):
    hy=o0+o1*int(xi)
    return hy
def sum_hypo_0(f_o0,f_o1):
    s = 0
    for i in range(m):
        s += hypo(x[i], f_o0, f_o1) - int(y[i])
    return s
def sum_hypo_1(f_o0,f_o1):
    s = 0
    for i in range(m):
        s += (hypo(x[i], f_o0, f_o1) - int(y[i]))*int(x[i])
    return s
def J(f_o0,f_o1):
    s = 0
    for i in range(m):
        s += (hypo(x[i], f_o0, f_o1) - int(y[i]))
    return (1/(2*m))*s
err=1
temp_o0=0.25
temp_o1=230
alp=10
while err>0.2:
    fin_o0 = temp_o0
    fin_o1 = temp_o1
    temp_o0=fin_o0-alp*(1/m)*sum_hypo_0(fin_o0,fin_o1)
    temp_o1=fin_o0-alp*(1/m)*sum_hypo_1(fin_o0,fin_o1)
    err=J(fin_o0,fin_o1)
    err=float("{:.4f}".format(err))

