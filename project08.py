def read_file(file_name):
    with open(file_name, 'r',encoding="utf-8") as file:
        lines = file.readlines()
        recepts = dict()
        for line in lines:
            splitted_line = line.split('^')
            if len(splitted_line) < 4:
                continue
            name = splitted_line[1]
            ingreds = splitted_line[3]
            recept = splitted_line[-2].replace('\\n','\n').strip()
            dict_ing = dict()
            splitted_ingerds = ingreds.split(' - ')

            for i in range(0, len(splitted_ingerds), 2):
                if i >= len(splitted_ingerds) -1:
                    break
                numbers = splitted_ingerds[i+1].split()
                if len(numbers) == 0:
                    continue
                if numbers[0][0].isdigit():
                    dict_ing[splitted_ingerds[i]] = splitted_ingerds[i+1]
                else:
                    dict_ing[splitted_ingerds[i]] = 'По вкусу'
                    dict_ing[splitted_ingerds[i+1]] = 'По вкусу'
            recepts[name] = [dict_ing, recept]

    return recepts

if __name__ == '__main__':
    tmp = read_file(r'C:\Users\Анастасия\Desktop\прога\cooking_bot\receipts2.txt')
    for k in tmp:
        print(k,tmp[k])
        break


