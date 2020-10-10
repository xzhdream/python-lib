a = '''
a=1
print(a)
'''
result = compile(a,'a.py','single')
print(result.co_code,result.co_names,result.co_consts)
