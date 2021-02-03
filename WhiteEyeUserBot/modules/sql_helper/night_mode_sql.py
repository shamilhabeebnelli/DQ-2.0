from sqlalchemy import Column, UnicodeText

from WhiteEyeUserBot.modules.sql_helper import BASE, SESSION


class Nightmode(BASE):
    __tablename__ = "nightmode"
    chat_id = Column(UnicodeText, primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Nightmode.__table__.create(checkfirst=True)


def add_nightmode(chat_id):
    nightmoddy = Nightmode(chat_id)
    SESSION.add(nightmoddy)
    SESSION.commit()


def rmnightmode(chat_id):
    rmnightmoddy = SESSION.query(Nightmode).get(chat_id)
    if rmnightmoddy:
        SESSION.delete(rmnightmoddy)
        SESSION.commit()


def get_all_chat_id():
    dayam = SESSION.query(Nightmode).all()
    SESSION.close()
    return dayam


def is_nightmode_indb(chat_id):
    try:
        return SESSION.query(Nightmode).filter(Nightmode.chat_id == chat_id).one()
    except:
        return None
    finally:
        SESSION.close()
