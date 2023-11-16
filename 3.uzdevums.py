# Iegūt lietotāja ievadīto skaitli
skaitlis = int(input("Ievadiet skaitli: "))

# Pārbauda vai skaitlis ir nepāra
if skaitlis % 2 != 0:
    print(f"Ievadītais skaitlis {skaitlis} ir nepāra.")
else:
    print(f"Ievadītais skaitlis {skaitlis} ir pāra.")
