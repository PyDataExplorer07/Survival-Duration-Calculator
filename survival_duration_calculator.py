class SurvivalDurationCalculator:
    def __init__(self, age_years):
        self.age_years = age_years
        self.months_in_year = 12
        self.weeks_in_year = 52
        self.days_in_year = 365.25          # Accounting for Leap year
        self.hours_in_day = 24
        self.minutes_in_hour = 60
        self.seconds_in_minute = 60

    def calculate_duration(self, unit):
        if unit.lower() in ['m','months']:
            return self.age_years * self.months_in_year , 'Months'
        elif unit.lower() in ['w','weeks']:
            return self.age_years * self.weeks_in_year , 'Weeks'
        elif unit.lower() in ['d','days']:
            return self.age_years * self.days_in_year , 'Days'
        elif unit.lower() in ['h','hour']:
            return self.age_years * self.days_in_year * self.hours_in_day , 'Hours'
        elif unit.lower() in ['min','minute']:
            return self.age_years * self.months_in_year * self.hours_in_day * self.minutes_in_hour , 'Minutes'
        elif unit.lower() in ['s','second']:
            return self.age_years * self.months_in_year * self.hours_in_day * self.minutes_in_hour * self.seconds_in_minute , 'Seconds'
        else:
            return None , None


age = float(input("What's your age? "))
Calculator = SurvivalDurationCalculator(age)

unit = input("Please choose a time unit (Months , Weeks , Days , Hours , Minutes , Seconds) ")

result , unit_name = Calculator.calculate_duration(unit)

if result is not None:
    print(f"You lived for {result} {unit_name}")

else:
    print("Invalid time unit selected.")


