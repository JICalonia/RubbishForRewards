class RubbishForRewards:
    def __init__(self):
        self.max_weight = 15.00
        self.current_weight = 15.00

        self.trash_types = {
            1: ("Plastic", 5),
            2: ("Paper", 3),
            3: ("Cans", 7),
            4: ("Compost", 2)
        }

        self.bag_type = None
        self.collected_weight = 0.0

    def display_menu(self):
        print("\n==== RUBBISH-FOR-REWARDS ====")
        print("1. Start Collecting")
        print("2. Submit for Rewards")
        print("3. Exit")

    def start_collecting(self):
        print("\n---- Start Collecting ----")
        print("1. Plastic")
        print("2. Paper")
        print("3. Cans")
        print("4. Compost")

        # Prevent changing trash type while a bag exists
        if self.bag_type is not None:
            print(f"\nBag already contains: {self.bag_type}")
            print("Please submit the bag before collecting a new type.")
            return

        try:
            choice = int(input("\nSelect type: "))

            if choice not in self.trash_types:
                print("Invalid selection.")
                return

            print(f"\nCurrent bag net weight: {self.current_weight:.2f} kg")

            weight = float(input("Enter weight (in kg): "))

            if weight <= 0 or weight > self.current_weight:
                print("Invalid weight. Weight must be greater than 0 and less than or equal to 15.00 kg.")
                return

            trash_name, _ = self.trash_types[choice]

            self.bag_type = trash_name
            self.collected_weight = weight
            self.current_weight -= weight

            print("\nCollection Recorded!")
            print(f"Type: {trash_name}")
            print(f"Collected Weight: {weight:.2f} kg")
            print(f"Remaining Bag Net Weight: {self.current_weight:.2f} kg")

        except ValueError:
            print("Invalid input.")

    def submit_rewards(self):
        print("\n---- Submit for Rewards ----")

        if self.bag_type is None:
            print("No collection found.")
            return

        # Find reward points
        reward_points = 0

        for _, (name, points_per_kg) in self.trash_types.items():
            if name == self.bag_type:
                reward_points = self.collected_weight * points_per_kg
                break

        print(f"Reward earned: {reward_points:.2f} points")

        # Reset bag
        self.current_weight = self.max_weight
        self.bag_type = None
        self.collected_weight = 0.0

        print("Current bag net weight reset to 15.00 kg.")

    def run(self):
        while True:
            self.display_menu()

            choice = input("\nEnter choice: ")

            if choice == "1":
                self.start_collecting()

            elif choice == "2":
                self.submit_rewards()

            elif choice == "3":
                print("\nProgram terminated.")
                break

            else:
                print("Invalid choice. Please try again.")


# Create object and run the system
system = RubbishForRewards()
system.run()