def s_finder(names: list):
    name_dict = {}
    for name in names:
        if name[0] == "S":
            name_dict[name] = names.count(name)
    return name_dict


names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
print(s_finder(names))
