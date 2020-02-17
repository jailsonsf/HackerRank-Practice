def merge_the_tools(string, k):
    n_parts = int(len(string) / k)

    for i in range(n_parts):
        sub_string = string[i * k : (i + 1) * k]

        result = ''


        for char in sub_string:
            if char not in result:
                result += char

        print(result)


string, k = input(), int(input())
merge_the_tools(string, k)
