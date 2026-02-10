from tabulate import tabulate

# Views all members
def view_all_members(members):
    if not members:
        print("\nNo members found\n")
        return
    print(tabulate(members, headers="keys", tablefmt="fancy_grid"))