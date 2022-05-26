def f(str):
    return int(str.split(' : ')[1])


number_of_answers = 0
with open('result.txt', 'r') as file:
    number_of_answers += sum(map(f, file.readlines()[::2]))

with open('result2.txt', 'r') as file:
    number_of_answers += sum(map(f, file.readlines()[::2]))

number_of_answers_with_zabuton = 0
with open('result_zabuton.txt', 'r') as file:
    number_of_answers_with_zabuton += sum(map(f, file.readlines()[::2]))

with open('result_zabuton2.txt', 'r') as file:
    number_of_answers_with_zabuton += sum(map(f, file.readlines()[::2]))


print(number_of_answers, number_of_answers_with_zabuton, sep='\n')
