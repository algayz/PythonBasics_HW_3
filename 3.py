letter = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JZШЭЮ', 10: 'QZФЩЪ'}

word = input("Введите слово на русском или английском языке: ").upper() 
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNMАВЕИНОРСТДКЛМПУБГЁЬЯЙЫЖЗХЦЧШЭЮФЩЪ':
        for j in letter:
            if i in letter[j]:
                count = count + j
   
print(f'Стоимость слова: {count}')