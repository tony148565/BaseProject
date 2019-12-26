
import json
import os


dic = {}
count = 0
list_name =[]

def make_a_post(ins,content):
    try:
        u = '.txt'
        t = ins
        list_name.append(ins)
        name = t + u
        fp = open(name, "w")
        fp.write(content)
        fp.close()
        value = True
        print(list_name)
        with open("list_for_text.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data.append(ins)
            print(data)
        with open("list_for_text.json", "w") as jsonFile:
                json.dump(data, jsonFile)
        return value
    except ValueError:
        value = False
    return value

def look_forum(lists):
    op = 'notepad' + lists + '.txt'
    os.system(op)

def get_text():
    with open("list_for_text.json", "r") as jsonFile:
        data = json.load(jsonFile)
    return data



def uspw(user,passw):
    fp = open('user.json', "r+")
    with fp as g:
        g_dic = json.load(g)
        #print(type(g_dic))
        if user in g_dic:
            if g_dic[user] == passw:
                value = True
            else:
                value = False
        else:
            value = False
    #fp.close()
    #print(value)
    return value


def register(user,passw):
    with open("user.json", "r") as jsonFile:
        data = json.load(jsonFile)
    if user in data:
        value = True
    else:
        value = False
        data[user] = passw
        with open("user.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    return value


