# Loop over the elements of the fish_list list below, logging each one. 
# Terminate the loop immediately after printing the string 'Nemo'.

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break    

# Can you achieve the same result using a while loop? What would the code look like?
index = 0
while index < len(fish_list):
    print(fish_list[index])
    if fish_list[index] == 'Nemo':
        break
    index += 1