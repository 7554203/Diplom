#def get_prediction(area):
#    COEF = 500_000
#    cost = area * COEF
#    return cost

def get_prediction(area):
       if (match('41', value) or match('42', value) or match('43', value)) and  value not in ('43.9', '42.9', '42.2', '43.2', '41.1', '71.1', '43.2'):  
               return 'Строительно-монтажные работы'
        if area =  '41.1':  
                print("Проектно-изыскательские работы")
        elif area in ('43.2'):  
                return 'Подключение коммуникаций'
        elif area in ('43.9', '42.9', '42.2'):  
                return 'Строительный надзор'
        else:
                return 'Прочие'