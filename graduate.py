# Project 4 – Graduate Rate (2017-2018)
# Name: Tyler Baxter
# Instructor: Dr. S. Einakian
# Section:
# main program

from graduate_funcs import *


def main():
    file1 = open("graduate_rate.csv", "r")
    agriculture = open("agriculture.csv", "w")
    computer = open("computer.csv", "w")
    education = open("education.csv", "w")
    engineering = open("engineering.csv", "w")
    header1 = file1.readline()
    header2 = file1.readline()
    header3 = file1.readline()
    file = read_file(file1)
    d_list = create_division_objects(file)
    g_list = create_graduate_objects(file)
    create_files(d_list, agriculture, computer, education, engineering)
    find_total_avg(d_list, g_list)
    avg_list = find_total_avg(d_list, g_list)
    total_ag = avg_list[0][0]
    total_co = avg_list[1][0]
    avg_co = avg_list[1][1]
    total_ed = avg_list[2][0]
    total_en = avg_list[3][0]
    total = avg_list[4][0]

    for obj in g_list:
        if 3200 < int(obj.id) < 3400:
            agriculture.write(str(obj.id) + " " + str(obj.major) + " " +
                              str(obj.bachelor[0] + obj.bachelor[1]) + " " +
                              str(obj.master[0] + obj.master[1]) + " " +
                              str(obj.doctor[0] + obj.doctor[1]) + "\n")
        if 3400 < int(obj.id) < 3600:
            computer.write(str(obj.id) + " " + str(obj.major) + " " +
                           str(obj.bachelor[0] + obj.bachelor[1]) + " " +
                           str(obj.master[0] + obj.master[1]) + " " +
                           str(obj.doctor[0] + obj.doctor[1]) + "\n")
        if 3600 < int(obj.id) < 3800:
            education.write(str(obj.id) + " " + str(obj.major) + " " +
                            str(obj.bachelor[0] + obj.bachelor[1]) + " " +
                            str(obj.master[0] + obj.master[1]) + " " +
                            str(obj.doctor[0] + obj.doctor[1]) + "\n")
        else:
            engineering.write(str(obj.id) + " " + str(obj.major) + " " +
                              str(obj.bachelor[0] + obj.bachelor[1]) + " " +
                              str(obj.master[0] + obj.master[1]) + " " +
                              str(obj.doctor[0] + obj.doctor[1]) + "\n")

    print("Total OF Processed Graduate in Computer and information sciences and support: " + str(total_co))
    print("Average of Processed Female and Male in Computer and information sciences and support: " + str(avg_co))
    print("Total of all Females and Males Graduate in all Majors: " + str(total))
    print("Compare total graduate rate of Computer and information sciences and support to all other Majors: ")
    if total_co > total_ag:
        print("    Rate of Computer and information sciences is > rate of Agriculture operations and related sciences")
    else:
        print("    Rate of Computer and information sciences is < rate of Agriculture operations and related sciences")
    if total_co > total_ed:
        print("    Rate of Computer and information sciences is > rate of Education")
    else:
        print("    Rate of Computer and information sciences is < rate of Education")
    if total_co > total_en:
        print("    Rate of Computer and information sciences is > rate of Engineering technologies/construction "
              "trades/mechanics and repairers")
    else:
        print("    Rate of Computer and information sciences is < rate of Engineering technologies/construction "
              "trades/mechanics and repairers")

    file1.close()
    agriculture.close()
    computer.close()
    education.close()
    engineering.close()


if __name__ == '__main__':
    main()
