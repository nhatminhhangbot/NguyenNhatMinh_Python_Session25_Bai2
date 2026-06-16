class NetflixAccount:
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            raise ValueError("Mật khẩu quá ngắn. Tối thiểu 6 ký tự.")
        self.__password = new_password

    @property
    def plan(self):
        return self.__plan

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        cls.max_profiles = new_limit

    def add_profile(self, profile_name):
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này")
            return
        self.profiles.append(profile_name)
        print(f"Đã thêm người xem: {profile_name}")

    def upgrade_plan(self, new_plan):
        valid_plans = ["Basic", "Standard", "Premium"]
        if new_plan in valid_plans:
            self.__plan = new_plan
            print(f"Đã nâng cấp lên gói cước: {new_plan}")
        else:
            print("Gói cước không hợp lệ")

    def display_info(self):
        print(f"\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Nền tảng: {self.platform_name}")
        print(f"Email: {self.email}")
        print(f"Mật khẩu: {self.password}")
        print(f"Gói cước hiện tại: {self.plan}")
        print(
            f"Danh sách người xem: {', '.join(self.profiles) if self.profiles else 'Chưa có'}")


def register_new_account():
    print("\n--- ĐĂNG KÝ TÀI KHOẢN MỚI ---")
    email = input("Nhập email: ").strip()
    if not NetflixAccount.validate_email(email):
        print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")
        return None

    account = NetflixAccount(email)

    while True:
        password = input("Nhập mật khẩu (tối thiểu 6 ký tự): ")
        try:
            account.password = password
            print("Đăng ký tài khoản thành công")
            return account
        except ValueError as e:
            print(f"Lỗi bảo mật: {e}")


def view_info(current_account):
    if current_account is None:
        print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
        return
    current_account.display_info()


def add_profile(current_account):
    if current_account is None:
        print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
        return

    print("\n--- THÊM NGƯỜI XEM ---")
    profile_name = input("Nhập tên người xem mới: ").strip()
    if profile_name:
        current_account.add_profile(profile_name)
    else:
        print("Tên người xem mới không được để trống")
        return


def upgrade_plan(current_account):
    if current_account is None:
        print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
        return

    print("\n--- NÂNG CẤP GÓI CƯỚC ---")
    print("Các gói hiện có: Basic, Standard, Premium")
    new_plan = input("Nhập tên gói cước muốn nâng cấp: ").strip()
    current_account.upgrade_plan(new_plan)


def update_policy():
    print("\n--- CẬP NHẬT CHÍNH SÁCH NETFLIX ---")
    try:
        limit = int(input("Nhập số lượng Profile tối đa mới: "))
        NetflixAccount.update_max_profiles(limit)
        print(
            f"Đã cập nhật giới hạn Profile toàn hệ thống thành {NetflixAccount.max_profiles}")
    except ValueError:
        print("Vui lòng nhập một con số hợp lệ")


def main():
    current_account = None
    while True:
        print("\n===== NETFLIX ACCOUNT MANAGER =====")
        print("1. Đăng ký tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Thêm người xem")
        print("4. Nâng cấp gói cước")
        print("5. Cập nhật chính sách Netflix (Admin)")
        print("6. Thoát chương trình")
        print("===================================")
        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == '1':
            current_account = register_new_account()
        elif choice == '2':
            view_info(current_account)
        elif choice == '3':
            add_profile(current_account)
        elif choice == '4':
            upgrade_plan(current_account)
        elif choice == '5':
            update_policy()
        elif choice == '6':
            print("Cảm ơn bạn đã sử dụng Netflix Account Manager!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 6!")


if __name__ == "__main__":
    main()
