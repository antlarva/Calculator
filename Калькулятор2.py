while True:
    try:
        if 'itog' in locals() and itog != 0:
            print('Предыдущий результат:', itog)
            numa = str(itog)
        else:
            numa = (input('Введите первое число: '))
        if numa.lower() == 'stop':
            break
        numb = (input('Введите второе число: '))
        if numb.lower() == 'stop':
            break
        elif numb.lower() == 'c':   #c=clear
            itog = 0
            print('Результат обнулился')
            continue
        
        num1 = float(numa)
        num2 = float(numb)
        
        dev1 = ('/')
        dev2 = ('*')
        dev3 = ('+')
        dev4 = ('-')
    
        print('Список действий:''/ -- деление,', '* -- умножение,', '+ -- плюс,', '- -- минус')
        funct = (input('Введите действие: '))
        if funct.lower() == 'stop':
            break
        elif funct.lower() == 'c':   #c=clear
            itog = 0
            print('Результат обнулился.')
            continue

        if funct == dev1:
            itog = num1 / num2
        elif funct == dev2:
            itog = num1 * num2
        elif funct == dev3:
            itog = num1 + num2
        elif funct == dev4:
            itog = num1 - num2
        else:
            print('Неправильное действие.')
            continue

        print('Результат:', itog)
    except ValueError:
        print('Ошибка: ValueError. Лучше введите число.')
        continue
    except NameError:
        print('Ошибка: NameError. Неправильное действие.')
        continue
    except OverflowError:
        print('Ошибка: OverFlowError. Слишком большое/маленькое число')
        continue