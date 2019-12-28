import re
import csv

# 将跨行命令拼接在一起
def cat_multilines(lines):
    result = []

    for line in lines:
        line.strip()

    sz = len(lines)

    i=0
    while i<sz:
        tokens = [x for x in lines[i].split(" ") if x]
        if len(tokens) <= 1:
            i = i+1
            continue
        j = 1



        while(tokens[len(tokens)-1] == "\\" or len(tokens[len(tokens)-1].split("\\"))>1):
            if tokens[len(tokens)-1] == "\\":
                tokens.pop()
            else:
                tokens[len(tokens)-1] = tokens[len(tokens)-1].split("\\")[0]
            if i+j >= sz:
                break
            tokens += [x for x in lines[i+j].split(" ") if x]
            j += 1
        tmp_str = ""
        for token in tokens:
            tmp_str += token + " "
        result.append(tmp_str.strip())
        i = i+j
    return result

def split_double_and(lines):
    result = []

    for line in lines:

        cmd = line.strip().split(" ")[0]

        line.strip()
        ls = line.split("&&")
        for i in range(len(ls)):
            if i != 0:
                result.append(cmd + " " + ls[i].strip())
            else:
                result.append(ls[i].strip())
    return result

def is_url(line):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, line)
        

def parse(line):
    stop_words = ["RUN", "run", "apt-get", "install", "&&", "update"]

    # TODO： parse ENV but not parse ARG

    package_list = []

    tokens = line.split(" ")
    if (len(tokens) <= 2) or (tokens[0] != "RUN" and tokens != "run"):
        return "none", False
    # tokens[0] should be "run" or "RUN", tokens[1] should be "apt-get" or "apt" or "pip"
    if tokens[1] == "apt-get" or tokens[1] == "apt" or tokens[1] == "apt-install":
        if 'install' in tokens:
            for token in tokens:
                if token.strip() not in stop_words and not re.match('-.*', token.strip()) \
                    and not re.match('--.*', token.strip()) and not re.match('Dpkg::.*', token.strip()) \
                        and not re.match('[0-9].*', token.strip()) and not re.match('/.*', token.strip()):
                    package_list.append("apt_" + token.strip().split("=")[0])

    if (tokens[1] == "pip"):
        if '-r' not in tokens and '-e' not in tokens:
            # -r means there's requirements.txt in this pip command. Either process or not ids further consideration.
            if 'install' in tokens:
                for token in tokens:
                    if token is tokens[1]:
                        continue
                    token = token.strip("\"").strip("\'")
                    if token not in stop_words and not re.match('-.*', token) and not re.match('--.*', token) \
                        and not re.match('\$.*', token) and not re.match('/.*', token) and not is_url(token):
                        package_list.append("pip_" + token.split("==")[0].split(">=")[0].split("<=")[0].split(">")[0].split("<")[0])
    
    if len(package_list) == 0:
        return [], False
    return package_list, True

# filepath = "sample_dockerfile/files/1/Dockerfile"
def parsefile(filepath):
    f = open(filepath)
    lines = split_double_and(cat_multilines(f.read().splitlines()))
    package_list = []
    for line in lines:
        pack_name_list, flag = parse(line)
        if flag:
            package_list += pack_name_list
    return package_list

'''
f = open("package_data.csv", 'w')
f_csv = csv.writer(f)

filepath = "sample_dockerfile/files/" + "35" + "/Dockerfile"

lst = parsefile(filepath)

if lst:
    print(lst)
if lst:
    f_csv.writerow(lst)

'''
f = open("package_data.csv", 'w')
f_csv = csv.writer(f)
for i in range(2000):
    filepath = "sample_dockerfile/files/" + str(i) + "/Dockerfile"
    lst = parsefile(filepath)
    if lst:
        print(i)
        print(lst)
    if lst:
        f_csv.writerow([i] + lst)
