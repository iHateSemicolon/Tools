print('중간 점수 입력')
middle_score = int(input())
print('기말 점수 입력')
final_score = int(input())
print('수행평가 점수 입력')
Lil_test = int(input())

result = (middle_score * 0.3) + (final_score * 0.3) + Lil_test 

if result >= 90:
    level = 'A'
    
elif result >= 80:
    level = 'B'
    
elif result >= 70:
    level = 'C'
    
else:
    print('병신')
    

print('최종 점수는', result,'로', '등급은', level,'입니다')
