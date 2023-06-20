import os, json
program_dir = os.getcwd()
config_file = os.getcwd()+"\\bin\\config.json"
def load_config():
    config = {}
    if os.path.exists(config_file):
        with open(config_file,"r") as f:
            return json.loads(f.read())
    else:
        _temp = [[],[],[]]
        with os.scandir(program_dir+"\\tests") as it:
            for x in it:
                _temp[0].append(x.name)
        with os.scandir(program_dir+"\\tests\\") as it:
            for y in it:
                _temp[1].append(os.fspath(y.path))
        with os.scandir(program_dir+"\\student_answers\\") as it:
            for entry in it:
                _temp[2].append(os.fspath(entry.path))
        for x in range(len(_temp[0])):
            config[_temp[0][x]] = {
                "test_dir": _temp[1][x],
                "stud_ans_dir": _temp[2][x]
            }
        with open(config_file,"w") as f:
            f.write(json.dumps(config))
        return load_config()
    
def save_config(conf):
    with open(config_file, 'w') as f:
        f.write(json.dumps(conf))
    print("complete")
    return "saved"


def read_answers(path):
    content = []
    with open(path) as f:
        content = f.read().splitlines()
    return content

def save(content, filename):
    if type(content) is type([]):
        with open(str(filename)+".txt", 'w') as f:
            f.write(str(content))


def check(question_answers, actual_answers):
    correct_answers = 0
    incorrect_answers = 0
    percent = 0
    students_answers = len(actual_answers)
    total_answers = len(question_answers)
    for x in range(len(question_answers)):
        if str(question_answers[x]).lower() == str(actual_answers[x]).lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
    percent = round(((correct_answers/total_answers)*100), 2)
    #print("Correct answers: "+str(correct_answers))
    #print("Incorrect answers: "+str(incorrect_answers))
    #print("Percentage of correct answers: "+str(percent)+"%")
    return correct_answers, incorrect_answers, str(round(((correct_answers/total_answers)*100), 2))+"%"
    
            
