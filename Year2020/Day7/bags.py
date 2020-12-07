class Bag:
    def __init__(self, name, sub_bags=None, contains_shiny=False, quant=None):
        if quant is None:
            quant = []
        if sub_bags is None:
            sub_bags = []
        self.name = name
        self.contains_shiny = contains_shiny
        self.sub_bags = sub_bags
        self.quant = quant

    def __repr__(self):
        return self.name


def parse_rule(rule: str) -> Bag:
    name, rule = rule.split(' bags contain ')
    sub_bags = [sub_bag.split(' ', 1)[1].split(' bag')[0] for sub_bag in rule.split(', ')]
    shiny_gold = name == 'shiny gold' or 'shiny gold' in sub_bags
    return Bag(name, sub_bags, shiny_gold)


def parse_rule_with_quant(rule: str) -> Bag:
    name, rule = rule.split(' bags contain ')

    if rule == 'no other bags.':
        return Bag(name)
    sub_bags = [sub_bag.split(' ', 1) for sub_bag in rule.split(', ')]
    quants = []
    sub_bag_names = []
    for sub_bag in sub_bags:
        quants.append(int(sub_bag[0]))
        sub_bag_names.append(sub_bag[1].split(' bag', 1)[0])
    return Bag(name, sub_bag_names, quant=quants)


def part_1(rules):
    bags = []
    for rule in rules:
        new_bag = parse_rule(rule)
        bags.append(new_bag)

    counter = 0
    while changes := True:
        changes = False
        for bag in bags:
            if bag.contains_shiny:
                for look_up_bag in bags:
                    if not look_up_bag.contains_shiny:
                        names = [sub_bag for sub_bag in look_up_bag.sub_bags]
                        if bag.name in names and not look_up_bag.contains_shiny:
                            look_up_bag.contains_shiny = True
                            changes = True
        if not changes:
            break
    print(len([bag for bag in bags if bag.contains_shiny]) - 1)


def part_2(rules):
    bags = []
    for rule in rules:
        new_bag = parse_rule_with_quant(rule)
        bags.append(new_bag)

    counter = 0
    bags_to_count = [bag for bag in bags if bag.name == 'shiny gold']
    while len(bags_to_count) != 0:
        bag = bags_to_count.pop(0)
        counter += sum([subs for subs in bag.quant])
        for quant, sub_bag in zip(bag.quant, bag.sub_bags):
            for index in range(quant):
                bags_to_count.append([bag_to_add for bag_to_add in bags
                                      if bag_to_add.name == sub_bag][0])

    print(counter)


def main():
    # with open('test_rules.txt') as file:
    #     rules = file.read().split('\n')
    #     part_1(rules)
    with open('test_part_2.txt') as file:
        rules = file.read().split('\n')
        part_2(rules)
    with open('input.txt') as file:
        rules = file.read().split('\n')
        part_1(rules)
        part_2(rules)


if __name__ == '__main__':
    main()
