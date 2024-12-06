# Author: Vlad Stefan

# Problem 1:
# Input: Text file with rules about page order and lists of pages
# Sum of the middle pages from correctly ordered lists.

with open('input.txt', 'r') as f:
    content = f.read().strip().split("\n\n")

ordering_rules = []
for line in content[0].strip().split("\n"):
    before, after = map(int, line.split('|'))
    ordering_rules.append((before, after))

updates = []
for line in content[1].strip().split("\n"):
    updates.append(list(map(int, line.split(','))))


def is_order_correct(update, rules):
    for before, after in rules:
        if before in update and after in update:
            if update.index(before) > update.index(after):
                return False
    return True


correct_updates = []
middle_values = []

for update in updates:
    if is_order_correct(update, ordering_rules):
        correct_updates.append(update)
        middle_index = len(update) // 2
        middle_values.append(update[middle_index])

middle_sum = sum(middle_values)

print(middle_sum)
