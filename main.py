import functions, math, time, os
start = time.time()


class App():
    def __init__(self):
        self.config = functions.load_config()
        self.ans_file = "answers.txt"
    def check_answers(self, testname):
        students_ans_count = 0
        _ca_temp = functions.read_answers(self.config[testname]['test_dir']+"\\answers.txt")
        _sa_temp = os.scandir(self.config[testname]['stud_ans_dir']+'\\')
        gui_return = []
        with open('results.txt','w') as f:
            for z in _sa_temp:
                s_ans = functions.read_answers(z.path)
                temp = list(functions.check(_ca_temp, s_ans))
                f.write(str(students_ans_count+1)+": "+str(temp)+"\n")
                students_ans_count += 1
                gui_return.append(temp)
        return gui_return

    def testing(self):
        print("working")
    
    def read_config(self):
        return self.config

    def save_config(self, conf):
        functions.save_config(conf)



if __name__ == "__main__":
    app = App()
    print(app.check_answers('test1'))
    print("running")
    end = time.time()
    print("finished compiling: "+str(end-start))
