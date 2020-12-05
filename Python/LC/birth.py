import datetime as dt
def gen(birth_year):
    current_year = dt.datetime.now().year
    age = current_year-birth_year
    gen = "Index Boomer" if 1946<birth_year<1964 else "Gen X" if 1965<birth_year<1976 else "Millennials" if 1977<birth_year<1995 else "Gen Z" if 1996<birth_year<current_year else "Ancient"
    return "You are "+ str(age) +" years old and belong to "+ gen         

print(gen(2029))
