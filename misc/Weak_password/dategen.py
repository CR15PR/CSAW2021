year= 1970

mangler = ["aaron","aaronaaron","noraa","Aaron","AARON","44r0n","4@r0n","@4r0n","@@r0n"]

with open("dates.txt", "w") as dates:
    while year < 2022:
        month = 1
        while month < 13:
            day=1
            while day < 32:
                daystr = f"{day:02d}"
                monstr = f"{month:02d}"
                yearstr = str(year)
                for i in mangler:
                    dates.write(i+yearstr+monstr+daystr+"\n")
                    dates.write(yearstr+monstr+daystr+i+"\n")
                day+=1
            month +=1
        year +=1
