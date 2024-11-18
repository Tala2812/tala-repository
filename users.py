class User:
    def __init__(self, user_id, name):

        self._id = user_id
        self._name = name
        self._access_level = 'user'

    def get_id(self):
        return self._id


    def get_name(self):
        return self._name


    def get_access_level(self):
        return self._access_level


    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):

        super().__init__(user_id, name)

        self._access_level = 'admin'


    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Несуществующий пользователь.")


    def remove_user(self, user_list, user_id):

        for user in user_list:
            if user.get_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Пользователь не найден.")


if __name__ == "__main__":

    users = []


    admin = Admin(1, "Admin User")


    user1 = User(2, "Ната")
    user2 = User(3, "Алиса")
    user3 = User(4, "Костя")
    user4 = User(7, "Саша")


    admin.add_user(users, user1)
    admin.add_user(users, user2)
    admin.add_user(users, user3)
    admin.add_user(users, user4)


    admin.add_user(users, "Not a User Object")


    admin.remove_user(users, 5)


    admin.remove_user(users, 3)


    for user in users:
        print(f"ID пользователя: {user.get_id()}, Имя: {user.get_name()}")