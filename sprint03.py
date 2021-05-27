import numpy as np
from dop import F
from flask import Flask, render_template, request, url_for

# A1B1=[10, 7, 8, 6, 12, 8, 11, 10, 14, 13]
# A1B2=[12, 13, 6, 9, 8, 11, 10, 10, 13, 17]

# A2B1=[8, 14, 6, 10, 16, 14, 13, 12, 11, 15]
# A2B2=[11, 12, 12, 16, 13, 8, 10, 9, 8, 15]

# A3B1=[15, 12, 11, 9, 8, 13, 11, 12, 16, 14]
# A3B2=[13, 12, 14, 8, 6, 8, 16, 12, 14, 16]


A1B1=[5050, 4090, 6000, 6500, 8900, 2900, 2.500, 6000, 10000, 9500]
A1B2=[3800, 1050, 12900, 6900, 3950, 8000, 11200, 12400, 4900, 8900]

A2B1=[9500, 12000, 6300, 4500, 3900, 8500, 8600, 5900, 12400, 6900]
A2B2=[12000, 11500, 8900, 4400, 9800, 6900, 7200, 6200, 10500, 9200]

A3B1=[12500, 8900, 6500, 7900, 8700, 9200, 10500, 14000, 7200, 5300]
A3B2=[14500, 4300, 6700, 12400, 13200, 8400, 7900, 15200, 3200, 5500]

data = [
    [A1B1, A2B1, A3B1],
    [A1B2, A2B2, A3B2]
    ]

data = [
 [[3.6, 3.8, 4.1], [2.9, 3.1, 3.0], [2.7, 2.5, 2.9]],
 [[4.2, 4.0, 4.1], [3.3, 2.9, 3.2], [3.7, 3.5, 3.6]],
 [[3.8, 3.5, 3.6], [3.6, 3.7, 3.5], [3.2, 3.0, 3.4]],
 [[3.4, 3.2, 3.2], [3.4, 3.6, 3.5], [3.6, 3.8, 3.7]]
]

n = len(data[0][0])
p = len(data[0])
g = len(data)

print(n, p, g)

sumarize_data = []
for row in data:
    sumarize_data.append([sum(item)/len(data[0][0]) for item in row])



print(sumarize_data)
Ys = []
Zs = []


for row in sumarize_data:
    Ys.append(sum(row)/len(row))


for i in range(len(sumarize_data[0])):
    Zs.append([row[i] for row in sumarize_data])
    
Zs = [i/len(Zs[0]) for i in list(map(sum,Zs))]



print('----------------------')

for i in sumarize_data:
    print(i)

print('----------------------')
all_sr = (sum(Ys)/len(Ys) + sum(Zs)/len(Zs))/2


def Q1():
    return  n * g *  sum([pow(Z - all_sr, 2) for Z in Zs ])

def Q2():
    return n * p * sum([pow(Y - all_sr, 2) for Y in  Ys])

def Q3():
    q = 0
    for i in range(g):
        for j in range(p):
            q += pow( sumarize_data[i][j] - Zs[j] - Ys[i] + all_sr,2)
    return q * n


def Q4():
    q = 0
    for i in range(g):
        for j in range(p):
            for k in range(n):
                q += pow(data[i][j][k] - sumarize_data[i][j], 2)
    return q


def Q():
    q = 0
    for i in range(g):
        for j in range(p):
            for k in range(n):
                q += pow(data[i][j][k] - all_sr, 2)
    return q


def S1():
    return Q1() / (p-1)

def S2():
    return Q2() / (g-1)

def S3():
    return Q3() / ((p-1) * (g-1))


def S4():

    return Q4() / (N - (p*g))

def S():
    return Q() / (N-1)

factor_A = Q1()
factor_B = Q2()
factor_A_B = Q3()

factor_random = Q4()

total_dispers = Q()





print('all_srednee:', all_sr)

print('Factor A: ', factor_A)
print('Factor B: ',factor_B)
print('Factor A-B: ',factor_A_B)
print('Factor random: ',factor_random)
print('All Dispers: ',total_dispers)

print()

N = p * n * g

print('N', N)
print()
print('S1', S1())
print('S2', S2())
print('S3', S3())
print('S4', S4())
print('S', S())


print()

FA = S1() / S4()
FB = S2() / S4()
FAB = S3() / S4()

print(FA, FB, FAB)

k1 = p-2

print(k1)
k2 = N - (p*g)-1

print(k2)


print(F(0.05, k1-1, k2-1))

app = Flask(__name__)
@app.route("/")
def main():
	return render_template('main.html')


@app.route("/laba6", methods=['post', 'get'])
def sprint03():
    return render_template('laba.html')


