for i in range(0,5):
    print("Uranus")
print("A znasz może inne planety układu słonecznego?")

num = 100
fibonacci = [1]

while len(fibonacci)<num:
    fibonacci.append(sum(fibonacci[-2:]))
print(fibonacci)
