for i in range(0,5):
    print("Uranus")
print("A znasz może inne planety układu słonecznego?")

num = 10
fibonacci = [1]

while len(fibonacci)<num:
    fibonacci.append(sum(fibonacci[-2:]))
print(fibonacci)

print("Ile to jeszcze będzie trwać?")
