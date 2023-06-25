def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    numMales = int(input("Number of Male students registered: "))
    numFemales = int(input("Number of Female students registered: "))

    totalStudents = numMales + numFemales

    m_perc = (numMales / totalStudents) * 100
    f_perc = (numFemales / totalStudents) * 100

    print(f"The total number of students: \t\t", totalStudents)
    print(f"The number of males and females:\t", numMales,"\t\t", numFemales)
    print(f"The percentage of males and females: \t {m_perc:.2f}% \t {f_perc:.2f}%")

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
