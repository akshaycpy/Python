s=input("Enter the string:")
vowels=0
consonant=0
for i in s:
    if(i=='i'or i=='o' or i=='u' or i=='a' or i=='e'):
        vowels=vowels+1
    else:
        consonant=consonant+1
print("Vowel is:",vowels)
print("Consonants are:",consonant)