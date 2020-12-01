check = True
def inputting(): ##вводим числа k,l,m,n
    global k,l,m,n
    print('Введите номер вертикали и номер горизонтали для 1 и 2 полей: ')
    while True:  ##проверяем на ошибки
        try:
            k, l = int(input('k = ')), int(input('l = '))
            m,n = int(input('m = ')), int(input('n = '))
            if 0<k<9 and 0<l<9 and 0<m<9 and 1<n<9:
                print('Для первого поля: ', k,',', l)
                print('Для второго поля: ', m,',', n)
                break
            else:
                print('Вводите числа только от 1 до 8')
        except BaseException:
            print('Вводите только числа от 1 до 8')
            pass

def field_color(): ##определяем цвет полей
    if (k+l)%2 == (m+n)%2 :
        print('а) поля одного цвета')
    else:
        print('а) поля разных цветов')
        
def queen_threat(): ##проверка угрозы ферзя
    if k==m or l==n or abs(k-m)==abs(l-n):
        print('б) ферзь угрожает полю (m,n)')
    else:
        print('б) ферзь не угрожает полю (m,n)')
        
def horse_threat(): ##проверка угрозы коня 
    if abs(k-m)==1 and abs(l-n)==2 or abs(l-n)==1 and abs(k-m)==2:
        print('в) конь угрожает полю (m,n)')
    else:
        print('в) конь не угрожает полю (m,n)')
        
def rook_move(): ##ходы ладьи
    if k==m or l==n:
        print('г) можно 1 ходом ладьи попасть на поле (m,n)')
    else:
        print('г) нельзя 1 ходом ладьи попасть на поле (m,n)')
        for i in range(8, 0, -1):
            for j in range(1, 9):
                if j==m and i==l or j==k and i==n:
                    print('   За два хода это можно сделать с таким промежуточным ходом:', j, ',', i)

            
def queen_move(): ##ходы ферзя
    if k==m or l==n or abs(k-m)==abs(l-n):
        print('д) можно 1 ходом ферзя попасть на поле (m,n)')
    else:
        print('д) нельзя 1 ходом ферзя попасть на поле (m,n)')
        for i in range(8, 0, -1):
            for j in range(1, 9):
                if abs(i-l)==abs(j-k) and abs(m-j)==abs(n-i):
                    print('   За два хода это можно сделать с таким промежуточным ходом:', j, ',', i)
                elif j==m and i==l or j==k and i==n:
                    print('   За два хода это можно сделать с таким промежуточным ходом:', j, ',', i)
                elif abs(i-l)==abs(j-k) and (j==m or i==n):
                    print('   За два хода это можно сделать с таким промежуточным ходом:', j, ',', i)
                elif (j==k or i==m) and abs(m-j)==abs(n-i):
                    print('   За два хода это можно сделать с таким промежуточным ходом:', j, ',', i)           

                
def bishop_move(): ##ходы слона
    if (k+l)%2 != (m+n)%2:
        print('е) слоном нельзя попасть на поле (m,n)')
    else:
        if abs(k-m)==abs(l-n):
            print('e) можно 1 ходом слона попасть на поле (m,n)')
        else:
            print('е) нельзя 1 ходом слона попасть на поле (m,n)')
            for i in range(8, 0, -1):
                for j in range(1, 9):
                    if abs(i-l)==abs(j-k) and abs(m-j)==abs(n-i):
                        print('   За два хода это можно сделать с таким промежуточным ходом:', j, ',', i )
                        
def choising(): ## реализовываем возможность совершать работу программы много раз
    global check
    choise = input('Чтобы выполнить заново введите 1, для прекращения работы - любой другой символ: ')
    if choise == '1':
        check = True
    else:
        check = False
                        
if __name__ == '__main__': ## выводим все методы
    while check:
        inputting()
        field_color()
        queen_threat()
        horse_threat()
        rook_move()
        queen_move()
        bishop_move()
        choising()
    
    