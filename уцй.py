from data import db_session
from data.users import User


def main(g):
    db_session.global_init("db/" + g)
    db_sess = db_session.create_session()

    for user in db_sess.query(User).filter(User.age > 18):
        print(user, user.age, 'years')
    db_sess.commit()


main(input())