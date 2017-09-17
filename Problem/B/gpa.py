def calculate(grade):
    gpa = 0
    div = 0
    for i in grade:
        gpa = gpa + i[0]*i[1]
        div = div + i[0]
    return gpa/div

def getsum(grade):
    cou = 0
    for i in grade:
        cou = cou+ i[0]
    return cou

grade_1_1 = [
    (2,3.3),
(2,3.8),
(5,3.8),#
(2,2.8),
(2,3.6),
(5,3.8),#
(3,3.8),
(2,3.5)]
grade_1_2 = [
    (3.5,3.8),
(3,3.2),
(5,2.7),#
(4,2.4),
(2,3.6),
(1,3.9)]
grade_2_1 = [
    (4,3.5),#
(4.5,3.8),
(5,3.6),#
(4,2.9),
(1,3.6),
(2,3.6)]
grade_2_2 = [
    (2,3.8),
(2,3.9),
(3.5,3.5),
(3.5,2.6),#
(0.5,3.7),
(3.5,2.5),#
(2.5,2.7)#]
print(calculate(grade_1_1))
print(getsum(grade_1_1))
print(calculate(grade_1_2))
print(getsum(grade_1_2))
print(calculate(grade_2_1))
print(getsum(grade_2_1))
print(calculate(grade_2_2))
print(getsum(grade_2_2))