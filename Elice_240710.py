the_world_is_flat = False
if the_world_is_flat:
    print("Be careful not to fall off!")
else:
    s = input("Input Number: ")
    stack = []
    i = 0

    while i < len(s):
        if s[i].isdigit():
            # 숫자가 나오면, stack에 추가
            stack.append(s[i])
        elif s[i] == '(':
            # 여는 괄호가 나오면, 새로운 부분 문자열의 시작을 의미
            stack.append(s[i])
        elif s[i] == ')':
            # 닫는 괄호가 나오면, stack에서 문자열을 만들어낸다
            substr = ""
            while stack and stack[-1] != '(':
                substr = stack.pop() + substr
            stack.pop() # 여는 괄호 '(' 제거
            k = int(stack.pop()) # 반복 횟수

            # 반복된 문자열을 stack에 추가
            stack.append(substr * k)
        else:
            # 알파벳은 그대로 stack에 추가
            stack.append(s[i])
        i += 1

    # stack에 남아있는 모든 문자열을 합친다
    print(len(''.join(stack)))