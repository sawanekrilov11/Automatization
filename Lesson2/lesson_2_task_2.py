year = 1991 
def is_year_leap(year):
    if year % 4 == 0: # при делении на 4 нет знаков после запятой(0), то true, иначе false
        return True
    else:
        return False
result = is_year_leap(year)
print(f'Год {year}: {result}')