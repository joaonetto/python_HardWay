import ex_25_functions

sentence = "All good things come to those who wait."
print(f"A frase utilizada foi: \n\t{sentence}\n")

words = ex_25_functions.break_words(sentence)
print(f"A frase foi dividida por cada palavra, veja abaixo:\n\t{words}\n")

sorted_words = ex_25_functions.sort_words(words)
print(f"A frase foi organizada em ordem alfabetica, veja:\n\t{sorted_words}\n")

print(f"A primeira palavra da frase é:\n\t{ex_25_functions.print_first_word(words)}\n")

print(f"A última palavra da frase é:\n\t{ex_25_functions.print_last_word(words)}\n")

print(f"A primeira e a última palavra foram retiradas - POP, o resultado é:\n\t{words}\n")

print(f"A primeira palavra da frase em ordem alfabetica é:\n\t{ex_25_functions.print_first_word(sorted_words)}\n")

print(f"A última palavra da frase em ordem alfabetica é:\n\t{ex_25_functions.print_last_word(sorted_words)}\n")

print(f"A primeira e a última palavra foram retiradas da ordem alfabetica - POP, o resultado é:\n\t{sorted_words}\n")

sorted_words = ex_25_functions.sort_sentence(sentence)
print(f"A frase foi recuperada e organizada em ordem alfabetica, veja:\n\t{sorted_words}\n")

print("A primeira e a última palavra da frase, veja:\n\t{}\n\t{}\n".format(*ex_25_functions.print_first_and_last(sentence)))

print("A primeira e a última palavra da frase em ordem alfabetica, veja:\n\t{}\n\t{}\n".format(*ex_25_functions.print_first_and_last_sorted(sentence)))
