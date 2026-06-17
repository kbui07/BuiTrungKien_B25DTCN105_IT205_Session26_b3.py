from abc import ABC, abstractmethod


class Champion(ABC):
    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    def get_combat_power(self):
        return self.base_hp + self.calculate_skill_damage() * 1.5

    def __add__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __gt__(self, other):
        return self.get_combat_power() > other.get_combat_power()


class Warrior(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power

    def calculate_skill_damage(self):
        return self.base_atk * self.ability_power


champion_pool = [
    Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
    Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
    Mage("MAG01", "Rikkei Wizard", 800, 500, 2.0)
]


def find_champion(champion_id):
    for champion in champion_pool:
        if champion.champion_id == champion_id:
            return champion
    return None


def show_champions():
    print("\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
    for champion in champion_pool:
        if isinstance(champion, Warrior):
            role = "Warrior"
            info = f"Armor: {champion.shield_bonus}"
        else:
            role = "Mage"
            info = f"AP: {champion.ability_power}"

        print(
            f"{champion.champion_id} | "
            f"{champion.name} | "
            f"{role} | "
            f"HP: {champion.base_hp} | "
            f"ATK: {champion.base_atk} | "
            f"{info} | "
            f"Chiến lực: {champion.get_combat_power():.0f}"
        )

def add_champion():
    print("1. Warrior")
    print("2. Mage")
    champion_type = input("Chọn hệ: ")
    champion_id = input("Nhập mã tướng: ").upper()
    if find_champion(champion_id):
        print("Mã tướng đã tồn tại!")
        return

    name = input("Nhập tên tướng: ")
    hp = int(input("Nhập HP: "))
    atk = int(input("Nhập ATK: "))
    match champion_type:
        case "1":
            armor = int(input("Nhập Armor: "))
            champion = Warrior(champion_id, name, hp, atk, armor)
        case "2":
            ap = float(input("Nhập Ability Power: "))
            champion = Mage(champion_id, name, hp, atk, ap)
        case _:
            print("Lựa chọn không hợp lệ!")
            return

    champion_pool.append(champion)
    print("Thêm tướng thành công!")
    print(
        f"Mã: {champion.champion_id} | "
        f"Tên: {champion.name} | "
        f"Chiến lực: {champion.get_combat_power():.0f}"
    )


def compare_champions():
    print("\n--- SO SÁNH SỨC MẠNH ---")
    id1 = input("Nhập mã tướng thứ nhất: ").upper()
    id2 = input("Nhập mã tướng thứ hai: ").upper()
    c1 = find_champion(id1)
    c2 = find_champion(id2)

    if c1 is None:
        print(f"Mã tướng {id1} không hợp lệ!")
        return
    if c2 is None:
        print(f"Mã tướng {id2} không hợp lệ!")
        return

    print(
        f"{c1.champion_id} - {c1.name} | "
        f"Chiến lực: {c1.get_combat_power():.0f}"
    )
    print(
        f"{c2.champion_id} - {c2.name} | "
        f"Chiến lực: {c2.get_combat_power():.0f}"
    )

    if c1 > c2:
        print(
            f"Kết quả: {c1.champion_id} - {c1.name} "
            f"mạnh hơn {c2.champion_id} - {c2.name}"
        )
    else:
        print(
            f"Kết quả: {c2.champion_id} - {c2.name} "
            f"mạnh hơn {c1.champion_id} - {c1.name}"
        )


def team_power():
    print("\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH ---")
    ids = input("Nhập danh sách mã tướng (cách nhau bằng dấu phẩy): ").split(",")
    total = 0
    index = 1

    print("\nDanh sách đội hình:")
    for champion_id in ids:
        champion_id = champion_id.strip().upper()
        champion = find_champion(champion_id)
        if champion is None:
            print(f"Mã tướng {champion_id} không hợp lệ, bỏ qua!")
            continue

        print(
            f"{index}. {champion.champion_id} - "
            f"{champion.name} | "
            f"Chiến lực: {champion.get_combat_power():.0f}"
        )
        total = champion + total
        index += 1

    print(f"\nTổng chiến lực đội hình: {total:.0f}")


while True:
    print("\n===== RIKKEI RPG - AUTO BATTLER =====")
    print("1. Hiển thị bể tướng")
    print("2. Thêm quân cờ mới")
    print("3. So sánh 2 quân cờ")
    print("4. Tính tổng chiến lực đội hình")
    print("5. Thoát")

    choice = input("Chọn chức năng (1-5): ")
    match choice:
        case "1":
            show_champions()

        case "2":
            add_champion()

        case "3":
            compare_champions()

        case "4":
            team_power()

        case "5":
            print(
                "Cảm ơn bạn đã sử dụng "
                "Rikkei RPG - Auto-Battler Manager!"
            )
            break

        case _:
            print("Lựa chọn không hợp lệ!")