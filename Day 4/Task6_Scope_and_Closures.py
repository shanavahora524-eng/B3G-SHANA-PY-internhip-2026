def make_validator(min_marks):

    def check_marks(marks):
        if marks>=min_marks:
            return"Valid"
        else:
            return"Invalid"
    return check_marks

Validator=make_validator(50)

print("Marks=21:",Validator(21))
print("Marks=90:",Validator(90))
print("Marks=20:",Validator(20))
print("Marks=75:",Validator(75))