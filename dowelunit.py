def dowellunitfunction(data):
    unit = []
    u = unit
    d = data
    if d == 1:
        #  data collected is related to length
        u.append("meters", "centimeters", "kilometers", "milimeters", "lightyears", "foots", "yard", "inches", "mile", "feet" )
        return d, u
    elif d == 2:
        #  data collected is related to area
        u.append("meter squared", "km square", "cm square")
        return d, u 
    elif d == 3:
        #  data collected is related to volume
        u.append("meter cube", "km cube", "cm cube", "litre", "kilolitre", "mililitre")
        return d, u
    elif d == 4:
        #  data collected is related to weight
        u.append("grams", "kilograms", "centigrams", "miligrams", "quintal", "pound", "ton")
        return d, u
    elif d == 5:
        #  data collected is related to time
        u.append("nano seconds ", "seconds", "minute", "hour", "quarters", "day", "week", "month", "year", "decade")
        return d, u 
    elif d == 6:
        # this is a unit free quantity
        return d
    elif d == 7:
        # Display options for user to choose from
        u.append("Length (1)", "area (2)", "Volume (3)", "Weight (4)", "time (5)", "lot (6)")
        return u

if __name__ == "__main__":
    data = input("Enter data")
    dowellunitfunction(data)