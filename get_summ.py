def get_summ(one, two, delimiter='&'):
    one=one.capitalize()
    two=two.capitalize()
    return f'{one}{delimiter}{two}'
 
one='Learn'
two='python'
print(get_summ(one, two))