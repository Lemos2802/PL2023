import csv
import re
import json

def campos_lista(campos):
    campos_l = []
    campos_n = []
    for i, c in enumerate(campos):
        if re.match(r".*{\d+}", c) or c == "":
            campos_l.append((i, c))
        elif re.match(r".*{\d+", c) or re.match(r"\d+}", c):
            campos_l.append((i, c))
        else:
            campos_n.append((i, c))
    return campos_n, campos_l

def tem_operacao(campo):
    match_obj = re.search(r"::(\w+)", campo)
    return match_obj.group(1) if match_obj else None

def soma(l):
    return sum(filter(None, l))

def nao_vazios(l):
    return sum(bool(i) for i in l)

def media(l):
    n = nao_vazios(l)
    return sum(l)/n if n > 0 else None

def abre_csv(file):
    with open(file, 'r', encoding="utf-8") as f:
        csvreader = csv.reader(f)
        campos = next(csvreader)
        campos_n, campos_l = campos_lista(campos)
        colecao = []
        for linha in csvreader:
            lista_operacoes = []
            d = {}
            key = None
            for i, valor in enumerate(linha):
                if (i, campos[i]) in campos_n:
                    d[campos[i]] = valor
                elif campos[i] != "" and (i, campos[i]) in campos_l and not re.match(r"\d+}", campos[i]):
                    key = campos[i].split("{")[0]
                    d[key] = [int(valor)]
                elif key is not None:
                    if tem_operacao(campos[i]):
                        lista_operacoes.append((key, tem_operacao(campos[i])))
                    if valor:
                        d[key].append(int(valor))
            if lista_operacoes:
                for k, o in lista_operacoes:
                    numeros = d[k]
                    if o == "sum":
                        r = soma(numeros)
                    elif o == "media":
                        r = media(numeros)
                    d.pop(k)
                    d[f"{k.lower()}_{o}"] = r
            colecao.append(d)
        return colecao

def abre_json(f):
    nome_json = re.match("(.*)\.csv", f).group(1)+".json"
    colecao = abre_csv(f)
    with open(nome_json, "w", encoding="utf-8") as ficheiro_json:
        json.dump(colecao, ficheiro_json, indent=4, ensure_ascii=False, separators=(",", ":"))

if __name__ == "__main__":
    abre_json("test.csv")
    abre_json("test2.csv")
    abre_json("test3.csv")
    abre_json("test4.csv")

	