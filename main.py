import telebot
import datetime
import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.__create_table()
        
    def __create_table(self):
        sql = self.connect_db()
            
        self.close_db(sql["cursor"], sql["connect"])
        
        
    def connect_db(self):
        with sqlite3.connect(self.db_name) as connect:
            cursor = connect.cursor()
        return {"connect": connect, "cursor": cursor}
    def close_db(self, cursor, connect):
        cursor.close()
        connect.close()
            

class TelegramBot(Database):
    def __init__(self, db_name, token):
        super().__init__(db_name)
        self.bot = telebot.TeleBot(token)
        self.router()
    def router(self):
        @self.bot.message_handler(commands=['start'])
        def start(message):
            print(message)
            self.bot.send_message(
                message.chat.id,
                f"Добро пожаловать, {message.from_user.first_name}!"    
            )
        @self.bot.message_handler(func=lambda message: True)
        def echo_all(message):
            self.bot.reply_to(
                message,
                "Не понимаю..."
            )
            self.bot.delete_message(
                chat_id=message.chat.id,
                message_id=message.message_id
            )
        self.bot.polling()    


TelegramBot(
    db_name = "tg.db",
    token = "6918195159:AAF0kkXbsaXCk8oa-ocCm1iMAqgSU5AA2WU"
)