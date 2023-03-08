from banks import Bank

bank = Bank("Sicred", 821)

bank.create_current_account("Bruno", "Alves", 20, "06371938123")
bank.create_savings_account("Bruno", "Alves", 20, "06371938123")

print(bank)



