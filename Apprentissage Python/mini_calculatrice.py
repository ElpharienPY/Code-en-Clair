print("Bienvenue dans la mini-calculatrice")
a = float(input("Entre un nombre : "))
print("Quelle operation (+, -, *, /) ?")
op = input()

while op not in ['+', '-', '*', '/']:
    print("Operation invalide. Recommence.")
    op = input()
    
b = float(input("Entre un autre nombre : "))

if op == '+':
    print(f"{a} + {b} = {a + b}") # ou print(a, "+"" ,b "=",a + b)) mais laborieux

elif op == '-':
    print(f"{a} - {b} = {a - b}")

elif op == '*':
    print(f"{a} * {b} = {a * b}")

elif op == '/':
    if b == 0:
        print("Erreur : Division par zero.")
    else:
        print(f"{a} / {b} = {a / b}")
        
# Mini-calculatrice
