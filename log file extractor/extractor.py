with open("server.log.txt" , "r") as log_file:
 with open("error_report.txt" , "w") as report_file:
    for line in log_file:
        if "ERROR" in line:
            report_file.write(line)
             
