import colorama
from colorama import Fore

colorama.init(autoreset=True)


class ExpenseSharingApp:
    def __init__(self) -> None:
        self.friends = []

    def get_friends(self) -> None:
        number_of_friends = int(input(Fore.BLUE + "Enter number of friends among which the bill has to be split: "))
        for i in range(1, number_of_friends + 1):
            (self.friends.append(input(f"{Fore.CYAN}Friend {i}'s name: ").capitalize()))

    @staticmethod
    def show_expense_table(friends_list, share) -> None:
        max_name_length = max(len(name) for name in friends_list)
        max_amount_length = len("Amount to be Paid")

        print(f'{Fore.MAGENTA}\nSplitted Bill:')
        print(f"\n\t {'Name':<{max_name_length}} \t\t {'Amount to be Paid in Rupees':<{max_name_length}}")
        print("\t" + "-" * (max_name_length + max_amount_length + 25))
        for friend in friends_list:
            print(f"\t {friend:<{max_name_length}} \t\t ₹ {share[friend]:<{max_name_length}}")

    def split_bill(self, amount, split_type, balance=None):
        if amount <= 0:
            exit(f"{Fore.RED} Exited with code 0: Amount Can't be Negative")

        share = {person: 0 for person in self.friends}

        if split_type == "equal":
            equal_share = amount / len(self.friends)
            equal_share = round(equal_share, 2)
            for person in self.friends:
                share[person] = equal_share

        elif split_type == "proportional":
            proportions = [int(input(f'{Fore.BLUE}Enter proportion for {person}: ')) for person in self.friends]
            total_proportion = sum(proportions)
            for i, person in enumerate(self.friends):
                share[person] += round(((amount * proportions[i]) / total_proportion), 2)

        else:
            print(f'{Fore.RED}Invalid split type entered. Please choose \'equal\' or \'proportional\'.')
            return

        if balance:
            for person, amount in share.items():
                balance[person] += amount

        self.show_expense_table(self.friends, share)

    @staticmethod
    def show_payment_status(payment_status_list, friends) -> None:
        max_name_length = max(len(name) for name in friends)
        max_status_length = len("Paid/Not Paid")

        print(f'{Fore.MAGENTA}\nPayment Status:')

        print(f"\n\t {'Name':<{max_name_length}} \t\t {'Paid/Not Paid':{max_name_length}}")
        print("\t" + "-" * (max_name_length + max_status_length + 20))

        for name in friends:
            status = "Paid" if name in payment_status_list else "Not Paid"
            print(f"\t {name:<{max_name_length}} \t\t {status:<{max_name_length}}")

    def track_payments(self, balance) -> None:
        payment_status_list = []

        while True:
            payer_name = input(f"{Fore.BLUE}\nEnter name of person who paid or Press 0 to show payment status: ")
            if payer_name == "0":
                break

            if payer_name not in self.friends:
                print(f'{Fore.RED} Invalid Name')
            else:
                payment_status_list.append(payer_name)

            if sorted(self.friends) == sorted(payment_status_list):
                break

        self.show_payment_status(payment_status_list, self.friends)


if __name__ == "__main__":
    print(Fore.YELLOW + '\n\t\t\t\t\t\x1B[4m' + 'Expense Sharing App' + '\x1B[0m\n')

    app = ExpenseSharingApp()

    app.get_friends()

    total_amount = float(input(f"{Fore.BLUE}\nEnter Total Bill Amount: "))
    split_way = input(f"{Fore.BLUE}\nEnter Split Type (equal or proportional): ")
    app.split_bill(total_amount, split_way, None)

    app.track_payments(balance=None)
