n = input("Please enter your name: ")
g = float(input("Please enter your GPA(0.0-4.0): "))
c = int(input("Please enter the total credit hours: "))
f = (g >= 3.5 and c >= 12)
print(f"Student name: {n}\nGPA: {g}\nTotal Credit Hours: {c}")
if not f:
    print()
    if g<3.5: print(f"Needed GPA points: {3.5 - g:.2f}")
    if c<12: print(f"Needed credits: {12 - c:.2f}")