user_input = input("请输入你想翻译的句子")
char_list = list(user_input)
result = ""
for char in char_list:
    if char.isalnum():
        result += char + "儿"
    else:
        result += char
print(result)
