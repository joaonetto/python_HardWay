import sys

script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
        next_lang = line.strip()
        raw_bytes = next_lang.encode(encoding, errors=errors)
        cooked_string = raw_bytes.decode(encoding, errors=errors)

        print(raw_bytes, "<===>", cooked_string)


languages = open("ex_23_languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

# Exemplo de utilizar o print com encode/decode
# >>> print(b"some utf-16 encoded bytestring \xc3\x90\xc2\xa2\xc3\x90\xc2\xbe\xc3\x92\xc2\xb7\xc3\x90\xc2\xb8\xc3\x90\xc2\xba\xc3\x93\xc2\xa3".decode('utf-16'))
# 潳敭甠晴㠭攠据摯摥戠瑹獥牴湩⁧郃ꋂ郃뻂鋃럂郃룂郃뫂鏃ꏂ
