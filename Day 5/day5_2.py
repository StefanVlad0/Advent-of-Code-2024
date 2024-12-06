# Author: Vlad Stefan

# Problem 1:
# Input: Text file with rules about page order and lists of pages
# Output: Sum of middle page numbers from corrected updates that are reordered based on the rules.


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


def sort_update(update, rules):
    ordered_update = update[:]
    for _ in range(len(ordered_update)):
        for before, after in rules:
            if before in ordered_update and after in ordered_update:
                idx_before = ordered_update.index(before)
                idx_after = ordered_update.index(after)
                if idx_before > idx_after:
                    ordered_update.remove(after)
                    ordered_update.insert(idx_before, after)
    return ordered_update


middle_sum = 0

for update in updates:
    if not is_order_correct(update, ordering_rules):
        corrected_update = sort_update(update, ordering_rules)
        middle_index = len(corrected_update) // 2
        middle_sum += corrected_update[middle_index]

print(middle_sum)
