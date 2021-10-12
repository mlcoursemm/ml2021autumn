
def a1(x):
    return -1
    
def R():
    return 0
    
def a2(x):
    return -1
    
if __name__ == '__main__':
    print(a1(0.0), R(), a2([0.0, 0.0]))
    
    with open('seminar02_task1.txt', 'w') as f:
        for i in range(-50, 50):
            x = i/10.0
            y = a1(x)
            f.write('%d ' % y)
            
    with open('seminar02_task2.txt', 'w') as f:
        f.write('%.3f' % R())   
    
    with open('seminar02_task3.txt', 'w') as f:
        for i in range(-50, 50):
            x1 = i/10.0
            for j in range(-50, 50):
                x2 = j/10.0
                y = a2([x1, x2])
                f.write('%d ' % y) 