from data import db_session
from data.users import User


def main():
    db_session.global_init("db/blogs.db")
    users_data = [
        {"name": "Ridley",
         "surname": "Scott",
         "age": 21,
         "position": "captain",
         "speciality": "research engineer",
         "address": "module_1",
         "email": "scott_chief@mars.org"},
        {"name": "Name1",
         "surname": "Surname1",
         "age": 150,
         "position": "position1",
         "speciality": "speciality1",
         "address": "module_1",
         "email": "email1@mars.org"},
        {"name": "Name2",
         "surname": "Surname2",
         "age": -20,
         "position": "position2",
         "speciality": "speciality2",
         "address": "module_2",
         "email": "email2@mars.org"},
        {"name": "Name3",
         "surname": "Surname3",
         "age": 25,
         "position": "position3",
         "speciality": "speciality3",
         "address": "module_3",
         "email": "email3@mars.org"}
    ]
    for data in users_data:
        user = User()
        user.surname = data["surname"]
        user.name = data["name"]
        user.age = data["age"]
        user.position = data['position']
        user.speciality = data["speciality"]
        user.address = data["address"]
        user.email = data["email"]
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()


if __name__ == '__main__':
    main()