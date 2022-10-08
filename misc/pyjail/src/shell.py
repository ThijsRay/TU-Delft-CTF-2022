import re

no_tricks = re.compile(r'__.+__')
banned = r"import|exec|eval|help|read|open|builtin|system|os|sys|doc|\+|input"

locals = {}
prev_locals = {}
# flag is stored in ./flag.txt

while True:
    try:
        user_input = input('>>> ').encode('utf-8').decode('ascii')
        if no_tricks.search(user_input):
            print('No tricks!')
            continue
        if re.search(banned, user_input):
            print('No banned words!')
            continue
        if '(' in user_input or ')' in user_input:
            print('No parentheses!')
            continue
        if '"' in user_input or "'" in user_input or '`' in user_input:
            print('No quotes!')
            continue
        if user_input == 'exit':
            break
        prev_locals = locals.copy()
        exec(user_input, {}, locals)
        # print the changed locals
        for k, v in locals.items():
            if k not in prev_locals or prev_locals[k] != v:
                print(k, '=', v)
    except KeyboardInterrupt:
        print('KeyboardInterrupt: Type exit to exit')
        continue
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")