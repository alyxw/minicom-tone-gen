from twitchio.ext import commands
import minicom
import creds
import mysql.connector


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=creds.twitch_key, prefix="?", initial_channels=[creds.twitch_channel]
        )

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f"Logged in as | {self.nick}")

    @commands.command()
    async def tty(self, ctx: commands.Context):
        message = ctx.message.content
        message = message[5:]
        cnx = mysql.connector.connect(
            host=creds.db_host,
            port=creds.db_port,
            user=creds.db_user,
            password=creds.db_pass,
            database=creds.db_database,
        )

        cur = cnx.cursor()
        sql = "INSERT INTO messages (message) VALUES (%s)"
        val = message
        cur.execute(sql, (val,))
        cnx.commit()

    @commands.command()
    async def clear(self, ctx: commands.Context):
        message = "$$$CLEAR"
        cnx = mysql.connector.connect(
            host=creds.db_host,
            port=creds.db_port,
            user=creds.db_user,
            password=creds.db_pass,
            database=creds.db_database,
        )
        cur = cnx.cursor()
        sql = "INSERT INTO messages (message) VALUES (%s)"
        val = message
        cur.execute(sql, (val,))
        cnx.commit()


bot = Bot()
bot.run()
