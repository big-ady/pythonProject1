def count_calls():
    global calls
    calls += 1

calls = 0

def string_info(s):
    length = len(s)
    count_calls()
    upper_case = s.upper()
    lower_case = s.lower()

    return length, upper_case, lower_case
count_calls()
length, upper_case, lower_case = string_info('Capybara')
print(length, upper_case, lower_case)
length, upper_case, lower_case = string_info('Armageddon')
print(length, upper_case, lower_case)

def is_contains(string, list_of_strings):
    list_of_strings = [s.lower() for s in list_of_strings]
    result = string.lower() in list_of_strings
    return result
count_calls()
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)