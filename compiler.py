import yara

rules = yara.compile('result.yar')
print(rules)