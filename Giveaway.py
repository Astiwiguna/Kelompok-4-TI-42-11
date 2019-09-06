s = str(input("Sebutkan provider yang anda pakai : "))
i = float(input("Sebutkan ipk anda : "))

if s == "Telkomsel" or s == "telkomsel" and i >= 3.0:
    print("Selamat anda mendapat IPhone X")
elif s == "Telkomsel" or s == "telkomsel" and 2.75 <= i < 3.0:
    print("Selamat anda mendapat PS4")
elif s == "Telkomsel" or s == "telkomsel" and 2.25 <= i < 2.75:
    print("Selamat anda dapat voucher oyo")
else:
    print("Selamat dan Terima Kasih")