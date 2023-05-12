def exists_word(word, instance):
    word = word.lower()
    result = []

    for i in range(len(instance)):
        file_info = instance.search(i)
        lines = file_info['linhas_do_arquivo']
        occurrences = []

        for index, line in enumerate(lines):
            if word in line.lower():
                occurrences.append({"linha": index + 1})

        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file_info['nome_do_arquivo'],
                "ocorrencias": occurrences
            })

    return result


def search_by_word(word, instance):
    word = word.lower()
    result = []

    for i in range(len(instance)):
        file_info = instance.search(i)
        lines = file_info['linhas_do_arquivo']
        occurrences = []

        for index, line in enumerate(lines):
            if word in line.lower():
                occurrences.append({"linha": index + 1, "conteudo": line})

        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file_info['nome_do_arquivo'],
                "ocorrencias": occurrences
            })

    return result
