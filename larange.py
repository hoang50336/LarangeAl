import numpy

def convolution(u, v, w, n):
    for i in range(1,n+4):
        for j in range(1,i+1):
            numpy.put(w, i, w[i] + u[j]*v[i-j+1])

def larange(x, y, n):
    l = [0]
    p = [0]
    w = [0]

    #Khởi tạo giá trị
    for i in range(1,n+3):
        l.append(float(0))
        w.append(float(0))
        if i == 1:
            p.append(float(1))
        else:
            p.append(float(0))

    l.append(float(0))
    p.append(float(0))
    w.append(float(0))

    l = numpy.array(l)
    p = numpy.array(p)
    w = numpy.array(w)
    print("l = ",l)
    print("p = ",p)
    print("w = ",w)

    for i in range(1, n+2):
        #Reset p[]
        for j in range(1, n+2):
            if j == 1:
                numpy.put(p, j, 1)
            else:
                numpy.put(p, j, 0)
        for j in range(1, n+2):
            if i != j:
                v = []
                for k in range(n+4):
                    v.append(float(0))
                v = numpy.array(v)
                for k in range(1, n+2):
                    if k == 1:
                        numpy.put(v, k, 1)
                    elif k == 2:
                        numpy.put(v, k, -x[j-1])
                    else:
                        numpy.put(v, k, 0)
                convolution(p, v, w, n)
                for k in range(1,n+2):
                    numpy.put(p, k, (w[k]/(x[i-1] - x[j-1])))
                    print("\n-%d-%d-%d-" %(i, j, k), end=" ")
                    print("p = ", p, end=" ")
                    print("w = ", w)
        for j in range(1,n+2):
            numpy.put(l, j, l[j] + p[j]*y[i-1])
    print("l = ",l)

n = int(input("Nhap. vao` bac. cua? da thuc': "))
x = [0]
y = [0]

for i in range(n+1):
    x.append(float(input("x[%d] = " %i)))
    y.append(float(input("y[%d] = " %i)))

for i in range(2):
    x.append(float(0))
    y.append(float(0))

x = numpy.array(x)
y = numpy.array(y)
print("x = ",x)
print("y = ",y)

# print("He. so' cua? da thuc' bac. %d tuong ung' la`: " %(n))
larange(x, y, n)