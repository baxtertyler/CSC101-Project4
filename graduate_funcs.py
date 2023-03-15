# Project 4 – Graduate Rate (2017-2018)
# Name: Tyler Baxter
# Instructor: Dr. S. Einakian
# Section: 03
# classes and functionalities will be provided here

# class Division
class Division:
    def __init__(self, id_, name):
        self.id = id_
        self.division_name = name

    def __repr__(self):
        return str(self.id) + " " + str(self.division_name)


# class Graduate:
class Graduate:
    def __init__(self, id_, major, bachelor, master, doctor):
        self.id = id_
        self.major = major
        self.bachelor = bachelor
        self.master = master
        self.doctor = doctor

    def __eq__(self, other):
        return (self.bachelor == other.bachelor) and (self.master == other.master) and (self.doctor == other.doctor)

    def __repr__(self):
        return str(self.id) + " " + str(self.major) + " " + str(self.bachelor) + " " + \
               str(self.master) + " " + str(self.doctor)


# read file and return list of strings
def read_file(input_file):
    input_file_list = input_file.readlines()
    return input_file_list


# create list of Division objects
def create_division_objects(input_file_list):
    d_object_list = []
    for line in input_file_list:
        temp_list = line.split(",")
        if int(temp_list[0]) == 3200 or int(temp_list[0]) == 3400 or \
                int(temp_list[0]) == 3600 or int(temp_list[0]) == 3800:
            d_object_list.append(Division(temp_list[0], temp_list[1]))
    return d_object_list


# create list of Graduate objects
def create_graduate_objects(input_file_list):
    g_object_list = []
    for line in input_file_list:
        temp_list = line.split(",")
        if 3200 < int(temp_list[0]) < 3800 and not (int(temp_list[0]) == 3400 or int(temp_list[0]) == 3600):
            g_object_list.append(Graduate(temp_list[0], temp_list[1], (int(temp_list[2]), int(temp_list[3])),
                                          (int(temp_list[4]), int(temp_list[5])),
                                          (int(temp_list[6]), int(temp_list[7]))))
    return g_object_list


# create files for each division
def create_files(d_object_list, agriculture, computer, education, engineering):
    agriculture.write(str(d_object_list[0]) + '\n')
    computer.write(str(d_object_list[1]) + '\n')
    education.write(str(d_object_list[2]) + '\n')
    engineering.write(str(d_object_list[3]) + '\n')
    agriculture.write("ID " + "Major " + "Bachelor " + "Master " + "Doctor" + '\n')
    computer.write("ID " + "Major " + "Bachelor " + "Master " + "Doctor" + '\n')
    education.write("ID " + "Major " + "Bachelor " + "Master " + "Doctor" + '\n')
    engineering.write("ID " + "Major " + "Bachelor " + "Master " + "Doctor" + '\n')


# find total and average graduate for all divisions
def find_total_avg(g_object_list):
    ag_total = 0
    ag_cnt = 0
    co_total = 0
    co_cnt = 0
    ed_total = 0
    ed_cnt = 0
    en_total = 0
    en_cnt = 0
    total = 0
    cnt = 0
    for line in g_object_list:
        if 3200 < int(line.id) < 3400:
            ag_total += (find_graduation_rate(line)[0] + find_graduation_rate(line)[1])
            ag_cnt += 6
        elif 3400 < int(line.id) < 3600:
            co_total += (find_graduation_rate(line)[0] + find_graduation_rate(line)[1])
            co_cnt += 6
        elif 3600 < int(line.id) < 3800:
            ed_total += (find_graduation_rate(line)[0] + find_graduation_rate(line)[1])
            ed_cnt += 6
        else:
            en_total += (find_graduation_rate(line)[0] + find_graduation_rate(line)[1])
            en_cnt += 6
        total += (find_graduation_rate(line)[0] + find_graduation_rate(line)[1])
        cnt += 6
    return [(ag_total, ag_total / ag_cnt), (co_total, co_total / co_cnt), (ed_total, ed_total / ed_cnt),
            (en_total, en_total / en_cnt), (total, total / cnt)]


# find (female, male) graduate rate for given major
def find_graduation_rate(grad):
    return (grad.bachelor[0] + grad.master[0] + grad.doctor[0]), \
           (grad.bachelor[1] + grad.master[1] + grad.doctor[1])
